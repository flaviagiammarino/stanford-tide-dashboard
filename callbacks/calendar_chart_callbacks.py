import pandas as pd

from visualizations.calendar_chart import calendar_chart
from visualizations.empty_chart import empty_chart

def update_calendar_chart(data):
    
    '''
    Update the calendar chart.

    Parameters:
    ----------------------------------
    df: pd.DataFrame.
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
    data['hour_num'] = data['ts'].dt.hour
    data['hour_str'] = data['ts'].apply(lambda x: x.strftime(format('%I %p')))

    # Get the last 21 days.
    end_date = (data['ts'].max() + pd.offsets.Week(weekday=6)).replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = (end_date - pd.Timedelta(days=20)).replace(hour=0, minute=0, second=0, microsecond=0)
    days = pd.date_range(start=start_date, end=end_date, freq='D')

    # Calculate the hourly medians over the last 14 days.
    data = data.groupby(by=['most_recent_week', 'day', 'hour_str', 'hour_num'])['bg'].median().reset_index()
    data = data.sort_values(by=['most_recent_week', 'day', 'hour_num'], ascending=[True, True, True])
    data = data.drop(labels=['hour_num'], axis=1).rename(columns={'hour_str': 'hour'})

    # Generate the line charts of the hourly medians for each of the last 21 days. Note that an empty chart
    # is returned for the additional 7 days displayed in the calendar.
    outputs = []
    for day in days.day:
        data_ = data[data['day'] == day]
        if data_.shape[0] > 1:
            outputs.append(calendar_chart(data_))
        else:
            outputs.append(empty_chart)

    return outputs
