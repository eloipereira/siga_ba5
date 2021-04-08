import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import time
import shelve
from datetime import datetime
from passlib.hash import sha256_crypt
import energy 
import emissions
import water
import waste_water
import urban_waste
from intro import *


# Dashboard starts here

col1, col2 = st.beta_columns((1,5))
with col1:
    st.image('ba5brasao2712.png', use_column_width=True)
with col2:
    st.markdown('''
    # SIGA-BA5
    ## Sistema Integrado de Gestão Ambiental
    ''')

area = st.sidebar.radio('Seleccionar área:', ['Introdução', 'Energia', 'Emissões', 'Água', 'Água Residual', 'Resíduos', 'Floresta', 'Financiamento'])

today = datetime.today()
two_years_ago = datetime(today.year-2,today.month,today.day)

data_init = st.sidebar.date_input('Data inicial',value=two_years_ago)
data_end = st.sidebar.date_input('Data final',value=today)

with st.sidebar.beta_expander('Configuração'):
    is_table = st.checkbox('Mostrar tabelas?', value=False)
    is_plot = st.checkbox('Mostrar gráficos?', value=True)

st.markdown(f'### {area}')

if area == 'Energia':
    energy.total_pie(data_init,data_end,is_table,is_plot)
    energy.time_series(data_init,data_end,is_table,is_plot)

if area == 'Emissões':
    #emissions.total_pie(data_init,data_end,is_table,is_plot)
    emissions.time_series(data_init,data_end,is_table,is_plot)

if area == 'Água':
    water.total_pie(data_init,data_end,is_table,is_plot)
    water.time_series(data_init,data_end,is_table,is_plot)

if area == 'Água Residual':
    waste_water.time_series(data_init,data_end,is_table,is_plot)
    
if area == 'Resíduos':
    urban_waste.time_series(data_init,data_end,is_table,is_plot)

if area == 'Floresta':
    st.write("Em implementação...")

if area == 'Financiamento':
    st.write("Em implementação...")

if area == 'Introdução':
    intro()

