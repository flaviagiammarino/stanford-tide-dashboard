from visualizations.line_chart import line_chart

def update_line_chart(data):
    
    '''
    Update the line chart.

    Parameters:
    ----------------------------------
    df: pd.DataFrame.
       Patients' dataset.

    Returns:
    ----------------------------------
    outputs: list.
        The first item is the figure title, the second item is the figure object.
    '''

    # Copy the data.
    data = data.copy()
    
    # Update the title of the figure.
    outputs = ['Glucose Levels for Patient: {}'.format(data['name'].iloc[0] if data['name'].nunique() == 1 else 'All')]
    
    # Extract the hours from the timestamps.
    data['hour_num'] = data['ts'].dt.hour
    data['hour_str'] = data['ts'].apply(lambda x: x.strftime(format('%I %p')))
    
    # Define the percentiles.
    def q90(x): return x.quantile(0.90)
    def q75(x): return x.quantile(0.75)
    def q50(x): return x.quantile(0.50)
    def q25(x): return x.quantile(0.25)
    def q10(x): return x.quantile(0.10)

    # Calculate the hourly percentiles.
    data = data.groupby(by=['hour_str']).agg({'bg': [q90, q75, q50, q25, q10], 'hour_num': 'max'}).reset_index(drop=False)
    data.columns = ['hour_str', '90%', '75% - IQR', '50% - Median', '25% - IQR', '10%', 'hour_num']
    data = data.sort_values(by='hour_num').drop(labels='hour_num', axis=1)
    data = data.rename(columns={'hour_str': 'hour'}).reset_index(drop=True)
    
    # Update the data in the figure.
    outputs.append(line_chart(data))
    
    return outputs
