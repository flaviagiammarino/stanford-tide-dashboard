
def update_table(data):
    '''
    Update the table.

    Parameters:
    ----------------------------------
    data: pd.DataFrame.
       Patients' dataset.

    Returns:
    ----------------------------------
    outputs: list.
        The first item is the title of the table, the remaining items are the descriptive statistics displayed in the table.
    '''
    
    # Update the title of the table.
    outputs = ['CGM Data in Past 2 Weeks for Patient: {}'.format(data['name'].iloc[0] if data['name'].nunique() == 1 else 'All')]
    
    # Update the average.
    outputs.append(format(data['bg'].mean(), '.2f'))

    # Update the average time below 54.
    outputs.append(format(data['extreme_hypo'].mean(), '.1%'))

    # Update the average time below 70.
    outputs.append(format(data['hypo'].mean(), '.1%'))

    # Update the average time in range.
    outputs.append(format(data['in_range'].mean(), '.1%'))

    # Update the average time above 180.
    outputs.append(format(data['hyp'].mean(), '.1%'))

    # Update the average time above 250.
    outputs.append(format(data['extreme_hyp'].mean(), '.1%'))

    # Update the coefficient of variation.
    outputs.append(format(data['bg'].std() / data['bg'].mean(), '.1%'))

    # Update the sample standard deviation.
    outputs.append(format(data['bg'].std(), '.1f'))

    # Update the average time worn.
    outputs.append(format(data['time_worn (%)'].mean(), '.1%'))

    return outputs
