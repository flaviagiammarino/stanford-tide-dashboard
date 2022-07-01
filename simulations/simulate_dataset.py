import pandas as pd

from simulations.simulate_patients import simulate_patients
from simulations.simulate_populations import simulate_populations
from algorithm.rank_patients import rank_patients

def simulate_dataset(num, freq, populations):
    '''
    Simulate a patients' dataset.

    Parameters:
    ----------------------------------
    num: int.
        Number of patients.
        
    freq: int.
        Frequency of the patients' blood glucose level time series (in minutes).
    
    populations: list of str.
        Patients' populations.
        
    Returns:
    ----------------------------------
    df: pd.DataFrame.
        Simulated patients' dataset.
        Data frame with the following columns:
        
        'id': int.
            Patient id.
        
        'name': str.
            Patient name.
        
        'population': str.
            Patient population.
            
        'ts': pd.datetime.
            Timestamp.
            
        'bg': float.
            Blood glucose level.
        
        'most_recent_week': float.
            1.0 if the timestamp falls within the most recent week, 0.0 otherwise.
        
        'time_worn': float.
            1.0 if the patient is wearing the device, 0.0 otherwise.
        
        'extreme_hypo': float.
            1.0 if the patient blood glucose level is less than 54, 0.0 otherwise.
        
        'hypo': float.
            1.0 if the patient blood glucose level is between 54 and 70, 0.0 otherwise.
        
        'in_range': float.
            1.0 if the patient blood glucose level is between 70 and 180, 0.0 otherwise.
        
        'hyp': float.
            1.0 if the patient blood glucose level is between 180 and 250, 0.0 otherwise.
        
        'extreme_hyp': float.
            1.0 if the patient blood glucose level is greater than 250, 0.0 otherwise.
            
        'time_worn (%)': float.
            Percentage of time that the patient has worn the device over a given week.
            
        'extreme_hypo (%)': float.
            Percentage of time that the patient blood glucose level has been less than 54 over a given week.

        'hypo (%)': float.
            Percentage of time that the patient blood glucose level has been between 54 and 70 over a given week.
            
        'in_range (%)': float.
            Percentage of time that the patient blood glucose level has been between 70 and 180 over a given week.
         
        'hyp (%)': float.
            Percentage of time that the patient blood glucose level has been between 180 and 250 over a given week.

        'extreme_hyp (%)': float.
            Percentage of time that the patient blood glucose level has been greater than 250 over a given week.
        
        'patient_rank': int.
            Patient rank.
        
        'review': str.
            Patient priority group.
    '''
    
    # Simulate the patients' blood glucose level time series.
    df = simulate_patients(freq=freq, num=num)
    
    # Rank the patients.
    df = rank_patients(df=df)
 
    # Add the simulated patients' populations.
    df = pd.merge(left=simulate_populations(num=num, populations=populations), right=df, on='id')
    
    return df
