import pandas as pd
import numpy as np

def rank_patients(inputs):
    '''
    Rank patients by priority. Priority groups are assigned in reverse order so each
    patient gets the highest possible priority given their data.
    
    Parameters:
    ----------------------------------
    inputs: pd.DataFrame.
        Data frame with patients blood glucose time series observed at 5 minutes frequency.
        The data frame should contain the following columns:
        - 'patient_id': Patient id.
        - 'patient_name': Patient name.
        - 'population': Patient population.
        - 'ts': Timestamp.
        - 'bg': Patient blood glucose level.
        - 'most_recent_week': 1 if the timestamp is within the last 7 days, 0 otherwise.
    
    Returns:
    ----------------------------------
    output: pd.DataFrame.
        Data frame with patients blood glucose time series observed at 5 minutes frequency
        including patients ranks and patients priority groups.
        The data frame contains the following columns:
        - 'patient_id': Patient id.
        - 'patient_name': Patient name.
        - 'population': Patient population.
        - 'ts': Timestamp.
        - 'bg': Patient blood glucose level.
        - 'most_recent_week': 1 if the timestamp is within the last 7 days, 0 otherwise.
        - 'patient_rank': Patient rank.
        - 'review':  Patient priority group.
        - 'time_worn (%)': Percentage of time that the patient has worn the device over a given week.
        - 'in_range': 1 of the patient blood glucose level is between 70 and 180, 0 otherwise.
        - 'in_range (%)': Percentage of time that the patient blood glucose level has been between 70 and 180 over a given week.
        - 'hypo': 1 of the patient blood glucose level is between 54 and 70, 0 otherwise.
        - 'hypo (%)': Percentage of time that the patient blood glucose level has been between 54 and 70 over a given week.
        - 'extreme_hypo': 1 of the patient blood glucose level is less than 54, 0 otherwise.
        - 'extreme_hypo (%)': Percentage of time that the patient blood glucose level has been below 54 over a given week.
    '''
    
    # Add columns for in range, hypo, extreme hypo.
    inputs = inputs.copy()
    inputs['in_range'] = np.where((inputs['bg'] <= 180) & (inputs['bg'] >= 70), 1.0, 0.0)
    inputs['hypo'] = np.where((inputs['bg'] < 70) & (inputs['bg'] >= 54), 1.0, 0.0)
    inputs['extreme_hypo'] = np.where(inputs['bg'] < 54, 1.0, 0.0)
    
    # Calculate weekly averages for in range, hypo, extreme hypo.
    average = inputs.drop(labels=['bg'], axis=1).groupby(['patient_id', 'most_recent_week']).mean()
    
    # Calculate percentage of time worn by week.
    time_worn = inputs.set_index('ts')[['most_recent_week', 'patient_id', 'bg']].copy()
    time_worn = time_worn.groupby(by=['patient_id', 'most_recent_week'])['bg'].resample('5T').last().reset_index()
    time_worn = time_worn.groupby(by=['patient_id', 'most_recent_week'])['bg'].agg(lambda x: pd.notna(x).sum() / (7 * 24 * 60 / 5))
    time_worn.name = 'time_worn'
    average = average.join(time_worn).reset_index()
    
    # Split data by week.
    current_week = average[average['most_recent_week'] == 1].copy()
    previous_week = average.loc[average['most_recent_week'] == 0, ['patient_id', 'in_range']].copy()
    previous_week.rename(columns={'in_range': 'tir_prev_week'}, inplace=True)
    
    # Calculate rankings for current week.
    ranks = pd.merge(current_week, previous_week, how='outer', on='patient_id')
    ranks = ranks.fillna({'tir_prev_week': 0})
    ranks['patient_rank'] = ranks[['in_range']].apply(tuple, axis=1).rank(method='dense', ascending=True, na_option='bottom').astype(int)
    
    # Group 5: Missing/insufficient data (default).
    ranks['review'] = '(5) Missing/insufficient data'
    
    # Group 6: No alerts.
    ranks.loc[((ranks['extreme_hypo'] <= 0.01) & (ranks['hypo'] <= 0.03) & (ranks['in_range'] - ranks['tir_prev_week'] >= -0.15) &
               (ranks['in_range'] >= 0.65) & (ranks['time_worn'] >= 0.5)), 'review'] = '(6) No alerts'
    
    # Group 4: Low TIR.
    ranks.loc[((ranks['in_range'] < 0.65) & (ranks['time_worn'] > 0.5)), 'review'] = '(4) Low TIR'
    
    # Group 3: Highest change in TIR.
    ranks.loc[(ranks['in_range'] - ranks['tir_prev_week'] < -0.15) & (ranks['time_worn'] > 0.5), 'review'] = '(3) Large drop in TIR'
    
    # Group 2: High lows (all patients with > 3%, low).
    ranks.loc[((ranks['hypo'] > 0.03) & (ranks['time_worn'] > 0.5)), 'review'] = '(2) High lows'
    
    # Group 1: High extreme lows (all patients with > 1%, extreme low).
    ranks.loc[((ranks['extreme_hypo'] > 0.01) & (ranks['time_worn'] > 0.5)), 'review'] = '(1) High extreme lows'
    
    # Add back the raw data.
    output = pd.merge(left=inputs, right=ranks[['patient_id', 'review', 'patient_rank']], on=['patient_id'])
    
    # Add back the weekly stats.
    average = average.rename(columns={'in_range': 'in_range (%)', 'hypo': 'hypo (%)', 'extreme_hypo': 'extreme_hypo (%)', 'time_worn': 'time_worn (%)'})
    output = pd.merge(left=output, right=average, on=['patient_id', 'most_recent_week'])
    
    return output[['patient_id', 'patient_name', 'population', 'ts', 'bg', 'most_recent_week', 'patient_rank', 'review', 'time_worn (%)',
                   'in_range', 'in_range (%)', 'hypo', 'hypo (%)', 'extreme_hypo', 'extreme_hypo (%)']]
