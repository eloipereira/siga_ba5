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


def login(user,pw):
    if user in db:
        if sha256_crypt.verify(pw,db[user]):
            db['logged'] = True
            return True
    return False

def register(user,pw):
    db[user] = sha256_crypt.hash(pw)
    return True

# Dashboard starts here

st.title("SIGA-BA5")
st.header("Sistema Integrado de Gestão Ambiental da BA5")

user_input = st.empty()
pw_input = st.empty()
login_btn = st.empty()

with shelve.open('auth') as db:
    register('admin','admin')
    if 'logged' not in db:
        db['logged'] = False
    if not db['logged']:
        user = user_input.text_input('Username')
        pw = pw_input.text_input('Password',type='password')
        if login_btn.button('Login'):
            logged_in = login(user,pw)
            if(logged_in):
                db['current_user'] = user
                st.success("Login successful")
            else:
                st.error("Invalid credentials")
        else:
            st.stop()

    user_input.empty()
    pw_input.empty()
    login_btn.empty()

    current_user = db['current_user']
    
    area = st.sidebar.radio('Seleccionar área:', ['Geral', 'Energia', 'Emissões', 'Floresta', 'Financiamento', 'Info'])

    today = datetime.today()
    two_years_ago = datetime(today.year-2,today.month,today.day)

    data_init = st.sidebar.date_input('Data inicial',value=two_years_ago)
    data_end = st.sidebar.date_input('Data final',value=today)

    st.subheader(f'Olá {current_user}!')

    with st.sidebar.beta_expander('Configuration'):
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

