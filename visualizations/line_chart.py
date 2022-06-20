import plotly.graph_objects as go

def line_chart(data):
    '''
    Generate the line chart.
    
    Parameters:
    ----------------------------------
    data: pd.DataFrame.
        Data frame with blood glucose level hourly percentiles over the last 14 days.

    Returns:
    ----------------------------------
    go.Figure.
        Figure object.
    '''
 
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

    # Add the 10th percentile.
    traces.append(
        go.Scatter(
            x=data['hour'],
            y=data['10%'],
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
    traces.append(
        go.Scatter(
            x=data['hour'],
            y=data['25% - IQR'],
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
    traces.append(
        go.Scatter(
            x=data['hour'],
            y=data['50% - Median'],
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
    traces.append(
        go.Scatter(
            x=data['hour'],
            y=data['75% - IQR'],
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
    traces.append(
        go.Scatter(
            x=data['hour'],
            y=data['90%'],
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

    return go.Figure(data=traces, layout=layout)
