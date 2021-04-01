import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import time
import shelve
from datetime import datetime
from passlib.hash import sha256_crypt
from geral import *
from energia import *
from intro import *


# Dashboard starts here

st.title("SIGA-BA5")
st.header("Sistema Integrado de Gestão Ambiental da BA5")
    
area = st.sidebar.radio('Seleccionar área:', ['Geral', 'Energia', 'Emissões', 'Floresta', 'Financiamento', 'Info'])

today = datetime.today()
two_years_ago = datetime(today.year-2,today.month,today.day)

data_init = st.sidebar.date_input('Data inicial',value=two_years_ago)
data_end = st.sidebar.date_input('Data final',value=today)

with st.sidebar.beta_expander('Configuração'):
    is_table = st.checkbox('Mostrar tabelas?', value=False)
    is_plot = st.checkbox('Mostrar gráficos?', value=True)

if area == 'Geral':
    geral(data_init,data_end,is_table,is_plot)

if area == 'Energia':
    energy_global_pie(data_init,data_end,is_table,is_plot)
    energy_global(data_init,data_end,is_table,is_plot)

if area == 'Emissões':
    st.empty()

if area == 'Financiamento':
    st.empty()

if area == 'Info':
    intro()

