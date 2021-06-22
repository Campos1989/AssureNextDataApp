# Arquivo principal do nosso programa

# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Carrega o arquivo de conexão da app
from app import app
from app import server

# Conecta aos módulos de páginas e outros módulos
from paginas import overview,forecast, insights
from modulos import navbar, constant

# Conteúdo principal
content = html.Div(id = "page-content", style = constant.CONTENT_STYLE, className = "p-3 pt-4 pb-3")

# Layout
app.layout = html.Div([dcc.Location(id = "url"), navbar.layout, content])

# Callback
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/paginas/overview' or pathname == '/':
        return overview.get_layout()
    elif pathname == '/paginas/forecast':
        return forecast.get_layout()
    elif pathname == '/paginas/insights':
        return insights.get_layout()
    else:
        return dbc.Jumbotron(
            [
                html.Div([
                    html.H1("404: Not found", className = "text-danger"),
                    html.Hr(),
                    html.P(f"Pagina {pathname} não encontrada...")
                ],
                style = constant.NAVITEM_STYLE)
            ]
       )

# Título
app.title = 'Data App - Dashboard Analítico Interativo - AssureNext '

#  Executa o programa
if __name__ == '__main__':
    app.run_server(debug = False,port = 4000, host = '0.0.0.0', threaded = True)


