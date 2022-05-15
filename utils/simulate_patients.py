import string
import datetime
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.ndimage import gaussian_filter1d

def simulate_patients(start, num, populations, seed=42):
    '''
    Generate artificial blood glucose level time series at 5 minutes frequency
    for a given number of patients over a 14 days time window.

    Parameters:
    ----------------------------------
    start: datetime.date.
        Start date of the time series.
    
    num: int.
        Number of patients.
    
    populations: list of str.
        Patients populations.
    
    seed: int.
        Random seed.
    
    Returns:
    ----------------------------------
    df: pd.DataFrame.
        Data frame with patients blood glucose time series observed at 5 minutes frequency.
        The data frame contains the following columns:
        - 'patient_id': Patient id.
        - 'patient_name': Patient name.
        - 'population': Patient population.
        - 'ts': Timestamp.
        - 'bg': Patient blood glucose level.
        - 'most_recent_week': 1 if the timestamp is within the last 7 days, 0 otherwise.
    '''
    
    # Set the random seed.
    np.random.seed(seed)
    
    # Define the number of timestamps.
    T = 14 * 24 * 60 // 5
    
    # Generate the timestamps.
    ts = pd.date_range(start=start, periods=T, freq='5T')
    
    # Initialize a data frame for storing the patients time series.
    df = pd.DataFrame(columns=['patient_id', 'patient_name', 'population', 'ts', 'bg', 'most_recent_week'])
    
    # Simulate the patients time series.
    for n in range(num):
        
        # Generate the baseline blood glucose level.
        x = pd.Series(
            index=ts,
            data=simulate_baseline(avg=np.random.uniform(low=70, high=180), nsample=T),
            name='bg',
            dtype=np.float64
        )
    
        for d in x.index.to_series().dt.day.unique():
            
            # Add the upward spikes.
            times, values = simulate_upward_spikes()
            x[(x.index.to_series().dt.day == d) & (x.index.to_series().dt.time.isin(times))] = values
    
            # Add the downward spikes.
            times, values = simulate_downward_spikes()
            x[(x.index.to_series().dt.day == d) & (x.index.to_series().dt.time.isin(times))] = values
        
            # Smooth the spikes.
            x[(x.index.to_series().dt.day == d)] = gaussian_filter1d(input=x[(x.index.to_series().dt.day == d)], sigma=3.0)
            
        # Add some missing values.
        x = add_missing_values(x)
        
        # Add the patient time series to the data frame.
        df = df.append(
            pd.DataFrame({
                'patient_id': 1 + n,
                'patient_name': ''.join(np.random.choice(a=[s for s in string.ascii_uppercase], size=2)),
                'population': np.random.choice(a=populations),
                'ts': x.index,
                'bg': x.values,
                'most_recent_week': np.where(x.index.max() - x.index < pd.Timedelta(days=7), 1, 0)
            })
        )
    
    # Set some patients time series to missing.
    df.loc[df['patient_id'].isin(np.random.choice(a=df['patient_id'].unique(), size=2)), 'bg'] = np.nan

    # Shift some patients time series upward.
    df.loc[(df['patient_id'].isin(np.random.choice(a=df['patient_id'].unique(), size=2))) & (df['most_recent_week'] == 1), 'bg'] += 25

    # Shift some patients time series downward.
    df.loc[(df['patient_id'].isin(np.random.choice(a=df['patient_id'].unique(), size=2))) & (df['most_recent_week'] == 1), 'bg'] -= 25

    return df


def simulate_baseline(avg, nsample):
    '''
    Simulate the baseline blood glucose level.
    '''
    return avg + sm.tsa.arma_generate_sample(
        ar=np.r_[1, - np.array([.75, -.25])],
        ma=np.r_[1, np.array([.65, .35])],
        scale=10.,
        nsample=nsample
    )


def simulate_upward_spikes():
    '''
    Simulate upward spikes in the blood glucose level.
    '''
    times, values = list(), list()
    
    # breakfast
    times.append(
        datetime.time(
            hour=np.random.choice(a=[6, 7, 8]),
            minute=np.random.choice(a=np.arange(5, 60, 5))
        )
    )
    values.append(
        np.random.uniform(low=200, high=400)
    )
    
    # lunch
    times.append(
        datetime.time(
            hour=np.random.choice(a=[12, 13, 14]),
            minute=np.random.choice(a=np.arange(5, 60, 5))
        )
    )
    values.append(
        np.random.uniform(low=200, high=400)
    )
    
    # dinner
    times.append(
        datetime.time(
            hour=np.random.choice(a=[18, 19, 20]),
            minute=np.random.choice(a=np.arange(5, 60, 5))
        )
    )
    values.append(
        np.random.uniform(low=200, high=400)
    )
    
    return times, values


def simulate_downward_spikes():
    '''
    Simulate downward spikes in the blood glucose level.
    '''
    times, values = list(), list()
    
    # morning
    times.append(
        datetime.time(
            hour=np.random.choice(a=[9, 10, 11]),
            minute=np.random.choice(a=np.arange(5, 60, 5))
        )
    )
    values.append(
        np.random.uniform(low=40, high=70)
    )
    
    # afternoon
    times.append(
        datetime.time(
            hour=np.random.choice(a=[15, 16, 17]),
            minute=np.random.choice(a=np.arange(5, 60, 5))
        )
    )
    values.append(
        np.random.uniform(low=40, high=70)
    )
    
    return times, values


def add_missing_values(x):
    '''
    Simulate missing values in the blood glucose measurements.
    '''
    # Simulate the start times of the missing sequences.
    times = np.random.choice(a=x.index, size=np.random.randint(low=0, high=20))
    
    # Loop across the missing sequences.
    for i in range(len(times)):
        
        # Simulate the duration of the missing sequence.
        duration = pd.Timedelta(minutes=np.random.randint(low=1, high=2 * 24 * 60 // 5))
        
        # Add the missing sequence to the time series.
        x[(x.index >= times[i]) & (x.index <= times[i] + duration)] = np.nan
    
    return x