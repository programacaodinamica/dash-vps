import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
server = app.server

df = px.data.gapminder().query("year == 2007")
fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 hover_name="country", log_x=True)

app.layout = html.Div([
    html.H1("Dashboard com Plotly Dash"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)