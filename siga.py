import streamlit as st
import pandas as pd
import datetime
import time
import shelve
from passlib.hash import sha256_crypt

def login(user,pw,db):
    if user in db:
        if sha256_crypt.verify(db[user], pw):
            db['logged'] = True
            return True
    return False

def register(user,pw,db):
    db[user] = sha256_crypt.hash(pw)
    return True

# Dashboard starts here

st.title("SIGA-BA5")
st.header("Sistema Integrado de Gestão Ambiental da BA5")

with shelve.open('auth') as db:
    register('admin','admin',db)
    #if 'logged' in db:
    db['logged'] = False
    if not db['logged']:
        user = st.text_input('Username')
        pw = st.text_input('Password',type='password')
        if st.button('Login'):
            logged_in = login(user,pw,db)
            if(logged_in):
                db['current_user'] = user
                st.success("Login successful")
            else:
                st.error("Invalid credentials")
    else:
        st.subheader(f'Olá {user}')

area = st.sidebar.selectbox('Seleccionar área:', ['Geral', 'Energia', 'Pegada', 'Floresta', 'Financiamento', 'R&D'])
data_init = st.sidebar.date_input('Data inicial')
st.sidebar.date_input('Data final')
if st.sidebar.checkbox('Configuração'):
    st.sidebar.radio('Mostrar tabelas?', [True,False])
    st.sidebar.radio('Mostrar gráficos?', [True,False])

if area == 'Geral':
    sliding = st.slider('select',0,100,step = 1)
    st.write(data_init + datetime.timedelta(days=sliding))
    st.select_slider('select me',[1,2,3])
    st.time_input('my time')
    st.spinner()
    time.sleep(5)


if area == 'Energia':
    st.empty()

if area == 'Pegada':
    st.empty()

if area == 'Financiamento':
    st.empty()

if area == 'R&D':
    st.empty()

