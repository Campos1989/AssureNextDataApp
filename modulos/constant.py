# Módulo de valores constantes

# Imports
import pickle

# Constantes
APP_LOGO = "imagens/logo.jpg"
DATAFILE = "datasets/Desafio.xlsx"
ModeloSeguro = pickle.load(open('modelos/ModeloSeguro.sav', 'rb'))
modeloLucro = pickle.load(open('modelos/modeloLucro.sav', 'rb'))
ModeloMaquinas = pickle.load(open('modelos/ModeloMaquinas.sav', 'rb'))


# Formatação dos argumentos da barra lateral
SIDEBAR_STYLE = {"position": "fixed", 
                 "top": 0, 
                 "left": 0, 
                 "bottom": 0, 
                 "width": "15rem", 
                 "padding": "0rem 0rem",
                 "background-color": "dark"}

# Formatação dos itens de navegação
NAVITEM_STYLE = {"padding": "0rem 1rem"}

# Os estilos do conteúdo principal posicionam-no à direita da barra lateral e adicionamos um preenchimento.
CONTENT_STYLE = {"margin-left": "15rem", "padding": "0rem 0rem"}

