import streamlit as st
import pandas as pd
import plotly.express as px

from desempleo.utils.data_utils import read_tabulado

st.set_page_config(layout="wide")

st.header("Semáforo de desempleo Nuevo León")

st.write("Esta visualización comprende los datos del último trimestre")

df = pd.read_csv("desempleo/data/descomposicion.csv", index_col=0)

desocupacion_df = df.loc[(df['L2'] == 'Población económicamente activa (PEA)') & (df['L3'].notna())]

main_column = st.columns([3,1,5,1])

columns = st.columns(2)

tabulado_df = read_tabulado()

with main_column[2]:

    st.subheader("Tasa de desocupación nacional")

    fig = px.sunburst(desocupacion_df, path=['L3', 'Sexo'], values='Total').update_traces(textinfo="label+percent parent").update_layout(height=900, width=700)

    st.plotly_chart(fig)

    st.subheader("Descomposición de desocupación")

with main_column[0]:

    st.subheader("Tasa de desocupación por estado")

    last_col = tabulado_df.columns.tolist()[-1]

    color_discrete_map = {state: 'blue' for state in tabulado_df.index}
    color_discrete_map['Media'] = 'red'

    fig = px.bar(tabulado_df, x = last_col, color=tabulado_df.index, color_discrete_map = color_discrete_map,).update_layout(height=900, width=500, xaxis_title='Indice de inflación', yaxis_title='Estado', showlegend=False).update_yaxes(categoryorder='total ascending')

    st.plotly_chart(fig)

with columns[0]:


    desempleo_df = df.loc[(df['L1'] == '7. Población desocupada por:') & (df['L3'].notna())]

    st.subheader("Por edad")

    desempleo_edad_df = desempleo_df.loc[desempleo_df['L2'] == '7.1 Grupos de edad']

    fig = px.pie(desempleo_edad_df, values='Total', names='L3').update_traces(textinfo="label+percent").update_layout(height=600)

    st.plotly_chart(fig)

with columns[1]:

    st.subheader("Por educación")

    desempleo_instruccion_df = desempleo_df.loc[desempleo_df['L2'] == '7.2 Nivel de instrucción']

    fig = px.pie(desempleo_instruccion_df, values='Total', names='L3').update_traces(textinfo="label+percent").update_layout(height=600)

    st.plotly_chart(fig)

with columns[0]:

    st.subheader("Por antecedentes")

    desempleo_antecedente_df = desempleo_df.loc[desempleo_df['L2'] == '7.3 Antecedente laboral']

    fig = px.pie(desempleo_antecedente_df, values='Total', names='L3').update_traces(textinfo="label+percent").update_layout(height=600)

    st.plotly_chart(fig)

with columns[1]:

    st.subheader("Por tiempo en desempleo")

    desempleo_duracion_df = desempleo_df.loc[desempleo_df['L2'] == '7.4 Duración del desempleo']

    fig = px.pie(desempleo_duracion_df, values='Total', names='L3').update_traces(textinfo="label+percent").update_layout(height=600)

    st.plotly_chart(fig)

foot_column = st.columns([3,5,1])

with foot_column[1]:

    st.subheader("Estructura laboral por salario")

    estructura_salario_df = df.loc[(df['L2'] == '3.3 Nivel de ingresos') & (df['L3'].notna())]

    fig = px.pie(estructura_salario_df, values='Total', names='L3').update_traces(textinfo="label+percent").update_layout(height=600)

    st.plotly_chart(fig)

tabulado_column = st.columns([2,5,1])

with tabulado_column[1]:

    st.header("Histórico de desempleo")

    tabulado_df_nacional = tabulado_df.loc[['Nuevo León', 'Media']]
    tabulado_df_nacional.index = ['Nuevo León', 'Media nacional']

    fig = px.line(tabulado_df_nacional.T).update_layout(width=800)

    st.plotly_chart(fig)
