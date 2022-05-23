import pandas as pd
import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask import Flask

from layouts.filters_layout import filters_layout
from layouts.bar_chart_layout import bar_chart_layout
from layouts.table_layout import table_layout
from layouts.line_chart_layout import line_chart_layout
from layouts.timeline_layout import timeline_layout
from callbacks.bar_chart_callback import update_bar_chart
from callbacks.line_charts_callback import update_line_charts

# App data.
data = pd.read_csv('data/sample_data.csv')

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

        # Filters.
        html.Div(
            children=filters_layout(data),
            style={'margin': '1.5vw 0vw 0.5vw 0vw'}
        ),

        # Bar chart.
        html.Div(
            children=bar_chart_layout,
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

        # Timeline.
        html.Div(
            children=timeline_layout,
            style={'margin': '1vw 0vw 1.5vw 0vw'}
        ),

    ]
)

# App callbacks.
@app.callback(
    [Output('bar-chart', 'figure'),
     Output('bar-chart', 'style')],
    [Input('population-checklist', 'value'),
     Input('time-worn-less-than-75-checklist', 'value'),
     Input('time-in-range-less-than-65-checklist', 'value'),
     Input('time-below-70-greater-than-4-checklist', 'value'),
     Input('time-below-54-greater-than-1-checklist', 'value'),
     Input('bar-chart', 'clickData')],
    [State('bar-chart', 'figure'),
     State('bar-chart', 'style')]
)
def bar_charts_callback(population, time_worn_less_than_75, time_in_range_less_than_65, time_below_70_greater_than_4,
time_below_54_greater_than_1, click_data, figure, style):
    
    # Update the bar chart.
    return update_bar_chart(data, population, time_worn_less_than_75, time_in_range_less_than_65, time_below_70_greater_than_4,
    time_below_54_greater_than_1, click_data, figure, style)

@app.callback(
    [Output('table-header', 'children'),
     Output('avg-clucose-table-cell', 'children'),
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
)
def line_charts_callback(population, time_worn_less_than_75, time_in_range_less_than_65, time_below_70_greater_than_4,
time_below_54_greater_than_1, click_data):
    
    # Update the table and all the line charts.
    return update_line_charts(data, population, time_worn_less_than_75, time_in_range_less_than_65, time_below_70_greater_than_4,
    time_below_54_greater_than_1, click_data)

# Run the app.
if __name__ == '__main__':
    application.run(debug=False, host='127.0.0.1')
