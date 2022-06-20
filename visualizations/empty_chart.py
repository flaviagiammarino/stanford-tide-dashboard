import numpy as np
import plotly.graph_objects as go

empty_chart = go.Figure(
    data=go.Scatter(
        x=[np.nan],
        y=[np.nan],
        opacity=0
    ),
    layout=dict(
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(
            visible=False
        ),
        yaxis=dict(
            visible=False
        )
    )
)