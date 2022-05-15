import datetime
import pandas as pd
import numpy as np

from utils.simulate_patients import simulate_patients
from utils.rank_patients import rank_patients

# Simulate the patients.
df = simulate_patients(start=datetime.date.today() - datetime.timedelta(days=14), num=50, populations=['4T', 'TIPs', 'Pilot', 'Pilot Cont'])

# Deduplicate the patients names.
names = df[['patient_id', 'patient_name']].drop_duplicates().reset_index(drop=True)
names['patient_name'] += names.groupby(['patient_name']).cumcount().astype(str).replace('0', '')
df = pd.merge(left=df.drop(labels=['patient_name'], axis=1), right=names, on='patient_id')

# Rank the patients.
df = rank_patients(df)

# Add the filters.
df['Filter TW < 75%'] = np.where(df['time_worn (%)'] < 0.75, 'Yes', 'No')
df['Filter TIR < 65%'] = np.where(df['in_range (%)'] < 0.65, 'Yes', 'No')
df['Filter TB 70 > 4%'] = np.where(df['hypo (%)'] > 0.04, 'Yes', 'No')
df['Filter TB 54 > 1%'] = np.where(df['extreme_hypo (%)'] > 0.01, 'Yes', 'No')

# Add the indicators.
df['% Time Below 54'] = np.where(df['bg'] < 54, 1.0, 0.0)
df['% Time Below 70'] = np.where((df['bg'] >= 54) & (df['bg'] < 70), 1.0, 0.0)
df['% Time in Range'] = np.where((df['bg'] >= 70) & (df['bg'] <= 180), 1.0, 0.0)
df['% Time Above 180'] = np.where((df['bg'] >= 180) & (df['bg'] <= 250), 1.0, 0.0)
df['% Time Above 250'] = np.where(df['bg'] > 250, 1.0, 0.0)

# Break down the timestamps.
df['day'] = df['ts'].dt.day
df['month'] = df['ts'].dt.month
df['year'] = df['ts'].dt.year
df['hour'] = df['ts'].dt.hour
df['minute'] = df['ts'].dt.minute
df['day_'] = df['ts'].dt.day_name()
df['month_'] = df['ts'].dt.month_name()
df['hour_'] = df['ts'].apply(lambda x: x.strftime(format('%I %p')))

# Export the results.
df.to_csv('data/sample_data.csv', index=None)
