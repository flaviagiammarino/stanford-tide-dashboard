import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def bar_chart(data):
    '''
    Generate the bar chart.
    
    Parameters:
    ----------------------------------
    data: pd.DataFrame.
        Data frame with average blood glucose level, time worn, time in range, time in hypoglycemia
        and time in extreme hypoglycemia over the last 7 days.
    
    Returns:
    ----------------------------------
    dict.
        Figure dictionary.
    '''

    # Initialize the figure.
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
        '<b>% Time Worn: </b>' + data['time_worn'].apply(lambda x: format(x, '.0%')) + '<br>' + \
        '<b>Avg. Glucose (mg/dL): </b>' + data['bg'].apply(lambda x: format(x, '.0f')) + '<br>' + \
        '<b>% Time in Range: </b>' + data['in_range'].apply(lambda x: format(x, '.0%')) + '<br>' + \
        '<b>% Time Below 70: </b>' + data['hypo'].apply(lambda x: format(x, '.1%')) + '<br>' + \
        '<b>% Time Below 54: </b>' + data['extreme_hypo'].apply(lambda x: format(x, '.1%')) + '<extra></extra>'

    # Define the colorscale.
    blue = 'rgba(31, 119, 180, 0.9)'
    red = 'rgba(214, 39, 40, 0.9)'

    # Add the first bar chart in the first column.
    fig.add_trace(
        trace=go.Bar(
            y=[data['review'], data['name']],
            x=data['time_worn'],
            customdata=data['id'],
            text=data['time_worn'].apply(lambda x: format(x, '.0%')),
            textposition='outside',
            textfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            orientation='h',
            marker=dict(
                color=np.where(data['time_worn'] < 0.75, red, blue),
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
            y=[data['review'], data['name']],
            x=data['bg'],
            customdata=data['id'],
            text=data['bg'].apply(lambda x: format(x, ',.0f')),
            textposition='outside',
            textfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            orientation='h',
            marker=dict(
                color=np.where(data['bg'] < 54, red, blue),
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
            y=[data['review'], data['name']],
            x=data['in_range'],
            customdata=data['id'],
            text=data['in_range'].apply(lambda x: format(x, '.0%')),
            textposition='outside',
            textfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            orientation='h',
            marker=dict(
                color=np.where(data['in_range'] < 0.65, red, blue),
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
            y=[data['review'], data['name']],
            x=data['hypo'],
            customdata=data['id'],
            text=data['hypo'].apply(lambda x: format(x, '.1%')),
            textposition='outside',
            textfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            orientation='h',
            marker=dict(
                color=np.where(data['hypo'] > 0.04, red, blue),
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
            y=[data['review'], data['name']],
            x=data['extreme_hypo'],
            customdata=data['id'],
            text=data['extreme_hypo'].apply(lambda x: format(x, '.1%')),
            textposition='outside',
            textfont=dict(
                family='Arial',
                size=8,
                color='#55514b'
            ),
            orientation='h',
            marker=dict(
                color=np.where(data['extreme_hypo'] > 0.01, red, blue),
                line=dict(width=0)
            ),
            width=0.8,
            hovertemplate=hovertemplate,
            hoverlabel=hoverlabel,
        ),
        row=1,
        col=5
    )

    # Use the same y-axis across all columns.
    for i in range(len(fig['data'])):
        fig['data'][i]['yaxis'] = 'y'

    # Add the figure layout.
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
            range=[0, data['time_worn'].max() + 0.2],
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
            range=[0, data['bg'].max() + 30],
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
            range=[0, data['in_range'].max() + 0.2],
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
            range=[0, np.min([data['hypo'].max() + 0.1, 1])],
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
            range=[0, np.min([data['extreme_hypo'].max() + 0.1, 1])],
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
