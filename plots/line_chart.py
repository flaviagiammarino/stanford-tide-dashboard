import pandas as pd
import numpy as np
import plotly.graph_objects as go

def line_chart(df):
    '''
    Generate the line charts of the percentiles by hour.

    Parameters:
    ----------------------------------
    df: pd.DataFrame.
        Data frame with patients blood glucose time series observed at 5 minutes frequency
        including patients ranks and patients priority groups.
        The data frame contains the following columns:
        - 'patient_id': Patient id.
        - 'patient_name': Patient name.
        - 'population': Patient population.
        - 'ts': Timestamp.
        - 'bg': Patient blood glucose level.
        - 'most_recent_week': 1 if the timestamp is within the last 7 days, 0 otherwise.
        - 'patient_rank': Patient rank.
        - 'review':  Patient priority group.
        - 'time_worn (%)': Percentage of time that the patient has worn the device over a given week.
        - 'in_range': 1 of the patient blood glucose level is between 70 and 180, 0 otherwise.
        - 'in_range (%)': Percentage of time that the patient blood glucose level has been between 70 and 180 over a given week.
        - 'hypo': 1 of the patient blood glucose level is between 54 and 70, 0 otherwise.
        - 'hypo (%)': Percentage of time that the patient blood glucose level has been between 54 and 70 over a given week.
        - 'extreme_hypo': 1 of the patient blood glucose level is less than 54, 0 otherwise.
        - 'extreme_hypo (%)': Percentage of time that the patient blood glucose level has been below 54 over a given week.

    Returns:
    ----------------------------------
    go.Figure.
    '''
    # Copy the data frame.
    df = df.copy()

    # Format the timestamps.
    df['ts'] = pd.to_datetime(df['ts'])

    # Extract the data for the most recent week.
    df = df[df['most_recent_week'] == 1]

    # Calculate the percentiles by hour.
    def q90(x): return x.quantile(0.90)
    def q75(x): return x.quantile(0.75)
    def q50(x): return x.quantile(0.50)
    def q25(x): return x.quantile(0.25)
    def q10(x): return x.quantile(0.10)

    df = df.groupby(by=['hour_']).agg({'bg': [q90, q75, q50, q25, q10], 'hour': [np.max]}).reset_index()
    df.columns = ['hour_', '90%', '75% - IQR', '50% - Median', '25% - IQR', '10%', 'hour']
    df = df.sort_values(by='hour').drop(labels='hour', axis=1).rename(columns={'hour_': 'hour'})

    # Define the figure layout.
    layout = dict(
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(x=0, y=1, orientation='h'),
        margin=dict(t=5, r=5, b=5, l=5, pad=0),
        font=dict(
            family='Arial',
            size=9,
            color='#55514b'
        ),
        xaxis=dict(
            fixedrange=True,
            type='category',
            tickangle=0,
            tickfont=dict(
                family='Arial Black',
                size=8,
                color='#55514b'
            ),
            color='#55514b',
            linecolor='#aca899',
            showgrid=False,
            zeroline=False,
            mirror=True,
        ),
        yaxis=dict(
            range=[0, 400],
            fixedrange=True,
            color='#55514b',
            linecolor='#aca899',
            showgrid=False,
            zeroline=False,
            mirror=True,
            tickangle=0,
            tickfont=dict(
                family='Arial',
                size=10,
                color='#55514b'
            ),
            title=dict(
                text='Glucose Levels (mg/dL)',
                font=dict(
                    family='Arial',
                    size=10,
                    color='#55514b'
                ),
            ),
        ),
    )

    # Define the tooltip layout.
    hoverlabel = dict(
        bgcolor='white',
        bordercolor='#aca899',
        font=dict(
            family='Arial',
            size=10,
            color='#55514b'
        )
    )

    # Add the data to the figure.
    data = []

    # Add the lower bound of the target range.
    data.append(
        go.Scatter(
            x=df['hour'],
            y=[70] * df.shape[0],
            mode='lines',
            showlegend=False,
            line=dict(
                color='rgba(207, 207, 207, 0.8)',
                width=0
            ),
            hoverlabel=hoverlabel,
            hovertemplate='70<extra></extra>'
        )
    )

    # Add the upper bound of the target range.
    data.append(
        go.Scatter(
            x=df['hour'],
            y=[180] * df.shape[0],
            mode='lines',
            showlegend=False,
            line=dict(
                color='rgba(207, 207, 207, 0.8)',
                width=0
            ),
            fill='tonexty',
            fillcolor='rgba(207, 207, 207, 0.8)',
            hoverlabel=hoverlabel,
            hovertemplate='180<extra></extra>'
        )
    )

    # Add the 10th percentile.
    data.append(
        go.Scatter(
            x=df['hour'],
            y=df['10%'],
            mode='lines',
            name='10%',
            showlegend=True,
            line=dict(
                color='#2CA02C',
                width=1.5
            ),
            hoverlabel=hoverlabel,
            hovertemplate='<b>Hour: </b>%{x}<br><b>10%: </b>%{y: ,.2f}<extra></extra>'
        )
    )

    # Add the 25th percentile.
    data.append(
        go.Scatter(
            x=df['hour'],
            y=df['25% - IQR'],
            mode='lines',
            name='25% - IQR',
            showlegend=True,
            line=dict(
                color='#1F77B4',
                width=1.5
            ),
            hoverlabel=hoverlabel,
            hovertemplate='<b>Hour: </b>%{x}<br><b>25% - IQR: </b>%{y: ,.2f}<extra></extra>'
        )
    )

    # Add the 50th percentile.
    data.append(
        go.Scatter(
            x=df['hour'],
            y=df['50% - Median'],
            mode='lines',
            name='50% - Median',
            showlegend=True,
            line=dict(
                color='#FF7F0E',
                width=1.5
            ),
            hoverlabel=hoverlabel,
            hovertemplate='<b>Hour: </b>%{x}<br><b>50% - Median: </b>%{y: ,.2f}<extra></extra>'
        )
    )

    # Add the 75th percentile.
    data.append(
        go.Scatter(
            x=df['hour'],
            y=df['75% - IQR'],
            mode='lines',
            name='75% - IQR',
            showlegend=True,
            line=dict(
                color='#1F77B4',
                width=1.5
            ),
            hoverlabel=hoverlabel,
            hovertemplate='<b>Hour: </b>%{x}<br><b>75% - IQR: </b>%{y: ,.2f}<extra></extra>'
        )
    )

    # Add the 90th percentile.
    data.append(
        go.Scatter(
            x=df['hour'],
            y=df['90%'],
            mode='lines',
            name='90%',
            showlegend=True,
            line=dict(
                color='#2CA02C',
                width=1.5
            ),
            hoverlabel=hoverlabel,
            hovertemplate='<b>Hour: </b>%{x}<br><b>90%: </b>%{y: ,.2f}<extra></extra>'
        )
    )

    return go.Figure(data=data, layout=layout)
