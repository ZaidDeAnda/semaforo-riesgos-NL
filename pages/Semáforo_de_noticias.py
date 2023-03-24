import pandas as pd

import streamlit as st

from noticias.utils.scrapper_utils import keywords

data = pd.read_csv("noticias/data/Noticias.csv")

topics = list(keywords.keys())

topics.insert(0, "Todos")

selection = st.selectbox(label='Seleccione tópico', options = topics)

if selection != "Todos":
    data = data.loc[data['cat'] == selection]

available_weeks = list(data['Periodo'].value_counts().index)

available_weeks.insert(0, "Todas")

selection_date = st.selectbox(label= 'Seleccione semana', options = available_weeks)

if selection_date != "Todas" :
    data = data.loc[data['Periodo'] == selection_date]

for i in range(10):
    row = data.iloc[i]
    cols = st.columns([4,2])
    cols[0].write(row['title'])
    link = f'[link]({row["url"]})'
    cols[0].markdown(link, unsafe_allow_html=True)
    st.markdown('---')

st.download_button(label="Descargar registro de noticias completo", data=pd.read_csv("noticias/data/Noticias.csv").to_csv().encode('utf-8'), file_name="Noticias.csv")