# Módulo para carga dos dados

# Imports
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from fbprophet import Prophet
from sklearn.ensemble import RandomForestRegressor
from fbprophet.plot import plot_plotly
import datetime
from modulos import constant


# Carregando as Sheets



# Tratamento e criação de variáveis e graficos pagina Visão Geral 

# Total de Seguros por periodo
def TotVendasPlot(dados):
    # Faço o Agrupamento
    TotSegurosPer = dados.groupby('Business_Sourcing_Month')['Total New Policies'].sum().reset_index()

    # Cria a figura
    fig = go.Figure(data = go.Scatter(x = TotSegurosPer['Business_Sourcing_Month'],
                                      y = TotSegurosPer['Total New Policies'],
                                      mode = 'lines'))

    # Layout
    fig.update_layout(title = 'Quantidade de Seguros Vendido entre 2009/2015 ',
                      xaxis_title = "Data",
                      yaxis_title = "Número de Seguros")
    return fig    


# Total de Lucro por Ano
def TotLucroPlot(dados):

    # Cria a figura
    fig = go.Figure(go.Bar(x = dados['Year'], y = dados['Value(Rs.)'],))

    # Configura o layout
    fig.update_layout(title_text = 'Lucro Medio Por Ano',
                      xaxis_title = "Ano",
                      yaxis_title = "Lucro")
    return fig
     

# Maquinas instaladas por perido 
def TotMaquinasPlot(dados):

    # Cria a figura
    fig = go.Figure(data = go.Scatter(x = dados['Month'],
                                      y = dados['Machines_Installed'],
                                      mode = 'lines'))
    # Layout
    fig.update_layout(title = 'Quantidade de Maquinas Instaladas entre 2009/2015 ',
                      xaxis_title = "Data",
                          yaxis_title = "Quantidade de Maquinas")
    return fig






 # Maquinas instaladas por Ano
def TotMaquinasAnoPlot(dados):
    # Extraio o ano
    TotMachineYear = dados.copy()
    TotMachineYear['Year'] = TotMachineYear['Month'].dt.year

    #Faço o Agrupamento
    TotMachineYear = TotMachineYear.groupby('Year')['Machines_Installed'].sum().reset_index()

    # Cria a figura
    fig = go.Figure(go.Bar(x = TotMachineYear['Year'], y = TotMachineYear['Machines_Installed'],))

    # Configura o layout
    fig.update_layout(title_text = 'Total de Maquinas Instaladas Por Ano',
                              xaxis_title = "Ano",
                              yaxis_title = "Maquinas")
    return fig

        


#### ----- Tratamento e criação de variáveis e graficos pagina Previsões ----- ####  

# Previsão Seguro 
# Previsões de 2 anos 
periodo = 24
# Crios as datas de 2 anos futuros
futuroSeguro = constant.ModeloSeguro.make_future_dataframe(periods = periodo,freq = 'MS')
# Previsões
previsaoSeguro = constant.ModeloSeguro.predict(futuroSeguro)
# Grafico das Previsões comparando com os dados reais. 
PrevSeguro = plot_plotly(constant.ModeloSeguro, previsaoSeguro)
# Layout
PrevSeguro.update_layout(title = 'Previsão de Novas Contratações de Seguro ',
                  xaxis_title = "Data",
                  yaxis_title = "Número de Seguros")


# Grafico apenas com as previsões de novas apólices
novosSeguros = previsaoSeguro[['ds','yhat']]
novosSeguros = novosSeguros.rename(columns = {'ds':'Business_Sourcing_Month','yhat':'Total New Policies'})
novosSeguros['Total New Policies'] = novosSeguros['Total New Policies'].astype(int)
novosSeguros['Year'] = novosSeguros['Business_Sourcing_Month'].dt.year
novosSeguros = novosSeguros.set_index('Year')
novosSeguros = novosSeguros.loc[2016:2017:]

# Cria a figura
PrevSeguro2 = go.Figure(data = go.Scatter(x = novosSeguros['Business_Sourcing_Month'],
                                  y = novosSeguros['Total New Policies'],
                                  mode = 'lines'))

# Layout
PrevSeguro2.update_layout(title = 'Contratações de Seguro Previsto',
                  xaxis_title = "Data",
                  yaxis_title = "Número de Seguros")





# Previsão Maquinas
# Crios as datas de 2 anos futuros
futuroMaquina = constant.ModeloMaquinas.make_future_dataframe(periods = periodo,freq = 'MS')
# Previsões
previsaoMaquina = constant.ModeloMaquinas.predict(futuroMaquina)
# Grafico das Previsões comparando com os dados reais. 
PrevMaquina = plot_plotly(constant.ModeloMaquinas, previsaoMaquina)
# Layout
PrevMaquina.update_layout(title = 'Previsão de Novas Instalações de Máquinas',
                  xaxis_title = "Data",
                  yaxis_title =  "Número de Máquinas")

# Grafico apenas com as previsões de Novas Instalações de Maquinas
novasMaquinas = previsaoMaquina[['ds','yhat']]
novasMaquinas = novasMaquinas.rename(columns = {'ds':'Month','yhat':'Machines_Installed'})
novasMaquinas['Machines_Installed'] = novasMaquinas['Machines_Installed'].astype(int)
novasMaquinas['Year'] = novasMaquinas['Month'].dt.year
novasMaquinas = novasMaquinas.set_index('Year')
novasMaquinas = novasMaquinas.loc[2016:2017:]

# Cria a figura
PrevMaquina2 = go.Figure(data = go.Scatter(x = novasMaquinas['Month'],
                                  y = novasMaquinas['Machines_Installed'],
                                  mode = 'lines'))

# Layout
PrevMaquina2.update_layout(title = 'Instalações de Maquinas Prevista',
                  xaxis_title = "Data",
                  yaxis_title = "Número de Maquinas")



#### -----  Tratamento e criação de variáveis e graficos pagina Insights ----- ####  



# Total por ano previsto de novas contratações de seguro 
novosSegurosAno = novosSeguros.copy()
novosSegurosAno = novosSegurosAno.reset_index().groupby('Year')['Total New Policies'].sum().reset_index()

# Total por ano previsto de novas Instalações
novasMaquinasAno = novasMaquinas.copy()
novasMaquinasAno = novasMaquinasAno.reset_index().groupby('Year')['Machines_Installed'].sum().reset_index()


# Previsão Lucro Medio 2016/2017

# Carregando o modelo 
# Preparando os dados novos para o modelo 
previsaoLucro = novosSegurosAno.merge(novasMaquinasAno,how='inner', on='Year')
values_prev = previsaoLucro.values
prevfinal = constant.modeloLucro.predict(values_prev)
prevfinal = prevfinal.astype(int)
previsaoLucro['Value(Rs.)'] = prevfinal

# 2016
Ano2016 = previsaoLucro['Year'][0]
TotalNewPolicies2016 = previsaoLucro['Total New Policies'][0]
MachinesInstalled2016 = previsaoLucro['Machines_Installed'][0]
LucroMedio2016 = previsaoLucro['Value(Rs.)'][0]

# 2017
Ano2017 = previsaoLucro['Year'][1]
TotalNewPolicies2017 = previsaoLucro['Total New Policies'][1]
MachinesInstalled2017 = previsaoLucro['Machines_Installed'][1]
LucroMedio2017 = previsaoLucro['Value(Rs.)'][1]