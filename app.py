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
                html.Div(
                    id = "thermographs",
                    className = "tab tabOption menuItem tabSelected",
                    children = [
                        html.Div(className = "tabHighlight"),
                        html.Div(
                            className = "tabLabel", 
                            children = [
                                html.I(className="tabIcon fas fa-fire"),
                                "Thermographs"
                            ]
                        )
                    ]
                ),
                html.Div(
                    id = "viewData",
                    className = "tab tabOption menuItem",
                    children = [
                        html.Div(className = "tabHighlight"),
                        html.Div(
                            className = "tabLabel", 
                            children = [
                                html.I(className="tabIcon fas fa-th"),
                                "View Data"
                            ]
                        )
                    ]
                ),
                html.Div(
                    id = "accessData",
                    className = "tab tabOption menuItem",
                    children = [
                        html.Div(className = "tabHighlight"),
                        html.Div(
                            className = "tabLabel", 
                            children = [
                                html.I(className="tabIcon fas fa-server"),
                                "Access Data"
                            ]
                        )
                    ]
                ),
                html.Div(
                    id = "documentation",
                    className = "tab submenuTab menuItem",
                    children = [
                        html.Div(className = "tabHighlight"),
                        html.Div(
                            className = "tabLabel", 
                            children = [
                                html.I(className="tabIcon fas fa-file"), 
                                "Documentation",
                                html.I(className="submenuTabIcon fas fa-angle-down"),
                            ]
                        )
                    ]
                ),
                # Sub menu content
                dbc.Collapse(
                    id = "documentationSubmenu",
                    className = "submenu",
                    children = [
                        html.Div(
                            id = "userGuide",
                            className = "tabOption menuItem submenuItem",
                            children = html.Div([html.I(className="tabIcon fas fa-angle-double-right"), "User Guide"])
                        ),
                        html.Div(
                            id = "readme",
                            className = "tabOption menuItem submenuItem",
                            children = html.Div([html.I(className="tabIcon fas fa-angle-double-right"), "README"])
                        ),
                        html.Div(
                            id = "contributing",
                            className = "tabOption menuItem submenuItem",
                            children = html.Div([html.I(className="tabIcon fas fa-angle-double-right"), "CONTRIBUTING"])
                        )
                    ]
                )
            ]
        )
    ]
)

navbar = html.Div(
    id = "navbar",
    children = [
        html.I(id = "sidebar-btn", className="fa fa-bars fa-lg"),
        html.Div(
            id = "notifications",
            children = [
                html.Div(   
                    id = "notificationIconRow",                  
                    children = html.I(className="notificationIcon fas fa-envelope")
                ),
                html.Div(
                    id = "notificationsDropdowns",
                    children = [
                        html.Div(
                            id = "messagesDropdown", 
                            className = "notificationDropdwon",
                            children = [
                                html.Div(
                                    className = "notificationTitle",
                                    children = "Messages"
                                ),
                                html.Div(
                                    className = "notificationContent",
                                    children = "you got them messages. check em out. read em up. get em done."
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

content = html.Div(
    id = "page-content",
    children = [
        html.Div(
            id = "thermographs-content",
            className = "tabContent contentSelected",
            children = [
                "This is your thermograph dashboard"
            ]
        ),
        html.Div(
            id = "viewData-content",
            className = "tabContent",
            children = [
                "This is your data table"
            ]
        ),
        html.Div(
            id = "accessData-content",
            className = "tabContent",
            children = [
                "This is your access panel"
            ]
        ),
        html.Div(
            id = "userGuide-content",
            className = "tabContent",
            children = [
                "Guide thy user."
            ]
        ),
        html.Div(
            id = "readme-content",
            className = "tabContent",
            children = [
                "I am a readme. Read me."
            ]
        ),
        html.Div(
            id = "contributing-content",
            className = "tabContent",
            children = [
                "Contribute."
            ]
        )
    ]
)

mainbar = html.Div(
    id = "mainbar",
    children = [navbar, content]
)

app.layout = html.Div([dcc.Location(id="url"), sidebar, mainbar])



@app.callback(
    Output("documentationSubmenu", "is_open"),
    [Input("documentation", "n_clicks")],
    [State("documentationSubmenu", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open



if __name__ == "__main__":
    app.run_server(port=8888, debug=True)