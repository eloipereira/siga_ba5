import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache()
def load_data(data_init,data_end):
    renewal_ratio_nan = 0.5
    df = pd.read_csv('energy_data.csv', index_col=0, parse_dates=True,dtype='float64')
    df = df.loc[data_init:data_end]
    df['renewal_energy_purchased'].fillna(df['electric_energy_purchased']*renewal_ratio_nan,inplace=True)
    df['Não-renovável fornecida'] = df['electric_energy_purchased'] - df['renewal_energy_purchased']
    df.drop(columns = ['electric_energy_purchased'], inplace=True)
    df.index.name = 'Tempo/mês'
    df.rename(
        columns = {
            'renewal_energy_purchased': 'Renovável fornecida',
            'renewal_energy_produced': 'Renovável produzida'
        }, inplace=True)
    return df

def total_pie(data_init,data_end,is_table=False,is_plot=True):
    df = load_data(data_init,data_end)
    df_sum = pd.DataFrame()
    column_name = 'Energia/kWh'
    title = f'Balanço energético de {data_init} a {data_end}'
    df_sum[column_name] = df.sum()
    df_sum.index.name = 'Variável'
    if (df.size > 0): 
        if is_plot:
            fig = px.pie(df_sum,
                values=column_name,
                names=df_sum.index,
                color=df_sum.index
            )
            fig.update_layout(
                title=dict(
                    text=title,
                    xanchor="center",
                    yanchor="top",
                    x=0.5,
                    y=0.93
                ),
                legend=dict(
                    orientation="h",
                    yanchor="top",
                    xanchor="center",
                    x = 0.5,
                    y=-0.1,
                    itemwidth=40
                )
            )
            st.plotly_chart(fig)
        if is_table:
            st.dataframe(df_sum.style.format("{:.2f}"))
    else: 
        st.write("Periodo sem dados.")

def time_series(data_init,data_end,is_table,is_plot):
    df = load_data(data_init,data_end)
    title = f'Evolução energética de {data_init} a {data_end}'
    if (df.size > 0):
        if is_plot:
            fig = px.area(df)
            fig.update_yaxes(
                title_text = "Energia/kWh" 
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
