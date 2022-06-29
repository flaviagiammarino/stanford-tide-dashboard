import plotly.graph_objects as go

def calendar_chart(data):
    '''
    Generate the calendar chart.

    Parameters:
    ----------------------------------
    data: pd.DataFrame.
       Data frame with blood glucose level hourly medians on a given day out of the last 14 days.

    Returns:
    ----------------------------------
    go.Figure.
        Figure object.
    '''
    
    # Define the figure layout.
    layout = dict(
        title=dict(
            text=data['day'].astype(str).iloc[0],
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
    traces = []

    # Add the lower bound of the target range.
    traces.append(
        go.Scatter(
            x=data['hour'],
            y=[70] * data.shape[0],
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
    traces.append(
        go.Scatter(
            x=data['hour'],
            y=[180] * data.shape[0],
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
    traces.append(
        go.Scatter(
            x=data['hour'],
            y=data['bg'],
            text=data['day'],
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

    return go.Figure(data=traces, layout=layout)
