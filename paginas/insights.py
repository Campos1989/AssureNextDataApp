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
                        dbc.Card([dbc.CardHeader("Ano"),
                              dbc.CardBody([html.H5(data_operations.Ano2016, className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3),
                        dbc.Col([
                        dbc.Card([dbc.CardHeader("Seguros Previstos"),
                              dbc.CardBody([html.H5(data_operations.TotalNewPolicies2016, className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3),
                        dbc.Col([
                        dbc.Card([dbc.CardHeader("Maquinas Previstas"),
                              dbc.CardBody([html.H5(data_operations.MachinesInstalled2016, className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3),
                        dbc.Col([
                        dbc.Card([dbc.CardHeader("Lucro Medio"),
                              dbc.CardBody([html.H5(data_operations.LucroMedio2016, className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3)],
                        className= "pb-3"),
                    
                    dbc.Row([
                        dbc.Col([
                        dbc.Card([dbc.CardHeader("Ano"),
                              dbc.CardBody([html.H5(data_operations.Ano2017, className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3),
                        dbc.Col([
                        dbc.Card([dbc.CardHeader("Seguros Previstos"),
                              dbc.CardBody([html.H5(data_operations.TotalNewPolicies2017, className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3),
                        dbc.Col([
                        dbc.Card([dbc.CardHeader("Maquinas Previstas"),
                              dbc.CardBody([html.H5(data_operations.MachinesInstalled2017, className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3),
                        dbc.Col([
                        dbc.Card([dbc.CardHeader("Lucro Medio"),
                              dbc.CardBody([html.H5(data_operations.LucroMedio2017, className = "card-text")]),], className = "shadow p-3 bg-light rounded")], width = 3)],
                        className= "pb-3"),
                                      
                  dbc.Row([
                      dbc.Card([dbc.CardBody([html.H6("Na página visão geral temos o total de seguros vendidos, maquinas instaladas e lucro médio ao longo dos anos 2009 a 2015 nos cardes. No gráfico das contratações de seguros, percebe-se uma tendência, crescente de novas aquisições até o ano de 2013, depois uma leve queda entre os anos 2015 e 2016, porem algo interessante a se notar é que em todos os anos os picos de contratações ocorrem em março, seria interessante a empresa investigar o porquê. Em relação a instalação de máquinas seguem também um padrão quase constante, onde podemos notar picos de instalações maiores nos meses de dezembro. Embora nos últimos anos (2014,2015) a empresa tenho tido menos contratações, assim como instalações de máquinas, o seu lucro médio anual não caiu, aumenta a cada ano, isso mostra uma eficiência da empresa em manter clientes antigos.", className = "card-text")]),],className = "shadow p-3 bg-light rounded"),],
                        className= "pb-3"),

                  dbc.Row([
                      dbc.Card([dbc.CardBody([html.H6("Na página previsões, temos o primeiro gráfico mostrando as previsões (tendências) para aquisição de novas apólices, podemos ver as previsões do modelo para todos os anos, e os pontos pretos sendo os dados atuais, pode-se notar que o modelo fez um bom trabalho, levando em consideração que as previsões estão dentro da margem de erro que é a parte sombreada, já o segundo gráfico mostra apenas os valores para os anos a serem previstos. O mesmo ocorre nos gráficos 3 e 4, esses já com relação a instalações de novas maquinas. Com essas previsões os gestores podem se preparar para os próximos dois anos se baseando no que o modelo previu como tendência. ", className = "card-text")]),],className = "shadow p-3 bg-light rounded"),],
                        className= "pb-3"),

                    dbc.Row([
                      dbc.Card([dbc.CardBody([html.H6("Nessa página de insights, é mostrado resumidamente o total, de novas contratações e novas instalações de maquinas assim como o lucro médio dos anos previstos, todas as essas previsões com visto na página previsões seguem um padrão, identificado pelo modelo com relação aos anos anteriores, embora a previsão para novas contratações para 2017 não esteja tão alto, o lucro médio não caiu tanto, o modelo levou em consideração a tendência que vem ocorrendo em que a empresa tem uma boa qualidade de serviço fazendo com que os clientes antigos permaneçam com os serviços a cada ano. Todas as informações acima e os gráficos são valiosas, pois os gestores conseguem agora identificar padrões e possivelmente algumas falhas, e com isso entender o que pode vir a ocorrer, se manter o trabalho que vem feito, e até buscar melhorias para que atinja valores acima do previsto.", className = "card-text")]),],className = "shadow p-3 bg-light rounded"),],
                        className= "pb-3")
                
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
