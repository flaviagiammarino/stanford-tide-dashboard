import datetime
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.ndimage import gaussian_filter1d
from joblib import Parallel, delayed
from tqdm import tqdm

def simulate_patient(id, freq):
    '''
    Simulate a single patient's blood glucose level time series.

    Parameters:
    ----------------------------------
    id: int.
        Patient id.
    
    freq: int.
        Frequency of the time series (in minutes).
    
    Returns:
    ----------------------------------
    pd.DataFrame.
        Simulated blood glucose level time series for a single patient.
        Data frame with the following columns:
        
        'id': int.
            Patient id.
        
        'ts': pd.datetime.
            Timestamp.
        
        'bg': float.
            Blood glucose level.
    '''
    
    # Generate the timestamps.
    ts = pd.date_range(
        start=pd.Timestamp(datetime.date.today()) - pd.Timedelta(days=14),
        end=pd.Timestamp(datetime.date.today()) - pd.Timedelta(minutes=freq),
        freq=f'{freq}T'
    )
    
    # Generate the baseline blood glucose level.
    bg = np.random.uniform(low=70, high=180)
    bg += sm.tsa.arma_generate_sample(
        ar=np.r_[1, - np.array([.75, -.25])],
        ma=np.r_[1, np.array([.65, .35])],
        scale=10.,
        nsample=len(ts)
    )
    
    def simulate_timestamps(hours):
        '''
        Generate random timestamps within certain hours on each of the 14 days.
        
        Parameters:
        ----------------------------------
        hours: list of int.
            Hours within which the timestamps should fall.
        
        Returns:
        ----------------------------------
        list of datetime.datetime.
            Generated timestamps, list of 14 datetime.datetime objects.
        '''
        
        fn = lambda date: datetime.datetime.combine(
            date=date,
            time=datetime.time(
                hour=np.random.choice(a=hours),
                minute=np.random.choice(a=np.arange(start=freq, stop=60, step=freq))
            )
        )
        return [fn(date) for date in ts.to_series().dt.date.unique()]

    # Add some upward spikes around mealtimes.
    bg[ts.to_series().isin(simulate_timestamps(hours=[6, 7, 8]))] = np.random.uniform(low=180, high=400, size=14)
    bg[ts.to_series().isin(simulate_timestamps(hours=[12, 13, 14]))] = np.random.uniform(low=180, high=400, size=14)
    bg[ts.to_series().isin(simulate_timestamps(hours=[18, 19, 20]))] = np.random.uniform(low=180, high=400, size=14)
    
    # Add some downward spikes after mealtimes.
    bg[ts.to_series().isin(simulate_timestamps(hours=[9, 10, 11]))] = np.random.uniform(low=20, high=70, size=14)
    bg[ts.to_series().isin(simulate_timestamps(hours=[15, 16, 17]))] = np.random.uniform(low=20, high=70, size=14)
    bg[ts.to_series().isin(simulate_timestamps(hours=[21, 22, 23]))] = np.random.uniform(low=20, high=70, size=14)
    
    # Add an upward or downward shift over the most recent week.
    bg[ts.max() - ts < pd.Timedelta(days=7)] += np.random.normal(loc=0, scale=10, size=1)

    # Smooth the spikes and shifts.
    bg = gaussian_filter1d(input=bg, sigma=3)
    
    # Add a missing sub-sequence.
    start, end = list(np.sort(np.random.randint(low=0, high=len(ts), size=2)))
    bg[start: end] = np.nan
    
    return pd.DataFrame({'id': id, 'ts': ts, 'bg': bg})


def simulate_patients(freq, num, distributed=True):
    '''
    Simulate multiple patients' blood glucose level time series.

    Parameters:
    ----------------------------------
    freq: int.
        Frequency of the time series (in minutes).
    
    num: int.
        Number of time series (i.e. number of patients).
    
    distributed: bool.
        Whether to parallelize the simulations or not.

    Returns:
    ----------------------------------
    pd.DataFrame.
        Simulated blood glucose level time series for multiple patients.
        Data frame with the following columns:
        
        'id': int.
            Patient id.
            
        'ts': pd.datetime.
            Timestamp.
            
        'bg': float.
            Blood glucose level.
    '''
    
    if distributed:
        return pd.concat(Parallel(n_jobs=-1)(delayed(lambda id: simulate_patient(id, freq))(id) for id in tqdm(range(num))))
    
    else:
        return pd.concat([simulate_patient(id, freq) for id in tqdm(range(num))], axis=0)
