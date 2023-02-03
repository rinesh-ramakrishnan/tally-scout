import dash
from dash import dcc
from dash import html


from graphs.overall_report import figure as overall


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            children="Tally Scout Analytics",
            className="title"
        ),
        html.P(
            children="Dashboard to analyze Income Vs Expenses",
            className='desc'
        ),
        dcc.Graph(
            figure=overall,
        ),
    ]
)

app.run_server(debug=True)