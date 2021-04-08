import streamlit as st

def intro():
    
    st.markdown('''
        Com vista à proteção ambiental e ao desenvolvimento sustentável, 
        a BA5 tem vindo a apostar num SGA que permite a eficácia na melhoria dos sistemas ambientais, 
        e que a conduziu, no ano de 2016, à certificação na norma EMAS, 
        tornando-se a primeira unidade de Defesa da União Europeia e do Espaço Económico Europeu a obter esta distinção. 
        Desta forma, tendo a necessidade de conciliar o cumprimento da missão que lhe está atribuída com a proteção do ambiente, 
        a BA5 promove mecanismos e ferramentas que incentivam a inovação e a aposta num modelo integrado de serviços, 
        que potencia sinergias entre as várias atividades desenvolvidas e o ambiente.

    ''')
    
    st.video('https://youtu.be/pUOXg3D8r7s')

    col1, col2, col3 = st.beta_columns([1,1,1])
    with col2:
        st.image('certificados.png')

    st.markdown('''
        ### Utilização do dashboard

        * Seleccione o descritor a analisar na barra lateral esquerda

        * Seleccione o intervalo pretendido

        * No campo "Configuração" seleccione opções extra de visualização

    ''')

    