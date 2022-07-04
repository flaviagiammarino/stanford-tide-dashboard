import pandas as pd
import numpy as np

def preprocess_data(df):
    '''
    Preprocess the patients' time series dataset.

    Parameters:
    ----------------------------------
    df: pd.DataFrame.
        Patients' time series dataset.
        Data frame with the following columns:

        'id': int.
            Patient id.

        'ts': pd.datetime.
            Timestamp.

        'bg': float.
            Blood glucose level.

    Returns:
    ----------------------------------
    df: pd.DataFrame.
        Preprocessed patients' time series dataset.
        Data frame with the following columns:

        'id': int.
            Patient id.

        'ts': pd.datetime.
            Timestamp.

        'bg': float.
            Blood glucose level.

        'most_recent_week': float.
            1.0 if the timestamp falls within the most recent week, 0.0 otherwise.

        'device_worn': float.
            1.0 if the patient is wearing the device, 0.0 otherwise.

        'extreme_hypo': float.
            1.0 if the patient's blood glucose level is less than 54, 0.0 otherwise.

        'hypo': float.
            1.0 if the patient's blood glucose level is between 54 and 70, 0.0 otherwise.

        'in_range': float.
            1.0 if the patient's blood glucose level is between 70 and 180, 0.0 otherwise.

        'hyp': float.
            1.0 if the patient's blood glucose level is between 180 and 250, 0.0 otherwise.

        'extreme_hyp': float.
            1.0 if the patient's blood glucose level is greater than 250, 0.0 otherwise.

        'device_worn (%)': float.
            Percentage of time that the patient has worn the device over a given week.

        'extreme_hypo (%)': float.
            Percentage of time that the patient's blood glucose level has been less than 54 over a given week.

        'hypo (%)': float.
            Percentage of time that the patient's blood glucose level has been between 54 and 70 over a given week.

        'in_range (%)': float.
            Percentage of time that the patient's blood glucose level has been between 70 and 180 over a given week.

        'hyp (%)': float.
            Percentage of time that the patient's blood glucose level has been between 180 and 250 over a given week.

        'extreme_hyp (%)': float.
            Percentage of time that the patient's blood glucose level has been greater than 250 over a given week.
        
        'bg (avg)': float.
            Patient's average blood glucose level over a given week.
        
        'rank': int.
            Patient's rank.
        
        'review': str.
            Patient's priority group.
    '''
    
    # Parse the timestamps.
    df['ts'] = pd.to_datetime(df['ts'])
    
    # Infer the frequency of the time series (in minutes)
    freq = df.groupby(by='id')['ts'].diff().mode()[0].total_seconds() / 60
    
    # Resample all the time series at the same frequency.
    df = df.set_index('ts').groupby(by='id')['bg'].resample(f'{freq}T').last().reset_index()
    
    # Add flag for most recent week.
    df['most_recent_week'] = np.where(df['ts'].max() - df['ts'] < pd.Timedelta(days=7), 1., 0.)
    
    # Add flag for device worn.
    df['device_worn'] = np.where(pd.notna(df['bg']), 1., 0.)
    
    # Add flags for extreme hypo, hypo, in range, hyp, extreme hyp.
    df['extreme_hypo'] = np.where(df['bg'] < 54, 1., 0.)
    df['hypo'] = np.where((df['bg'] >= 54) & (df['bg'] < 70), 1., 0.)
    df['in_range'] = np.where((df['bg'] >= 70) & (df['bg'] <= 180), 1., 0.)
    df['hyp'] = np.where((df['bg'] > 180) & (df['bg'] <= 250), 1., 0.)
    df['extreme_hyp'] = np.where(df['bg'] > 250, 1., 0.)
    df.loc[df['device_worn'] == 0., ['extreme_hypo', 'hypo', 'in_range', 'hyp', 'extreme_hyp']] = np.nan
    
    # Calculate the weekly percentages of time worn, time in extreme hypo, time in hypo, time in range, time in hyp, time in extreme hyp.
    stats = df.drop(labels=['ts', 'bg'], axis=1).groupby(by=['id', 'most_recent_week']).mean()
    stats.columns = [x + ' (%)' for x in stats.columns]
    
    # Calculate the weekly average blood glucose level.
    stats = stats.join(df.groupby(by=['id', 'most_recent_week'])['bg'].mean())
    stats = stats.rename(columns={'bg': 'bg (avg)'}).reset_index(drop=False)

    # Prepare the data for ranking.
    data = pd.merge(
        left=stats.loc[stats['most_recent_week'] == 0., ['id', 'in_range (%)']].rename(columns={'in_range (%)': 'in_range_previous_week (%)'}),
        right=stats.loc[stats['most_recent_week'] == 1., ['id', 'device_worn (%)', 'in_range (%)', 'hypo (%)', 'extreme_hypo (%)']],
        on='id',
        how='outer'
    ).fillna({'in_range_previous_week (%)': 0.})

    # Rank the patients by time in range over the most recent week.
    data['rank'] = data[['in_range (%)']].apply(tuple, axis=1).rank(method='dense', ascending=True, na_option='bottom').astype(int)

    # Assign the patients to priority groups.
    data['review'] = prioritize_patients(data)

    # Add the weekly statistics to the input data frame.
    df = pd.merge(left=df, right=stats, on=['id', 'most_recent_week'])
    
    # Add the ranks and priority groups to the input data frame.
    df = pd.merge(left=df, right=data[['id', 'rank', 'review']], on='id')
    
    return df


def prioritize_patients(data):
    '''
    Assign the patients to priority groups. Priority groups are assigned in reverse
    order so each patient gets the highest possible priority given their data.

    Parameters:
    ----------------------------------
    data: pd.DataFrame.
        Data frame with the following columns:

        'id': int.
            Patient id.

        'device_worn (%)': float.
            Percentage of time that the patient has worn the device over the most recent week.

        'in_range (%)': float.
            Percentage of time that the patient's blood glucose level has been between 70 and 180 over the most recent week.

        'hypo (%)': float.
            Percentage of time that the patient's blood glucose level has been between 54 and 70 over the most recent week.
 
        'extreme_hypo (%)': float.
            Percentage of time that the patient's blood glucose level has been less than 54 over the most recent week.
        
        'in_range_previous_week (%)': float.
            Percentage of time that the patient's blood glucose level has been between 70 and 180 over the previous week.
 
    Returns:
    ----------------------------------
    review: pd.Series.
        Patients priority groups.
    '''
    
    # Group 5: Missing/insufficient data (default).
    review = pd.Series(data='(5) Missing/insufficient data', index=data.index)
    
    # Group 6: No alerts.
    # - time in range didn't decrease by more than 15% over the most recent week
    # - time in extreme hypo was at most 1% over the most recent week
    # - time in hypo was at most 4% over the most recent week
    # - time in range was at least 65% over the most recent week
    # - time worn was at least 50% over the most recent week
    review[(data['in_range (%)'] - data['in_range_previous_week (%)'] >= - 0.15) &
           (data['extreme_hypo (%)'] <= 0.01) &
           (data['hypo (%)'] <= 0.04) &
           (data['in_range (%)'] >= 0.65) &
           (data['device_worn (%)'] >= 0.5)] = '(6) No alerts'
    
    # Group 4: Low TIR.
    # - time in range was less than 65% over the most recent week
    # - time worn was more than 50% over the most recent week
    review[(data['in_range (%)'] < 0.65) &
           (data['device_worn (%)'] > 0.5)] = '(4) Low TIR'
    
    # Group 3: Large drop in TIR.
    # - time in range decreased by more than 15% over the most recent week
    # - time worn was more than 50% over the most recent week
    review[(data['in_range (%)'] - data['in_range_previous_week (%)'] < - 0.15) &
           (data['device_worn (%)'] > 0.5)] = '(3) Large drop in TIR'
    
    # Group 2: High lows.
    # - time in hypo was more than 4% over the most recent week
    # - time worn was more than 50% over the most recent week
    review[(data['hypo (%)'] > 0.04) &
           (data['device_worn (%)'] > 0.5)] = '(2) High lows'
    
    # Group 1: High extreme lows.
    # - time in extreme hypo was more than 1% over the most recent week
    # - time worn was more than 50% over the most recent week
    review[((data['extreme_hypo (%)'] > 0.01) &
            (data['device_worn (%)'] > 0.5))] = '(1) High extreme lows'
    
    return review
