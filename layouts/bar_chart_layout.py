import dash_core_components as dcc
import dash_html_components as html

from plots.placeholder_chart import placeholder_chart

bar_chart_layout = html.Div(
    children=[

        # Header.
        html.Label(
            children='Patients',
            style={
                'font-weight': '600',
                'font-size': '0.85vw',
                'margin': '0',
                'padding': '0'
            }
        ),

        # Graph.
        html.Div(
            children=[

                dcc.Graph(
                    id='bar-chart',
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

            ],
            style={
                'margin': '0vw 0vw 0vw 0vw',
                'max-height': '45vh',
                'width': '100%',
                'overflow': 'scroll',
            }
        )

    ]
)
