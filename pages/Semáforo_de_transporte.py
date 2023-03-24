import streamlit as st

import plotly.express as px

from alimentos.utils.data_utils import calculate_ratio
from noticias.utils.months import months

st.header('Precios promedio del transporte.')

try:

    ratios_df, comparison_month, _ = calculate_ratio("transporte")

    st.subheader(f'Comparación realizada del mes {months[comparison_month]} del presente año contra el año pasado')

    fig = px.bar(ratios_df, x='ratio', y = ratios_df.index, color = 'Nombre ciudad', barmode='group',hover_data=ratios_df.columns.tolist())

    updated_text = [f'{round(val, 1)}%' for val in ratios_df['ratio']]

    fig.update_traces(text = updated_text)

    fig.update_yaxes(autorange='reversed')

    fig.update_layout(
            {
                "height" : 1000,
                "width" : 900,
                "xaxis_title" : "Porcentaje",
                "yaxis_title" : "Transporte",
                "legend_title_text" : "Ciudad"
            }
        )

    st.plotly_chart(fig)
    
except Exception as e:
    print(e)
    st.write('Obteniendo nuevos datos, espere por favor ⚙')
