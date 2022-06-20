from visualizations.bar_chart import bar_chart
from visualizations.empty_chart import empty_chart

def update_bar_chart(data,
                     population,
                     time_worn_less_than_75,
                     time_in_range_less_than_65,
                     time_below_70_greater_than_4,
                     time_below_54_greater_than_1,
                     click_data,
                     figure,
                     style,
                     changed_id):
    
    '''
    Update the bar chart.

    Parameters:
    ----------------------------------
    data: pd.DataFrame.
       Patients' dataset.

    population: list.
        Selected options in "population-checklist".

    time_worn_less_than_75: list.
        Selected options in "time-worn-less-than-75-checklist".

    time_in_range_less_than_65: list.
        Selected options in "time-in-range-less-than-65-checklist".

    time_below_70_greater_than_4: list.
        Selected options in "time-below-70-greater-than-4-checklist".

    time_below_54_greater_than_1: list.
        Selected options in "time-below-54-greater-than-1-checklist".

    click_data: dict.
        Bar chart click data.

    figure: dict.
        Bar chart figure dictionary.

    style: dict.
        Bar chart style dictionary.
    
    changed_id: list.
        Inputs that triggered the callback.

    Returns:
    ----------------------------------
    outputs: list.
        The first item is the bar chart figure dictionary, the second item is the bar chart style dictionary.
    '''

    # If the filters have changed, draw a new bar chart.
    if 'bar-chart.clickData' not in changed_id:
        
        # Filter the data.
        data = data[data['most_recent_week'] == 1]
        
        if population is not None:
            data = data[data['population'].isin(population)]

        if time_worn_less_than_75 is not None:
            if time_worn_less_than_75 == ['Yes']:
                data = data[data['time_worn (%)'] < 0.75]
            elif time_worn_less_than_75 == ['No']:
                data = data[data['time_worn (%)'] >= 0.75]

        if time_in_range_less_than_65 is not None:
            if time_in_range_less_than_65 == ['Yes']:
                data = data[data['in_range (%)'] < 0.65]
            elif time_in_range_less_than_65 == ['No']:
                data = data[data['in_range (%)'] >= 0.65]

        if time_below_70_greater_than_4 is not None:
            if time_below_70_greater_than_4 == ['Yes']:
                data = data[data['hypo (%)'] > 0.04]
            elif time_below_70_greater_than_4 == ['No']:
                data = data[data['hypo (%)'] <= 0.04]

        if time_below_54_greater_than_1 is not None:
            if time_below_54_greater_than_1 == ['Yes']:
                data = data[data['extreme_hypo (%)'] > 0.01]
            elif time_below_54_greater_than_1 == ['No']:
                data = data[data['extreme_hypo (%)'] <= 0.01]

        # Average the data.
        data = data.groupby(by=['review', 'rank', 'id', 'name'])[['time_worn', 'bg', 'in_range', 'hypo', 'extreme_hypo']].mean()
        data = data.sort_values(by=['review', 'rank'], ascending=[False, True]).fillna(value=0).reset_index()
        
        # If the data frame is not empty, return the bar chart.
        if not data.empty:
    
            # Draw the bar chart.
            figure = bar_chart(data)
    
            # Update the height of the figure.
            style['height'] = 'calc(' + str(0.75 * data['id'].nunique()) + 'vw' + ' + ' + str(0.75 * data['id'].nunique()) + 'vh)'

        # If the data frame is empty, return an empty chart.
        else:
    
            # Draw an empty chart.
            figure = empty_chart
    
            # Update the height of the figure.
            style['height'] = '100%'

    # If the selected patient has changed, update the existing bar chart.
    else:

        # Extract the id of the selected patient.
        patient_id = click_data['points'][0]['customdata']

        # Highlight the row of the bar chart corresponding to the selected patient.
        for i in range(len(figure['data'])):

            # Extract the row index of the selected patient.
            index = list(figure['data'][i]['customdata']).index(patient_id)

            # Extract the current colors.
            colors = list(figure['data'][i]['marker']['color'])

            # Decrease the transparency for the selected patient, and increase the transparency for the other patients.
            figure['data'][i]['marker']['color'] = [colors[j].replace('0.9', '0.45') if j != index else colors[j].replace('0.45', '0.9') for j in range(len(colors))]
    
    outputs = [figure, style]
    
    return outputs
