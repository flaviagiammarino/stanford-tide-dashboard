import dash_html_components as html

# First row.
first_row = [html.Tr(
    children=[

        # First column.
        html.Div(
            children=[

                html.P(
                    children=['Avg. Glucose'],
                    style={
                        'margin': '0.5vw 0vw 0vw 0vw',
                        'padding': '0',
                    }
                ),

                html.P(
                    children='mg/dL',
                    style={
                        'margin': '0vw 0vw 0.5vw 0vw',
                        'padding': '0'
                    }
                ),

            ],
            className='table-cell',
            style={
                'background-color': 'rgba(233, 195, 155, 0.25)',
                'font-weight': '600',
            }
        ),

        # Second column.
        html.Div(
            children=[

                html.P(
                    children='Very Low',
                    style={
                        'margin': '0.5vw 0vw 0vw 0vw',
                        'padding': '0'
                    }
                ),

                html.P(
                    children='< 54 mg/dL',
                    style={
                        'margin': '0vw 0vw 0.5vw 0vw',
                        'padding': '0',
                        'font-weight': 'normal'
                    }
                ),

            ],
            className='table-cell',
            style={
                'background-color': 'rgba(134, 180, 169, 0.25)',
                'font-weight': '600',
            }

        ),

        # Third column.
        html.Div(
            children=[

                html.P(
                    children='Low',
                    style={
                        'margin': '0.5vw 0vw 0vw 0vw',
                        'padding': '0'
                    }
                ),

                html.P(
                    children='< 70 mg/dL',
                    style={
                        'margin': '0vw 0vw 0.5vw 0vw',
                        'padding': '0',
                        'font-weight': 'normal'
                    }
                ),
                
            ],
            className='table-cell',
            style={
                'background-color': 'rgba(134, 180, 169, 0.25)',
                'font-weight': '600',
            }
        ),

        # Fourth column.
        html.Div(
            children=[

                html.P(
                    children='In Target Range',
                    style={
                        'margin': '0.5vw 0vw 0vw 0vw',
                        'padding': '0'
                    }
                ),

                html.P(
                    children='70 - 180 mg/dL',
                    style={
                        'margin': '0vw 0vw 0.5vw 0vw',
                        'padding': '0',
                        'font-weight': 'normal'
                    }
                ),

            ],
            className='table-cell',
            style={
                'background-color': 'rgba(134, 180, 169, 0.25)',
                'font-weight': '600',
            }
        ),

        # Fifth column.
        html.Div(
            children=[

                html.P(
                    children='High',
                    style={
                        'margin': '0.5vw 0vw 0vw 0vw',
                        'padding': '0'
                    }
                ),

                html.P(
                    children='> 180 mg/dL',
                    style={
                        'margin': '0vw 0vw 0.5vw 0vw',
                        'padding': '0',
                        'font-weight': 'normal'
                    }
                ),

            ],
            className='table-cell',
            style={
                'background-color': 'rgba(134, 180, 169, 0.25)',
                'font-weight': '600',
            }
        ),

        # Sixth column.
        html.Div(
            children=[

                html.P(
                    children='Very High',
                    style={
                        'margin': '0.5vw 0vw 0vw 0vw',
                        'padding': '0'
                    }
                ),

                html.P(
                    children='> 250 mg/dL',
                    style={
                        'margin': '0vw 0vw 0.5vw 0vw',
                        'padding': '0',
                        'font-weight': 'normal'
                    }
                ),

            ],
            className='table-cell',
            style={
                'background-color': 'rgba(134, 180, 169, 0.25)',
                'font-weight': '600',
            }
        ),

        # Seventh column.
        html.Div(
            children=[

                html.P(
                    children='Coefficient of',
                    style={
                        'margin': '0.5vw 0vw 0vw 0vw',
                        'padding': '0'
                    }
                ),

                html.P(
                    children='Variation',
                    style={
                        'margin': '0vw 0vw 0.5vw 0vw',
                        'padding': '0'
                    }
                ),

            ],
            className='table-cell',
            style={
                'background-color': 'rgba(255, 185, 119, 0.25)',
                'font-weight': '600',
            }
        ),

        # Eighth column.
        html.Div(
            children=[

                html.P(
                    children='SD',
                    style={
                        'margin': '0.5vw 0vw 0vw 0vw',
                        'padding': '0'
                    }
                ),

                html.P(
                    children='mg/dL',
                    style={
                        'margin': '0vw 0vw 0.5vw 0vw',
                        'padding': '0'
                    }
                ),

            ],
            className='table-cell',
            style={
                'background-color': 'rgba(255, 185, 119, 0.25)',
                'font-weight': '600',
            }
        ),

        # Ninth column
        html.Div(
            children=[

                html.P(
                    children='% Time CGM',
                    style={
                        'margin': '0.5vw 0vw 0vw 0vw',
                        'padding': '0'
                    }
                ),

                html.P(
                    children='Active',
                    style={
                        'margin': '0vw 0vw 0.5vw 0vw',
                        'padding': '0'
                    }
                ),

            ],
            className='table-cell',
            style={
                'background-color': 'rgba(207, 207, 207, 0.25)',
                'font-weight': '600',
            }
        ),
    ]

)]

# Second row.
second_row = [html.Tr(
    children=[

        # First column
        html.Div(
            id='avg-glucose-table-cell',
            className='table-cell',
            style={
                'border-left': '0.1vw solid #aca899',
                'border-right': '0.1vw solid #aca899',
                'box-sizing': 'border-box',
                'padding': '0.5vw 0vw 0vw 0vw',
                'margin': '0',
                'font-size': '0.84vw',
                'font-weight': '600',
                'color': 'rgb(255, 128, 14)',
                'height': '2vw',
                'line-height': '2vw',
            }
        ),

        # Second column.
        html.Div(
            id='very-low-table-cell',
            className='table-cell',
            style={
                'border-right': '0.1vw solid #aca899',
                'box-sizing': 'border-box',
                'padding': '0.5vw 0vw 0vw 0vw',
                'margin': '0',
                'font-size': '0.84vw',
                'font-weight': '600',
                'color': 'rgb(57, 115, 124)',
                'height': '2vw',
                'line-height': '2vw',
            }
        ),

        # Third column.
        html.Div(
            id='low-table-cell',
            className='table-cell',
            style={
                'border-right': '0.1vw solid #aca899',
                'box-sizing': 'border-box',
                'padding': '0.5vw 0vw 0vw 0vw',
                'margin': '0',
                'font-size': '0.84vw',
                'font-weight': '600',
                'color': 'rgb(57, 115, 124)',
                'height': '2vw',
                'line-height': '2vw',
            }
        ),

        # Fourth column.
        html.Div(
            id='in-target-range-table-cell',
            className='table-cell',
            style={
                'border-right': '0.1vw solid #aca899',
                'box-sizing': 'border-box',
                'padding': '0.5vw 0vw 0vw 0vw',
                'margin': '0',
                'font-size': '0.84vw',
                'font-weight': '600',
                'color': 'rgb(57, 115, 124)',
                'height': '2vw',
                'line-height': '2vw',
            }
        ),

        # Fifth column.
        html.Div(
            id='high-table-cell',
            className='table-cell',
            style={
                'border-right': '0.1vw solid #aca899',
                'box-sizing': 'border-box',
                'padding': '0.5vw 0vw 0vw 0vw',
                'margin': '0',
                'font-size': '0.84vw',
                'font-weight': '600',
                'color': 'rgb(57, 115, 124)',
                'height': '2vw',
                'line-height': '2vw',
            }
        ),

        # Sixth column.
        html.Div(
            id='very-high-table-cell',
            className='table-cell',
            style={
                'border-right': '0.1vw solid #aca899',
                'box-sizing': 'border-box',
                'padding': '0.5vw 0vw 0vw 0vw',
                'margin': '0',
                'font-size': '0.84vw',
                'font-weight': '600',
                'color': 'rgb(57, 115, 124)',
                'height': '2vw',
                'line-height': '2vw',
            }
        ),

        # Seventh column.
        html.Div(
            id='coefficient-variation-table-cell',
            className='table-cell',
            style={
                'border-right': '0.1vw solid #aca899',
                'box-sizing': 'border-box',
                'padding': '0.5vw 0vw 0vw 0vw',
                'margin': '0',
                'font-size': '0.84vw',
                'font-weight': '600',
                'color': 'rgb(200, 82, 0)',
                'height': '2vw',
                'line-height': '2vw',
            }
        ),

        # Eighth column.
        html.Div(
            id='standard-deviation-table-cell',
            className='table-cell',
            style={
                'border-right': '0.1vw solid #aca899',
                'box-sizing': 'border-box',
                'padding': '0.5vw 0vw 0vw 0vw',
                'margin': '0',
                'font-size': '0.84vw',
                'font-weight': '600',
                'color': 'rgb(200, 82, 0)',
                'height': '2vw',
                'line-height': '2vw',
            }
        ),

        # Ninth column.
        html.Div(
            id='time-active-table-cell',
            className='table-cell',
            style={
                'border-right': '0.1vw solid #aca899',
                'box-sizing': 'border-box',
                'padding': '0.5vw 0vw 0vw 0vw',
                'margin': '0',
                'font-size': '0.84vw',
                'font-weight': '600',
                'color': 'rgb(165, 172, 175)',
                'height': '2vw',
                'line-height': '2vw',
            }
        ),

    ]

)]

# Full table.
table_layout = html.Div(
    children=[

        # Header.
        html.Label(
            id='table-header',
            style={
                'font-weight': '600',
                'font-size': '0.95vw',
                'margin': '1vw 0vw 1vw 0vw',
                'padding': '0',
                'display': 'block'
            }
        ),

        # Table.
        html.Table(
            children=first_row + second_row,
            style={
                'margin': '1vw 0vw 0.5vw 0vw',
                'padding': '0',
                'display': 'block'
            }
        )

    ]
)
