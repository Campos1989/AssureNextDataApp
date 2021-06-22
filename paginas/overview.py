# Script de criação do dashboard
# https://dash.plotly.com/dash-html-components

# Imports
import traceback
import pandas as pd
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

        # Carrega os dados
        firts = pd.read_excel(constant.DATAFILE, 'First')
        second = pd.read_excel(constant.DATAFILE,'Second')
        third = pd.read_excel(constant.DATAFILE,'Third')

        TotSeguro = firts['Total New Policies'].sum()
        TotMaquina = third['Machines_Installed'].sum()
        TotLucro = second['Value(Rs.)'].sum()

        TotVendasPlot = data_operations.TotVendasPlot(firts)
        TotLucroPlot = data_operations.TotLucroPlot(second)
        TotMaquinasPlot = data_operations.TotMaquinasPlot(third)
        TotMaquinasAnoPlot = data_operations.TotMaquinasAnoPlot(third)
       
    
        # Gera o container
        layout = dbc.Container([
                    dbc.Row([
                        dbc.Col([
                        dbc.Card([dbc.CardHeader("Total de Seguros Vendido"),
                              dbc.CardBody([html.H3(TotSeguro, className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 4),
                        dbc.Col([
                        dbc.Card([dbc.CardHeader("Total de Maquinas Instaladas"),
                              dbc.CardBody([html.H3(TotMaquina, className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 4),
                        dbc.Col([
                        dbc.Card([dbc.CardHeader("Total de Lucro Medio"),
                              dbc.CardBody([html.H3(TotLucro, className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 4)],
                        className= "pb-3"),
                   
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id = 'my-line', 
                                      figure = TotVendasPlot)
                        ],
                        width = 12)],
                    style = {'padding-bottom': '10px'},
                    no_gutters = True),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id = 'my-line2', 
                                      figure = TotMaquinasPlot)
                        ],
                        width = 12)],
                    style = {'padding-bottom': '10px'},
                    no_gutters = True),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id = 'my-box', 
                                      figure = TotLucroPlot)
                        ],
                        width = 6),
                        dbc.Col([
                            dcc.Graph(id = 'my-box2', 
                                      figure = TotMaquinasAnoPlot)
                        ],
                        width = 6)
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
