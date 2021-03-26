import streamlit as st
from energia import energy_global_pie


def geral(data_init,data_end,is_table,is_plot):
    energy_global_pie(data_init,data_end,is_table,is_plot)

