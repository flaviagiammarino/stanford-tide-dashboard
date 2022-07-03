import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask import Flask

from layouts.bar_chart_layout import bar_chart_layout
from layouts.table_layout import table_layout
from layouts.line_chart_layout import line_chart_layout
from layouts.calendar_chart_layout import calendar_chart_layout

from callbacks.bar_chart_callbacks import update_bar_chart
from callbacks.table_callbacks import update_table
from callbacks.line_chart_callbacks import update_line_chart
from callbacks.calendar_chart_callbacks import update_calendar_chart

# App data (sample).
from data.sample_data import load_sample_data
df = load_sample_data()

# App data (random).
# from data.sample_data import generate_random_data
# df = generate_random_data()

# App set-up.
server = Flask(__name__)

app = dash.Dash(
    name=__name__,
    server=server,
    title='Stanford TIDE',
    update_title=None
)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True

application = app.server

# App layout.
app.layout = html.Div(
    children=[
        
        # Bar chart.
        html.Div(
            children=bar_chart_layout(
                populations=df['population'].sort_values().unique().tolist()
            ),
            style={'margin': '1vw 0vw 0.5vw 0vw'}
        ),

        # Table.
        html.Div(
            children=table_layout,
            style={'margin': '1vw 0vw 0.5vw 0vw'}
        ),

        # Line chart.
        html.Div(
            children=line_chart_layout,
            style={'margin': '1vw 0vw 1vw 0vw'}
        ),

        # Calendar chart.
        html.Div(
            children=calendar_chart_layout,
            style={'margin': '1vw 0vw 1.5vw 0vw'}
        ),

    ]
)

# App callbacks.
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('bar-chart', 'style'),
     Output('table-header', 'children'),
     Output('avg-glucose-table-cell', 'children'),
     Output('very-low-table-cell', 'children'),
     Output('low-table-cell', 'children'),
     Output('in-target-range-table-cell', 'children'),
     Output('high-table-cell', 'children'),
     Output('very-high-table-cell', 'children'),
     Output('coefficient-variation-table-cell', 'children'),
     Output('standard-deviation-table-cell', 'children'),
     Output('time-active-table-cell', 'children'),
     Output('line-chart-header', 'children'),
     Output('line-chart', 'figure'),
     Output('monday-week-1', 'figure'),
     Output('tuesday-week-1', 'figure'),
     Output('wednesday-week-1', 'figure'),
     Output('thursday-week-1', 'figure'),
     Output('friday-week-1', 'figure'),
     Output('saturday-week-1', 'figure'),
     Output('sunday-week-1', 'figure'),
     Output('monday-week-2', 'figure'),
     Output('tuesday-week-2', 'figure'),
     Output('wednesday-week-2', 'figure'),
     Output('thursday-week-2', 'figure'),
     Output('friday-week-2', 'figure'),
     Output('saturday-week-2', 'figure'),
     Output('sunday-week-2', 'figure'),
     Output('monday-week-3', 'figure'),
     Output('tuesday-week-3', 'figure'),
     Output('wednesday-week-3', 'figure'),
     Output('thursday-week-3', 'figure'),
     Output('friday-week-3', 'figure'),
     Output('saturday-week-3', 'figure'),
     Output('sunday-week-3', 'figure')],
    [Input('population-checklist', 'value'),
     Input('time-worn-less-than-75-checklist', 'value'),
     Input('time-in-range-less-than-65-checklist', 'value'),
     Input('time-below-70-greater-than-4-checklist', 'value'),
     Input('time-below-54-greater-than-1-checklist', 'value'),
     Input('bar-chart', 'clickData')],
    [State('bar-chart', 'figure'),
     State('bar-chart', 'style')]
)
def update_dashboard(populations,
                     time_worn_less_than_75,
                     time_in_range_less_than_65,
                     time_below_70_greater_than_4,
                     time_below_54_greater_than_1,
                     click_data,
                     figure,
                     style):
    
    # Create a copy of the patients' dataset.
    data = df.copy()
    
    # Check which inputs have triggered the callback.
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    
    # Update the bar chart.
    outputs = update_bar_chart(data,
                               populations,
                               time_worn_less_than_75,
                               time_in_range_less_than_65,
                               time_below_70_greater_than_4,
                               time_below_54_greater_than_1,
                               click_data,
                               figure,
                               style,
                               changed_id)

    # If a patient has been selected, use only the data for this patient.
    if 'bar-chart.clickData' in changed_id:
        
        # Extract the id of the selected patient.
        id = click_data['points'][0]['customdata']
        
        # Extract the data for the selected patient.
        data = data[data['id'] == id].reset_index(drop=True)
    
    # Update the table.
    outputs.extend(update_table(data))

    # Update the line chart.
    outputs.extend(update_line_chart(data))

    # Update the calendar chart.
    outputs.extend(update_calendar_chart(data))
    
    return outputs


# Run the app.
if __name__ == '__main__':
    application.run(debug=False, host='127.0.0.1')
