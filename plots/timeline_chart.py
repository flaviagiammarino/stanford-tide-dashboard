import plotly.graph_objects as go

def timeline_chart(df):
    '''
    Generate the line charts of the median by day and hour.
    
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
    # Define the figure layout.
    layout = dict(
        title=dict(
            text=df['day'].astype(str).values[0],
            font=dict(
                family='Arial Black'
            ),
            x=0.5
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        showlegend=False,
        margin=dict(t=25, r=5, b=15, l=5, pad=0),
        font=dict(
            family='Arial',
            size=6,
            color='#55514b'
        ),
        xaxis=dict(
            fixedrange=True,
            type='category',
            tickangle=-45,
            tickfont=dict(
                family='Arial',
                size=6,
                color='#55514b'
            ),
            nticks=6,
            color='#55514b',
            linecolor='#aca899',
            showgrid=False,
            zeroline=False,
            mirror=True,
        ),
        yaxis=dict(
            range=[0, 400],
            fixedrange=True,
            showticklabels=False,
            linecolor='#aca899',
            mirror=True,
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

    # Add the median.
    data.append(
        go.Scatter(
            x=df['hour'],
            y=df['bg'],
            text=df['day'],
            mode='lines',
            name='50% - Median',
            showlegend=True,
            line=dict(
                color='#FF7F0E',
                width=1.5
            ),
            hoverlabel=hoverlabel,
            hovertemplate='<b>Day: </b>%{text}<br><b>Hour: </b>%{x}<br><b>50% - Median: </b>%{y: ,.2f}<extra></extra>'
        )
    )

    return go.Figure(data=data, layout=layout)
