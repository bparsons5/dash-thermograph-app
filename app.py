import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
import dash_table
import pandas as pd
import markdown
import numpy as np

# GLOBAL

df = pd.read_excel("assets/data/objective data.xlsx")
objectives = {}
metrics = {}
gauges = {}


# GRAPH FUNCTIONS
def thermograph(last, current):
    fig = go.Figure()

    fig.add_trace(
        go.Heatmap(
            z=[[0, 100],[1, 100]],
            x=[0,100], # horizontal axis
            y=[0, 1], # vertical axis
            showscale=False,
            zsmooth='best',
            colorscale = [[0, 'rgba(184,15,10,.6)'], [0.33, 'rgba(249,166,2,.6)'], [0.67, 'rgba(199,234,70,.6)'], [1, 'rgba(11,102,35,.6)']]
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[last, current],
            y=[.45, .55],
            mode="markers",
            marker_symbol=["triangle-up", "triangle-down"],
            marker_color=["rgb(97, 151, 171)", "rgb(27, 37, 47)"],
            marker=dict(
                color="black",
                size = 30
            )
        )
    )

    fig.update_layout(
        paper_bgcolor = 'rgba(0,0,0,0)', 
        xaxis=dict(
            range=[0,100]
        ),
        yaxis=dict(
            range=[0,1],
            showticklabels=False
        ),
        yaxis_showgrid=False,
        showlegend=True,
        height=100,
        margin=dict(
            l=5,
            r=5,
            b=15,
            t=15
        ),
    )

    return(fig)

def thermograph2(data):
    fig = go.Figure()

    fig.add_trace(
        go.Heatmap(
            z=[[0, 100],[1, 100]],
            x=[0,100], # horizontal axis
            y=[0, 1], # vertical axis
            showscale=False,
            zsmooth='best',
            colorscale = [[0, 'rgba(184,15,10,.6)'], [0.33, 'rgba(249,166,2,.6)'], [0.67, 'rgba(199,234,70,.6)'], [1, 'rgba(11,102,35,.6)']]
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data['x'],
            y=data['y'],
            text=data['x'],
            mode="markers",
            marker_symbol=data['symbol'],
            marker_color=data['color'],
            marker=dict(
                color="black",
                size = 30
            )
        )
    )

    fig.update_layout(
        paper_bgcolor = 'rgba(0,0,0,0)', 
        xaxis=dict(
            range=[0,100]
        ),
        yaxis=dict(
            range=[0,1],
            showticklabels=False
        ),
        yaxis_showgrid=False,
        showlegend=True,
        height=100,
        margin=dict(
            l=5,
            r=5,
            b=15,
            t=15
        ),
    )

    return(fig)

def gauge(last, current):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = current,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Speed", 'font': {'size': 24}},
        delta = {'reference': last, 'increasing': {'color': "rgba(52,62,64,1)"}, 'decreasing': {'color': "rgba(52,62,64,1)"}},
        gauge = {
            'axis': {'range': [None, 120], 'tickwidth': 1, 'tickcolor': "rgba(60, 141, 188,1)"},
            'bar': {'color': "rgba(52,62,64,1)"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': 'rgba(212, 111, 108,1)'},
                {'range': [50, 90], 'color': 'rgba(239, 223, 128,1)'},
                {'range': [90, 110], 'color': 'rgba(109, 164, 123,1)'},
                {'range': [110, 120], 'color': 'rgba(236, 240, 245,1)'}],
            'threshold': {
                'line': {'color': "rgba(52,62,64,1)", 'width': 4},
                'thickness': 0.75,
                'value': 100}}))

    fig.update_layout(
        margin=dict(
            l=20,
            r=30,
            b=0,
            t=0
        ),
        paper_bgcolor = 'rgba(0,0,0,0)', 
        font = {'color': "rgba(60, 141, 188,1)", 'family': "Arial"},
        height = 300,
        width = 400
    )

    return(fig)


def gauge2(data):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = data['current'],
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': data['metric'], 'font': {'size': 24}},
        delta = {'reference': data['last'], 'increasing': {'color': "rgba(52,62,64,1)"}, 'decreasing': {'color': "rgba(52,62,64,1)"}},
        gauge = {
            'axis': {'range': [None, 120], 'tickwidth': 1, 'tickcolor': "rgba(60, 141, 188,1)"},
            'bar': {'color': "rgba(52,62,64,1)"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': 'rgba(212, 111, 108,1)'},
                {'range': [50, 90], 'color': 'rgba(239, 223, 128,1)'},
                {'range': [90, 110], 'color': 'rgba(109, 164, 123,1)'},
                {'range': [110, 120], 'color': 'rgba(236, 240, 245,1)'}],
            'threshold': {
                'line': {'color': "rgba(52,62,64,1)", 'width': 4},
                'thickness': 0.75,
                'value': 100}}))

    fig.update_layout(
        margin=dict(
            l=20,
            r=30,
            b=0,
            t=0
        ),
        paper_bgcolor = 'rgba(0,0,0,0)', 
        font = {'color': "rgba(60, 141, 188,1)", 'family': "Arial"},
        height = 300,
        width = 400
    )

    return(fig)


def createVisualizations(df):
    global objectives
    global metrics
    global gauges
    # - - - - - - - - - - - - - - - - - - - #
    # Data Format
    # - - - - - - - - - - - - - - - - - - - #
    data = pd.DataFrame(
        data = {
            'x': [0, 0],
            'y': [.55,.45],
            'category': ['last','current'],
            'color': ['rgba(54, 127, 169,1)', 'rgba(34,45,50,1)'],
            'symbol': ['triangle-down','triangle-up']
        }
    )
    
    # - - - - - - - - - - - - - - - - - - - #
    # OBJECTIVES
    # - - - - - - - - - - - - - - - - - - - #
    # create filtered data for objectives
    df['lastPerMetric'] = df['last'] * df['weight per obj']
    df['currentPerMetric'] = df['current'] * df['weight per obj']
    lastPerObj = df.groupby("objective")['lastPerMetric'].sum().values
    currentPerMetric = df.groupby("objective")['currentPerMetric'].sum().values
    dfObj = pd.DataFrame(
        data = {
            'objective': df['objective'].unique(),
            'lastPerObj': lastPerObj,
            'currentPerObj': currentPerMetric
        }
    )
    
    # loop to create objectives 
    # must use lapply. for loops do not work for dynamically creating output variables
    for i in range(0, len(df['objective'].unique())):
        # filter down to appropriate data
        lineData = dfObj.iloc[i]
        data['x'] = [lineData['lastPerObj'], lineData['currentPerObj']]

        objectives["thermograph"+ lineData['objective']] = thermograph2(data)

    
    # - - - - - - - - - - - - - - - - - - - #
    # METRICS
    # - - - - - - - - - - - - - - - - - - - #
    
    # loop to create metrics 
    for i in range(0, len(df['metric'])):
        # filter down to appropriate data
        lineData = df.iloc[i]
        data['x'] = [lineData['last'], lineData['current']]
        metrics["thermograph" + lineData['metric']] = thermograph2(data)
        gauges["gauge" + lineData['metric']] = gauge2(lineData)


# RUN SETUP FUNCTIONS
createVisualizations(df)


# UI

app = dash.Dash(
    external_scripts=["https://code.jquery.com/jquery-3.4.1.min.js"], # there is a high side jquery cdn
    external_stylesheets=[dbc.themes.BOOTSTRAP] # files in assets/css files are automatically included
)

readme = open('README.md').read()
contributing = open('CONTRIBUTING.md').read()

sidebar = html.Div(
    id = "sidebar",
    children = [
        html.Div(
            id = "sidebar-title",
            children = [
                html.H4("Thermograph App v2")
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
        ),
        html.Div(
            id = "controls",
            children = [
                html.H5("Controls"),
                dcc.Dropdown(
                    id='objective_selection',
                    options=[{'label': i, 'value': i} for i in df['objective'].unique()],
                    value=df['objective'].unique()[0]
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

card = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="PoC Overview", tab_id="poc-overview"),
                    dbc.Tab(label="Dendrogram", tab_id="dendrogram"),
                    dbc.Tab(label="Network", tab_id="network"),
                    dbc.Tab(label="Sunburst", tab_id="sunburst"),
                ],
                id="card-tabs",
                card=True,
                active_tab="poc-overview",
            )
        ),
        dbc.CardBody(html.Div(id="card-content", className="card-text")),
    ]
)

content = html.Div(
    id = "page-content",
    children = [
        html.Div(
            id = "thermographs-content",
            className = "tabContent contentSelected",
            children = [
                html.Div([
                    html.H3("Demonstration of Thermographs using Python Dash"),
                    dbc.Row([
                        dbc.Col(
                            html.Div(
                                id = "thermograph-display",
                                children = [
                                    html.H4(id="objective_title"),
                                    dcc.Graph(id="objective_thermograph"),
                                    html.Div(id="metric_thermographs")
                                ]
                            ),
                            width = 7
                        ),
                        dbc.Col(
                            html.Div([
                                html.Div(card),
                                dcc.Graph(figure=gauge(13,45)),
                            ]),
                            width = 5
                        )
                    ])
                ])
            ]
        ),
        html.Div(
            id = "viewData-content",
            className = "tabContent",
            children = [
                html.H3("View the underlying data"),
                # The data table width is currently set by css. However, this doesnt display the ideal
                # layout. Dash has some documentation but I have yet to get any of there examples to work.
                dash_table.DataTable(
                    id='viewData-table',
                    style_data={
                        'whiteSpace': 'normal',
                        'height': 'auto'
                    },
                    columns=[{"name": i, "id": i} for i in df.columns],
                    page_current=0,
                    page_size=20,
                    page_action='custom',

                    sort_action='custom',
                    sort_mode='single',
                    sort_by=[]
                )
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
            className = "tabContent documentation",
            children = [
                "Guide thy user."
            ]
        ),
        html.Div(
            id = "readme-content",
            className = "tabContent documentation",
            children = [
                dcc.Markdown([
                    readme
                ])
            ]
        ),
        html.Div(
            id = "contributing-content",
            className = "tabContent documentation",
            children = [
                dcc.Markdown([
                    contributing
                ])
            ]
        )
    ]
)

mainbar = html.Div(
    id = "mainbar",
    children = [navbar, content]
)

app.layout = html.Div(
    id = "app-layout",
    children = [dcc.Location(id="url"), sidebar, mainbar]
)





# Server

@app.callback(
    Output("card-content", "children"), 
    [Input("card-tabs", "active_tab")]
)
def tab_content(active_tab):
    if active_tab == "poc-overview":
        return html.Div(
            id = "background_info",
            children = [
                html.P([
                    html.B("Background: "), "NGA is implementing a large scale effort to track the agency's progress against newly defined and rigourously tangible goals, objectives, and expected accomplishments.", html.Br(), html.Br(),
                    html.B("Purpose: "), "This demonstration looks at how to build a dynamic thermograph style capability with R Shiny. The thermographs include a gradient color bar with a quantitative scale (0 to 1 used in this demonstration). Visualization and layout will be generated through highly dynamic algorithms based on the given data.", html.Br(), html.Br(),
                    html.B("Overview of Methodology: "), "Construct a web application via R Shiny to create impactful dashboards while maintaining dynamic adaption of the given data.", html.Br(), html.Br(),
                    html.B("Metric Status: "), "Using the plotly package in R, the thermographs are created using a scatter plot trace as well as a contour trace for the hue background. The black triangle and blue circle represent the previous and current periods respectively. The data contained in the demo Excel file allows for the inclusion of associated data related to the metric such as related objective, the objective owner, the metric owner and changes since last reporting. Metric analysis can also be found under the Metric Analysis box, which gives insight to each metric, its description, and a further look at its progress.", html.Br(), html.Br(),
                    html.B("Objective Status: "), "Similar to the Metric Status this demonstration included an objective level that includes a weighted scoring of the objective's metrics.", html.Br(), html.Br(),
                    html.B("Web Application: "), "Creating a web application as the medium for the visualization gives the user a natural flow and feel while navigating the tool. In addition, it allows for unlimited extensibility and customization."
                ])
            ]
        )
    else:
        return "This is tab {}".format(active_tab)


@app.callback(
    Output("documentationSubmenu", "is_open"),
    [Input("documentation", "n_clicks")],
    [State("documentationSubmenu", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output('viewData-table', 'data'),
    [Input('viewData-table', "page_current"),
     Input('viewData-table', "page_size"),
     Input('viewData-table', 'sort_by')])
def update_table(page_current, page_size, sort_by):
    if len(sort_by):
        dff = df.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff = df

    return dff.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')

@app.callback(
    Output(component_id='objective_title', component_property='children'),
    [Input(component_id='objective_selection', component_property='value')]
)
def update_output_div(input_value):
    return input_value

@app.callback(
    Output(component_id='objective_thermograph', component_property='figure'),
    [Input(component_id='objective_selection', component_property='value')]
)
def update_output_div(input_value):
    return objectives["thermograph"+ input_value]

if __name__ == "__main__":
    app.run_server(port=8888, debug=True)