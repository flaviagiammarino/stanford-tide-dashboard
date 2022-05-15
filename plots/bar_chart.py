import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def bar_chart(df):
    '''
    Generate the horizontal bar charts by patient.

    Parameters:
    ----------------------------------
    output: pd.DataFrame.
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
    dict.
    '''
    
    # Copy the data frame.
    df = df.copy()

    # Extract the data for the most recent week.
    df = df[df['most_recent_week'] == 1]

    # Calculate the averages.
    df = df.groupby(by=['review', 'patient_rank', 'patient_id', 'patient_name'])[['time_worn (%)', 'bg', '% Time in Range', '% Time Below 70', '% Time Below 54']].mean()
    df = df.sort_values(by=['review', 'patient_rank'], ascending=[False, True]).fillna(value=0).reset_index()

    # Plot the averages.
    fig = make_subplots(
        rows=1,
        cols=5,
        shared_yaxes=True,
        shared_xaxes=False,
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

    # Define the tooltip text.
    hovertemplate = \
        '<b>% Time Worn: </b>' + df['time_worn (%)'].apply(lambda x: format(x, '.0%')) + '<br>' + \
        '<b>Avg. Glucose (mg/dL): </b>' + df['bg'].apply(lambda x: format(x, '.0f')) + '<br>' + \
        '<b>% Time in Range: </b>' + df['% Time in Range'].apply(lambda x: format(x, '.0%')) + '<br>' + \
        '<b>% Time Below 70: </b>' + df['% Time Below 70'].apply(lambda x: format(x, '.1%')) + '<br>' + \
        '<b>% Time Below 54: </b>' + df['% Time Below 54'].apply(lambda x: format(x, '.1%')) + '<extra></extra>'

    # Define the colorscale.
    blue = 'rgba(31, 119, 180, 0.9)'
    red = 'rgba(214, 39, 40, 0.9)'

    # Add the first bar chart in the first column.
    fig.add_trace(
        trace=go.Bar(
            y=[df['review'], df['patient_name']],
            x=df['time_worn (%)'],
            customdata=df['patient_id'],
            text=df['time_worn (%)'].apply(lambda x: format(x, '.0%')),
            textposition='outside',
            textfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            orientation='h',
            marker=dict(
                color=np.where(df['time_worn (%)'] < 0.75, red, blue),
                line=dict(width=0)
            ),
            width=0.8,
            hovertemplate=hovertemplate,
            hoverlabel=hoverlabel,
        ),
        row=1,
        col=1
    )

    # Add the second bar chart in the second column.
    fig.add_trace(
        trace=go.Bar(
            y=[df['review'], df['patient_name']],
            x=df['bg'],
            customdata=df['patient_id'],
            text=df['bg'].apply(lambda x: format(x, ',.0f')),
            textposition='outside',
            textfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            orientation='h',
            marker=dict(
                color=np.where(df['bg'] < 54, red, blue),
                line=dict(width=0)
            ),
            width=0.8,
            hovertemplate=hovertemplate,
            hoverlabel=hoverlabel,
        ),
        row=1,
        col=2
    )

    # Add the third bar chart in the third column.
    fig.add_trace(
        trace=go.Bar(
            y=[df['review'], df['patient_name']],
            x=df['% Time in Range'],
            customdata=df['patient_id'],
            text=df['% Time in Range'].apply(lambda x: format(x, '.0%')),
            textposition='outside',
            textfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            orientation='h',
            marker=dict(
                color=np.where(df['% Time in Range'] < 0.65, red, blue),
                line=dict(width=0)
            ),
            width=0.8,
            hovertemplate=hovertemplate,
            hoverlabel=hoverlabel,
        ),
        row=1,
        col=3
    )

    # Add the fourth bar chart in the fourth column.
    fig.add_trace(
        trace=go.Bar(
            y=[df['review'], df['patient_name']],
            x=df['% Time Below 70'],
            customdata=df['patient_id'],
            text=df['% Time Below 70'].apply(lambda x: format(x, '.1%')),
            textposition='outside',
            textfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            orientation='h',
            marker=dict(
                color=np.where(df['% Time Below 70'] > 0.04, red, blue),
                line=dict(width=0)
            ),
            width=0.8,
            hovertemplate=hovertemplate,
            hoverlabel=hoverlabel,
        ),
        row=1,
        col=4
    )

    # Add the fifth bar chart in the fifth column.
    fig.add_trace(
        trace=go.Bar(
            y=[df['review'], df['patient_name']],
            x=df['% Time Below 54'],
            customdata=df['patient_id'],
            text=df['% Time Below 54'].apply(lambda x: format(x, '.1%')),
            textposition='outside',
            textfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            orientation='h',
            marker=dict(
                color=np.where(df['% Time Below 54'] > 0.01, red, blue),
                line=dict(width=0)
            ),
            width=0.8,
            hovertemplate=hovertemplate,
            hoverlabel=hoverlabel,
        ),
        row=1,
        col=5
    )

    # Make sure to use the same y-axis across all columns.
    for i in range(len(fig['data'])):
        fig['data'][i]['yaxis'] = 'y'

    # Update the figure layout.
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        showlegend=False,
        margin=dict(t=25, r=5, b=5, l=5, pad=0),
        font=dict(
            family='Arial',
            size=9,
            color='#55514b'
        ),
        xaxis=dict(
            range=[0, df['time_worn (%)'].max() + 0.2],
            fixedrange=True,
            tickmode='array',
            tickvals=[0, 0.25, 0.5, 0.75, 1],
            tickformat='.0%',
            tickangle=0,
            tickfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            title=dict(
                text='% Time Worn',
                font=dict(
                    family='Arial',
                    size=10,
                    color='#55514b'
                ),
            ),
            color='#55514b',
            linecolor='#aca899',
            showgrid=False,
            zeroline=False,
            mirror=True,
            side='top'
        ),
        xaxis2=dict(
            range=[0, df['bg'].max() + 30],
            fixedrange=True,
            tickformat=',.0f',
            tickangle=0,
            tickfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            title=dict(
                text='Avg. Glucose (mg/dL)',
                font=dict(
                    family='Arial',
                    size=10,
                    color='#55514b'
                ),
            ),
            color='#55514b',
            linecolor='#aca899',
            showgrid=False,
            zeroline=False,
            mirror=True,
            side='top'
        ),
        xaxis3=dict(
            range=[0, df['% Time in Range'].max() + 0.2],
            fixedrange=True,
            tickmode='array',
            tickvals=[0, 0.25, 0.5, 0.75, 1],
            tickformat='.0%',
            tickangle=0,
            tickfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            title=dict(
                text='% Time in Range',
                font=dict(
                    family='Arial',
                    size=10,
                    color='#55514b'
                ),
            ),
            color='#55514b',
            linecolor='#aca899',
            showgrid=False,
            zeroline=False,
            mirror=True,
            side='top'
        ),
        xaxis4=dict(
            range=[0, np.min([df['% Time Below 70'].max() + 0.1, 1])],
            fixedrange=True,
            tickformat='.0%',
            tickangle=0,
            tickfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            title=dict(
                text='% Time Below 70',
                font=dict(
                    family='Arial',
                    size=10,
                    color='#55514b'
                ),
            ),
            color='#55514b',
            linecolor='#aca899',
            showgrid=False,
            zeroline=False,
            mirror=True,
            side='top'
        ),
        xaxis5=dict(
            range=[0, np.min([df['% Time Below 54'].max() + 0.1, 1])],
            fixedrange=True,
            tickformat='.0%',
            tickangle=0,
            tickfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            title=dict(
                text='% Time Below 54',
                font=dict(
                    family='Arial',
                    size=10,
                    color='#55514b'
                ),
            ),
            color='#55514b',
            linecolor='#aca899',
            showgrid=False,
            zeroline=False,
            mirror=True,
            side='top'
        ),
        yaxis=dict(
            fixedrange=True,
            type='multicategory',
            color='#55514b',
            linecolor='#aca899',
            dividercolor='#aca899',
            showgrid=True,
            zeroline=False,
            showdividers=True,
            tickangle=0,
            tickfont=dict(
                family='Arial',
                size=10,
                color='#55514b'
            ),
        ),
    )

    return fig.to_dict()
