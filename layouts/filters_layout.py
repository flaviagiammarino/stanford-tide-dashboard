import dash_core_components as dcc
import dash_html_components as html

def filters_layout(data):
    return html.Div(
        children=[
    
            # Population.
            html.Div(
                children=[
    
                    html.P(
                        children=['Population'],
                        className='checklist-title'
                    ),
    
                    dcc.Checklist(
                        id='population-checklist',
                        options=[{'value': x, 'label': x} for x in data['population'].unique()],
                        value=data['population'].unique().tolist(),
                        inputClassName='checklist-input',
                        labelClassName='checklist-label'
                    ),
    
                ],
                className='checklist-container'
            ),
    
            # Time worn.
            html.Div(
                children=[
    
                    html.P(
                        children=['Time Worn < 75%?'],
                        className='checklist-title'
                    ),
    
                    dcc.Checklist(
                        id='time-worn-less-than-75-checklist',
                        options=[{'value': 'No', 'label': 'No'}],
                        inputClassName='checklist-input',
                        labelClassName='checklist-label'
                    ),
    
                ],
                className='checklist-container'
            ),
    
            # Time in range.
            html.Div(
                children=[
    
                    html.P(
                        children=['Time in Range < 65%?'],
                        className='checklist-title'
                    ),
    
                    dcc.Checklist(
                        id='time-in-range-less-than-65-checklist',
                        options=[
                            {'value': 'Yes', 'label': 'Yes'},
                            {'value': 'No', 'label': 'No'},
                        ],
                        value=['Yes', 'No'],
                        inputClassName='checklist-input',
                        labelClassName='checklist-label'
                    ),
    
                ],
                className='checklist-container'
            ),
    
            # Time below 70%.
            html.Div(
                children=[
    
                    html.P(
                        children=['Time Below < 70% > 4%?'],
                        className='checklist-title'
                    ),
    
                    dcc.Checklist(
                        id='time-below-70-greater-than-4-checklist',
                        options=[
                            {'value': 'Yes', 'label': 'Yes'},
                            {'value': 'No', 'label': 'No'},
                        ],
                        value=['Yes', 'No'],
                        inputClassName='checklist-input',
                        labelClassName='checklist-label'
                    ),
    
                ],
                className='checklist-container'
            ),
    
            # Time below 54%.
            html.Div(
                children=[
    
                    html.P(
                        children=['Time Below < 54% > 1%?'],
                        className='checklist-title'
                    ),
    
                    dcc.Checklist(
                        id='time-below-54-greater-than-1-checklist',
                        options=[
                            {'value': 'Yes', 'label': 'Yes'},
                            {'value': 'No', 'label': 'No'},
                        ],
                        value=['Yes', 'No'],
                        inputClassName='checklist-input',
                        labelClassName='checklist-label'
                    ),
    
                ],
                className='checklist-container'
            ),
    
        ],
        style={
            'display': 'flex',
            'padding': '0.5vw 0vw 0.5vw 0vw',
            'background-color': 'rgba(233, 195, 155, 0.25)'
        }
    )
