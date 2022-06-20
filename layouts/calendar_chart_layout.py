import dash_core_components as dcc
import dash_html_components as html

from visualizations.empty_chart import empty_chart

# First row
first_row = [html.Tr(
    children=[

        # First column.
        html.Div(
            children='Monday',
            className='calendar-header',
        ),

        # Second column.
        html.Div(
            children='Tuesday',
            className='calendar-header',
        ),

        # Third column.
        html.Div(
            children='Wednesday',
            className='calendar-header',
        ),

        # Fourth column.
        html.Div(
            children='Thursday',
            className='calendar-header',
        ),

        # Fifth column.
        html.Div(
            children='Friday',
            className='calendar-header',
        ),

        # Sixth column.
        html.Div(
            children='Saturday',
            className='calendar-header',
        ),

        # Seventh column.
        html.Div(
            children='Sunday',
            className='calendar-header',
        ),

    ],
)]

# Second row
second_row = [html.Tr(
    children=[

        # First column.
        html.Div(
            children=dcc.Graph(
                id='monday-week-1',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Second column.
        html.Div(
            children=dcc.Graph(
                id='tuesday-week-1',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Third column.
        html.Div(
            children=dcc.Graph(
                id='wednesday-week-1',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Fourth column.
        html.Div(
            children=dcc.Graph(
                id='thursday-week-1',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Fifth column.
        html.Div(
            children=dcc.Graph(
                id='friday-week-1',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Sixth column.
        html.Div(
            children=dcc.Graph(
                id='saturday-week-1',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Seventh column.
        html.Div(
            children=dcc.Graph(
                id='sunday-week-1',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

    ],
)]

# Third row
third_row = [html.Tr(

    children=[

        # First column.
        html.Div(
            children=dcc.Graph(
                id='monday-week-2',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Second column.
        html.Div(
            children=dcc.Graph(
                id='tuesday-week-2',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Third column.
        html.Div(
            children=dcc.Graph(
                id='wednesday-week-2',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Fourth column.
        html.Div(
            children=dcc.Graph(
                id='thursday-week-2',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Fifth column.
        html.Div(
            children=dcc.Graph(
                id='friday-week-2',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Sixth column.
        html.Div(
            children=dcc.Graph(
                id='saturday-week-2',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Seventh column.
        html.Div(
            children=dcc.Graph(
                id='sunday-week-2',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

    ],

)]

# Fourth row.
fourth_row = [html.Tr(

    children=[

        # First column.
        html.Div(
            children=dcc.Graph(
                id='monday-week-3',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Second column.
        html.Div(
            children=dcc.Graph(
                id='tuesday-week-3',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Third column.
        html.Div(
            children=dcc.Graph(
                id='wednesday-week-3',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Fourth column.
        html.Div(
            children=dcc.Graph(
                id='thursday-week-3',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Fifth column.
        html.Div(
            children=dcc.Graph(
                id='friday-week-3',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Sixth column.
        html.Div(
            children=dcc.Graph(
                id='saturday-week-3',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

        # Seventh column.
        html.Div(
            children=dcc.Graph(
                id='sunday-week-3',
                figure=empty_chart,
                config={
                    'responsive': True,
                    'autosizable': True,
                    'displayModeBar': False,
                },
                style={
                    'display': 'block',
                    'width': '100%',
                    'height': '100%',
                    'margin': '0',
                    'padding': '0'
                }
            ),
            className='calendar-cell',
        ),

    ],

)]

# Full table.
calendar_chart_layout = html.Table(
    children=first_row + second_row + third_row + fourth_row,
    style={
        'margin': '1vw 0vw 0.5vw 0vw',
        'padding': '0',
        'display': 'block'
    }
)
