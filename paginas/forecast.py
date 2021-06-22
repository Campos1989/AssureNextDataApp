# Script de criação do dashboard
# https://dash.plotly.com/dash-html-components

# Imports
import traceback
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

# Módulos customizados
from app import app
from modulos import data_operations, constant

# Gera o layout
def get_layout():

    try:

        # Gera o container
        layout = dbc.Container([
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id = 'my-line', 
                                      figure = data_operations.PrevSeguro,responsive = True)
                        ],
                        width = 12)
                    ],
                    style = {'padding-bottom': '10px'},
                    no_gutters = True),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id = 'my-line2', 
                                      figure = data_operations.PrevSeguro2)
                        ],
                        width = 12)
                    ],
                    style = {'padding-bottom': '10px'},
                    no_gutters = True),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id = 'my-line3', 
                                      figure = data_operations.PrevMaquina,responsive = True)
                        ],
                        width = 12)
                    ],
                    style = {'padding-bottom': '10px'},
                    no_gutters = True),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id = 'my-line4', 
                                      figure = data_operations.PrevMaquina2)
                        ],
                        width = 12)
                    ],
                    style = {'padding-bottom': '10px'},
                    no_gutters = True)             
                   
                ],
                fluid = True)
        return layout
    except:
        layout = dbc.Jumbotron(
                    [
                        html.Div([
                            html.H1("500: Internal Server Error", className = "text-danger"),
                            html.Hr(),
                            html.P(f"Following Exception Occured: "),
                            html.Code(traceback.format_exc())
                        ],
                        style = constant.NAVITEM_STYLE)
                    ]
                )
        return layout

