import dash

from plots.bar_chart import bar_chart
from plots.placeholder_chart import placeholder_chart

def update_bar_chart(data, population, time_worn_less_than_75, time_in_range_less_than_65, time_below_70_greater_than_4,
time_below_54_greater_than_1, click_data, figure, style):
    '''
    Update the figure with the horizontal bar charts.

    Parameters:
    ----------------------------------
    data: pd.DataFrame.
        Raw unfiltered data frame.

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

    Returns:
    ----------------------------------
    figure: dict.
        Bar chart figure dictionary.

    style: dict.
        Bar chart style dictionary.
    '''
    # Find out which input has changed.
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    # If the filters have changed, draw a new bar chart.
    if 'bar-chart.clickData' not in changed_id:

        # Filter the data frame
        df = data.copy()

        if population is not None and population != []:
            df = df[df['population'].isin(population)]

        if time_worn_less_than_75 is not None and time_worn_less_than_75 != []:
            df = df[df['Filter TW < 75%'].isin(time_worn_less_than_75)]

        if time_in_range_less_than_65 is not None and time_in_range_less_than_65 != []:
            df = df[df['Filter TIR < 65%'].isin(time_in_range_less_than_65)]

        if time_below_70_greater_than_4 is not None and time_below_70_greater_than_4 != []:
            df = df[df['Filter TB 70 > 4%'].isin(time_below_70_greater_than_4)]

        if time_below_54_greater_than_1 is not None and time_below_54_greater_than_1 != []:
            df = df[df['Filter TB 54 > 1%'].isin(time_below_54_greater_than_1)]

        # If the filtered data frame is not empty, return the bar chart.
        if df.shape[0] > 0:

            # Draw the bar chart.
            figure = bar_chart(df)

            # Update the height of the figure.
            n = df['patient_name'].nunique()
            style['height'] = 'calc(' + str(0.75 * n) + 'vw' + ' + ' + str(0.75 * n) + 'vh)'

        # If the filtered data frame is empty, return an empty chart.
        else:
    
            # Draw the empty chart.
            figure = placeholder_chart

            # Update the height of the figure.
            style['height'] = '100%'

        return figure, style

    # If the selected patient has changed, update the existing bar chart.
    elif 'bar-chart.clickData' in changed_id:

        # Extract the id of the selected patient.
        patient_id = click_data['points'][0]['customdata']

        # Highlight the row of the bar chart corresponding to the selected patient.
        for i in range(len(figure['data'])):

            # Extract the row index of the selected patient.
            idx = list(figure['data'][i]['customdata']).index(patient_id)

            # Extract the current colors.
            col = list(figure['data'][i]['marker']['color'])

            # Decrease the transparency for the selected patient, and increase the transparency for the other patients.
            figure['data'][i]['marker']['color'] = [col[j].replace('0.9', '0.45') if j != idx else col[j].replace('0.45', '0.9') for j in range(len(col))]

        return figure, style

    else:
        raise dash.exceptions.PreventUpdate
