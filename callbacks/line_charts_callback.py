import dash
import pandas as pd
import datetime

from plots.placeholder_chart import placeholder_chart
from plots.line_chart import line_chart
from plots.timeline_chart import timeline_chart

def calculate_statistics(df):
    '''
    Calculate the descriptive statistics displayed in the table.

    Parameters:
    ----------------------------------
    df: pd.DataFrame.
        Input data frame containing either all patients or a single selected patient.

    Returns:
    ----------------------------------
    avg: str.
        Average glucose level.

    avg_below_54: str.
        Average percentage time of glucose level below 54.

    avg_below_70: str.
        Average percentage time of glucose level below 70.

    avg_in_range: str.
        Average percentage time of glucose level in range 70 - 180.

    avg_above_180: str.
       Average percentage time of glucose level above 180.

    avg_above_250: str.
        Average percentage time of glucose level above 250.

    cv: str.
        Coefficient of variation of glucose level.

    std: str.
        Standard deviation of glucose level.

    avg_worn: str.
        Average percentage time that the device has been worn.
    '''
    # Copy the data frame.
    df = df.copy()

    # Extract the data for the most recent week.
    df = df[df['most_recent_week'] == 1]

    # Calculate the average.
    avg = format(df['bg'].mean(), '.2f')

    # Calculate the average time below 54.
    avg_below_54 = format(df['% Time Below 54'].mean(), '.1%')

    # Calculate the average time below 70.
    avg_below_70 = format(df['% Time Below 70'].mean(), '.1%')

    # Calculate the average time in range.
    avg_in_range = format(df['% Time in Range'].mean(), '.1%')

    # Calculate the average time above 180.
    avg_above_180 = format(df['% Time Above 180'].mean(), '.1%')

    # Calculate the average time above 250.
    avg_above_250 = format(df['% Time Above 250'].mean(), '.1%')

    # Calculate the coefficient of variation.
    cv = format(df['bg'].std() / df['bg'].mean(), '.1%')

    # Calculate the sample standard deviation.
    std = format(df['bg'].std(), '.1f')

    # Calculate the average time worn.
    avg_worn = format(df['time_worn (%)'].mean(), '.1%')

    return [avg, avg_below_54, avg_below_70, avg_in_range, avg_above_180, avg_above_250, cv, std, avg_worn]


def update_timeline(data):
    '''
    Generate the line charts of the median by day and hour.

    Parameters:
    ----------------------------------
    df: pd.DataFrame.
        Input data frame containing either all patients or a single selected patient.

    Returns:
    ----------------------------------
    figures: list.
        List of 21 figure dictionaries, one for each day in the last 3 weeks.
    '''
    # Copy the data frame.
    data = data.copy()

    # Format the timestamps.
    data['ts'] = pd.to_datetime(data['ts'])

    # Extract the last 21 days.
    end_date = (datetime.datetime.now() + pd.offsets.Week(weekday=6)).replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = (end_date - datetime.timedelta(days=20)).replace(hour=0, minute=0, second=0, microsecond=0)
    days = pd.date_range(start=start_date, end=end_date, freq='D').day

    # Calculate the hourly medians.
    df = data.groupby(by=['most_recent_week', 'day_', 'day', 'hour_', 'hour'])['bg'].median().reset_index()
    df = df.sort_values(by=['most_recent_week', 'day', 'hour'], ascending=[True, True, True])
    df = df.drop(labels='hour', axis=1).rename(columns={'hour_': 'hour'})

    # Plot the hourly medians for each of the last 21 days.
    figures = []
    for day in days:
        fig_data = df[df['day'] == day]
        if fig_data.shape[0] > 1:
            figures.append(timeline_chart(fig_data))
        else:
            figures.append(placeholder_chart)

    return figures


def update_line_charts(data, population, time_worn_less_than_75, time_in_range_less_than_65, time_below_70_greater_than_4,
time_below_54_greater_than_1, click_data):
    '''
    Update the table and all the line charts.

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

    Returns:
    ----------------------------------
    A list containing the following items:
    - The title of the table.
    - The data displayed in the table.
    - The title of the figure with the line chart of the percentiles by hour.
    - The figure with the line chart of the percentiles by hour.
    - The 21 figures with the line chart of the median by hour for each day in the last 3 weeks.
    '''
    # Find out which input has changed.
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    # If the filters have changed, reset the table using all patients.
    if 'bar-chart.clickData' not in changed_id:

        # Update the title of the table.
        table_title = ['CGM Data in Past 2 Weeks for Patient: All']

        # Update the data in the table.
        table_data = calculate_statistics(data)

        # Update the title of the large line chart with the percentiles.
        large_figure_title = ['Glucose Levels for Patient: All']

        # Update the large line chart with the percentiles.
        large_figure = [line_chart(data)]

        # Update the small line charts with the median.
        small_figures = update_timeline(data)

        return table_title + table_data + large_figure_title + large_figure + small_figures

    # If the selected patient has changed, update the table using only this patient.
    elif 'bar-chart.clickData' in changed_id:

        # Extract the id of the selected patient.
        patient_id = click_data['points'][0]['customdata']

        # Extract the data of the selected patient.
        df_ = data[data['patient_id'] == patient_id].reset_index(drop=True)

        # Extract the name of the selected patient.
        patient_name = df_['patient_name'].unique()[0]

        # Update the title of the table.
        table_title = ['CGM Data in Past 2 Weeks for Patient: ' + patient_name]

        # Update the data in the table.
        table_data = calculate_statistics(df_)

        # Update the title of the large line chart with the percentiles.
        large_figure_title = ['Glucose Levels for Patient: ' + patient_name]

        # Update the large line chart with the percentiles.
        large_figure = [line_chart(df_)]

        # Update the small line charts with the median.
        small_figures = update_timeline(df_)

        return table_title + table_data + large_figure_title + large_figure + small_figures

    else:
        raise dash.exceptions.PreventUpdate
