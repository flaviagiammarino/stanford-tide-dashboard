import dash_core_components as dcc
import dash_html_components as html

from plots.placeholder_chart import placeholder_chart

# First row
first_row = [html.Tr(
    children=[

        # First column.
        html.Div(
            children='Monday',
            className='timeline-header',
        ),

        # Second column.
        html.Div(
            children='Tuesday',
            className='timeline-header',
        ),

        # Third column.
        html.Div(
            children='Wednesday',
            className='timeline-header',
        ),

        # Fourth column.
        html.Div(
            children='Thursday',
            className='timeline-header',
        ),

        # Fifth column.
        html.Div(
            children='Friday',
            className='timeline-header',
        ),

        # Sixth column.
        html.Div(
            children='Saturday',
            className='timeline-header',
        ),

        # Seventh column.
        html.Div(
            children='Sunday',
            className='timeline-header',
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
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Second column.
        html.Div(
            children=dcc.Graph(
                id='tuesday-week-1',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Third column.
        html.Div(
            children=dcc.Graph(
                id='wednesday-week-1',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Fourth column.
        html.Div(
            children=dcc.Graph(
                id='thursday-week-1',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Fifth column.
        html.Div(
            children=dcc.Graph(
                id='friday-week-1',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Sixth column.
        html.Div(
            children=dcc.Graph(
                id='saturday-week-1',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Seventh column.
        html.Div(
            children=dcc.Graph(
                id='sunday-week-1',
                figure=placeholder_chart,
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
            className='timeline-cell',
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
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Second column.
        html.Div(
            children=dcc.Graph(
                id='tuesday-week-2',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Third column.
        html.Div(
            children=dcc.Graph(
                id='wednesday-week-2',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Fourth column.
        html.Div(
            children=dcc.Graph(
                id='thursday-week-2',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Fifth column.
        html.Div(
            children=dcc.Graph(
                id='friday-week-2',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Sixth column.
        html.Div(
            children=dcc.Graph(
                id='saturday-week-2',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Seventh column.
        html.Div(
            children=dcc.Graph(
                id='sunday-week-2',
                figure=placeholder_chart,
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
            className='timeline-cell',
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
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Second column.
        html.Div(
            children=dcc.Graph(
                id='tuesday-week-3',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Third column.
        html.Div(
            children=dcc.Graph(
                id='wednesday-week-3',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Fourth column.
        html.Div(
            children=dcc.Graph(
                id='thursday-week-3',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Fifth column.
        html.Div(
            children=dcc.Graph(
                id='friday-week-3',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Sixth column.
        html.Div(
            children=dcc.Graph(
                id='saturday-week-3',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

        # Seventh column.
        html.Div(
            children=dcc.Graph(
                id='sunday-week-3',
                figure=placeholder_chart,
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
            className='timeline-cell',
        ),

    ],

)]

# Full table.
timeline_layout = html.Table(
    children=first_row + second_row + third_row + fourth_row,
    style={
        'margin': '1vw 0vw 0.5vw 0vw',
        'padding': '0',
        'display': 'block'
    }
)
