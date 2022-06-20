import string
import itertools
import pandas as pd
import numpy as np

def simulate_patient_names(num):
    '''
    Simulate the patients' names.

    Parameters:
    ----------------------------------
    num: int.
        Number of patients.

    Returns:
    ----------------------------------
    names: list of str.
        Simulated patients' names.
    '''
    
    names = []
    for s in itertools.product(string.ascii_uppercase, repeat=np.argmax(26 ** np.arange(10) >= num)):
        names.append(''.join(s))
        if len(names) == num:
            break
    
    np.random.shuffle(names)
    
    return names


def simulate_populations(num, populations):
    '''
    Simulate the patients' populations.

    Parameters:
    ----------------------------------
    num: int.
        Number of patients.
    
    populations: list of str.
        Patients' populations.

    Returns:
    ----------------------------------
    pd.DataFrame.
        Simulated patients' populations.
        Data frame with the following columns:
        
        'id': int.
            Patient id.
        
        'name': str.
            Patient name.
        
        'population': str.
            Patient population.
    '''
    
    return pd.DataFrame({
        'id': np.arange(num),
        'name': simulate_patient_names(num),
        'population': np.random.choice(a=populations, size=num),
    })
