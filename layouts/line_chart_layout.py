import dash_core_components as dcc
import dash_html_components as html

from plots.placeholder_chart import placeholder_chart

line_chart_layout = html.Div(

    children=[

        # Header.
        html.Label(
            id='line-chart-header',
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
                    id='line-chart',
                    figure=placeholder_chart,
                    config={
                        'responsive': True,
                        'autosizable': True,
                        'displayModeBar': False,
                    },
                    style={
                        'display': 'block',
                        'width': '100%',
                        'height': 'calc(15vw + 15vh)',
                        'margin': '0',
                        'padding': '0'
                    }
                )

            ],
            style={
                'display': 'block',
                'width': '100%',
                'height': 'calc(15vw + 15vh)',
                'margin': '0',
                'padding': '0'
            }
        )

    ]
)
