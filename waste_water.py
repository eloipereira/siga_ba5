import streamlit as st
import pandas as pd
import plotly.express as px
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

@st.cache()
def load_data(data_init,data_end):
    df = pd.read_csv(config['datasets']['waste_water'], index_col=0, parse_dates=True,dtype='float64')
    df = df.loc[data_init:data_end]
    df.index.name = 'Tempo/mês'
    df.rename(
        columns = {
            'waste_water_production': 'Água Residual produzida',
        }, inplace=True)
    return df


def time_series(data_init,data_end,is_table,is_plot):
    df = load_data(data_init,data_end)
    title = f'Volume de água residual tratada de {data_init} a {data_end}'
    if (df.size > 0):
        if is_plot:
            fig = px.area(df)
            fig.update_yaxes(
                title_text = "Água Residual/m3" 
            )
            fig.update_layout(
                title=dict(
                    text=title,
                    xanchor="center",
                    yanchor="top",
                    x=0.5,
                    y=0.93
                ),
                legend_title = '',
                legend=dict(
                    orientation="h",
                    yanchor="top",
                    xanchor="center",
                    x = 0.5,
                    y=-0.2,
                    itemwidth=40
                )
            )
            st.plotly_chart(fig)
        if is_table:
            st.dataframe(df.style.format("{:.2f}"))
    else: 
        st.write("Periodo sem dados.")
        
