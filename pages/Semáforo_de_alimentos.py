import streamlit as st

import plotly.express as px

from alimentos.utils.data_utils import calculate_ratio
from alimentos.utils.data_utils import read_historical
from noticias.utils.months import months

st.set_page_config(layout="wide")

st.header('Precios promedio de los alimentos.')

try:
    ratios_df, comparison_month, top_6_items = calculate_ratio()

    st.subheader(f'Comparación realizada del mes {months[comparison_month]} del presente año contra el año pasado')

    title_column = st.columns([3,3,5])

    title_column[2].subheader("Alimentos con más tasa de inflación")

    columns = st.columns([1,4,1,1,1,1])

    historical_df = read_historical()

    fig = px.line(historical_df.loc[['Resumen nacional', 'Monterrey N.L.']].T).update_layout(height=700, width=600, xaxis_title="Fecha", yaxis_title="Porcentaje", legend_title="ciudad")

    columns[1].subheader('Histórico de porcentaje de inflación respecto al año pasado')
    columns[1].plotly_chart(fig)

    keys = list(top_6_items.keys())
    for j in range(2):
        for i, column in enumerate(columns[2:-1]):
            column.write(keys[i+(3*j)])
            column.write(f'Ratio de inflación = {int(top_6_items[keys[i+(3*j)]]["ratio"])}%')
            column.image(f'{top_6_items[keys[i+(3*j)]]["url"]}')

    fig = px.bar(ratios_df, x='ratio', y = ratios_df.index, color = 'Nombre ciudad', color_continuous_scale=['green', 'yellow', 'red'], barmode='group',hover_data=ratios_df.columns.tolist())

    updated_text = [f'{round(val, 1)}%' for val in ratios_df['ratio']]

    fig.update_traces(text = updated_text)

    fig.update_yaxes(autorange='reversed')

    fig.update_layout(
            {
                "height" : 1000,
                "width" : 1300,
                "xaxis_title" : "Porcentaje",
                "yaxis_title" : "Alimento",
                "legend_title_text" : "Ciudad"
            }
        )
    
    columns[1].subheader("Desglose del ratio de inflación de todos los grupos de alimentos")

    columns[1].plotly_chart(fig)
    
except Exception as e:
    print(e)
    st.write('Obteniendo nuevos datos, espere por favor ⚙')
