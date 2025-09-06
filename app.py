import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Nav([
        dbc.NavLink("主页", href="/"),
        dbc.NavLink("国际房价", href="/international"),
    ], pills=True, className="mb-4"),
    dash.page_container
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)