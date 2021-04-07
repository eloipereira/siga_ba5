import streamlit as st

def intro():
    col1, col2 = st.beta_columns((1,2))
    with col1:
        st.image('ba5brasao2712.png', width=150)
    with col2:
       st.image('certificados.png', use_column_width=False)
    st.write('Com vista à proteção ambiental e ao desenvolvimento sustentável, a BA5 tem vindo a apostar num SGA que permite a eficácia na melhoria dos sistemas ambientais, e que a conduziu, no ano de 2016, à certificação na norma EMAS, tornando-se a primeira unidade de Defesa da União Europeia e do Espaço Económico Europeu a obter esta distinção. Desta forma, tendo a necessidade de conciliar o cumprimento da missão que lhe está atribuída com a proteção do ambiente, a BA5 promove mecanismos e ferramentas que incentivam a inovação e a aposta num modelo integrado de serviços, que potencia sinergias entre as várias atividades desenvolvidas e o ambiente.')
    st.video('https://youtu.be/i9i4W-H8wnQ')