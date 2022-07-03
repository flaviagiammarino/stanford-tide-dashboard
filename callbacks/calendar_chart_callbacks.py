import pandas as pd

from visualizations.calendar_chart import calendar_chart
from visualizations.empty_chart import empty_chart

def update_calendar_chart(data):
    '''
    Update the calendar chart.

    Parameters:
    ----------------------------------
    data: pd.DataFrame.
       Patients' dataset.

    Returns:
    ----------------------------------
    outputs: list.
        List of 21 figure objects, one for each day in the last 3 weeks.
    '''

    # Copy the data.
    data = data.copy()

    # Extract the days and hours from the timestamps.
    data['day'] = data['ts'].dt.day
    data['hour'] = data['ts'].dt.hour

    # Get the last 21 days.
    end_date = data['ts'].max().date() + pd.offsets.Week(weekday=6)
    start_date = end_date - pd.offsets.Day(n=20)
    days = pd.date_range(start=start_date, end=end_date, freq='D')

    # Calculate the hourly medians over the last 14 days.
    data = data.groupby(by=['most_recent_week', 'day', 'hour'])['bg'].median().reset_index()
    data = data.sort_values(by=['most_recent_week', 'day', 'hour'], ascending=[True, True, True])
    data['hour'] = pd.to_datetime(data['hour'], format='%H').dt.strftime('%I %p')
    
    # Update the line charts of the hourly medians for each of the last 21 days,
    # skip the additional 7 days displayed in the calendar.
    outputs = []
    for day in days.day:
        data_ = data[data['day'] == day]
        if data_.shape[0] > 1:
            outputs.append(calendar_chart(data_))
        else:
            outputs.append(empty_chart)

    return outputs
