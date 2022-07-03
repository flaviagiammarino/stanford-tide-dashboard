import pandas as pd

from algorithm.rank_patients import preprocess_data
from simulations.simulate_patients import simulate_patients
from simulations.simulate_populations import simulate_populations

def load_sample_data():
    
    # Load the patients' dataset.
    patients = pd.read_csv('data/patients.csv', parse_dates=['ts'])
    
    # Preprocess the patients' dataset.
    patients = preprocess_data(patients)

    # Load the patients' populations.
    populations = pd.read_csv('data/populations.csv')
    
    # Add the patient's populations to the patients' dataset.
    df = populations.set_index('id').join(patients.set_index('id'))
    
    return df.reset_index(drop=False)


def generate_random_data(num=50, freq=5, populations=['4T', 'Pilot', 'Pilot Cont', 'TIPs']):
    
    # Generate the patients' dataset.
    patients = simulate_patients(freq, num)
    
    # Preprocess the patients' dataset.
    patients = preprocess_data(patients)
    
    # Generate the patients' populations.
    populations = simulate_populations(num, populations)
    
    # Add the patient's populations to the patients' dataset.
    df = populations.set_index('id').join(patients.set_index('id'))
    
    return df.reset_index(drop=False)
