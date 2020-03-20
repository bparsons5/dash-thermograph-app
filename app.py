import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# link fontawesome to get the chevron icons

app = dash.Dash(
    external_scripts=["https://code.jquery.com/jquery-3.4.1.min.js"], # there is a high side jquery cdn
    external_stylesheets=[dbc.themes.BOOTSTRAP] # files in assets/css files are automatically included
)

sidebar = html.Div(
    id = "sidebar",
    children = [
        html.Div(
            id = "sidebar-title",
            children = [
                html.H4("Thermograph App")
            ]
        ),
        html.Div(
            id = "sidebar-content",
            children = [
                html.H2("Sidebar", className="display-4"),
                html.Hr(),
                html.P(
                    "A sidebar with collapsible navigation links", className="lead"
                )
                # dbc.Nav(submenu_1 + submenu_2, vertical=True)
            ]
        )
    ]
)

navbar = html.Div(
    id = "navbar",
    children = [
        html.I(id = "sidebar-btn", className="fa fa-bars fa-lg")
    ]
)

content = html.Div(id="page-content")

mainbar = html.Div(
    id = "mainbar",
    children = [navbar, content]
)

app.layout = html.Div([dcc.Location(id="url"), sidebar, mainbar])


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)