import streamlit as st
import plotly.graph_objects as go

"""
# Proyecto reparto
"""

"""Ponderación de criterios"""

# Crear dos columnas con un espacio entre ellas
col1, col2 = st.columns([2, 3], gap="large")  # gap="large" añade más espacio

# Columna izquierda: sliders
with col1:
    criterio_1 = st.slider(
        "Criterio 1:",
        min_value=0,
        max_value=100,
        value=(0),
        key='key1',
        help='tooltip c1'
    )

    if criterio_1 == 100:
        crit1 = 1
    else: crit1 = criterio_1

    criterio_2 = st.slider(
        "Criterio 2:",
        min_value=0,
        max_value=100-crit1,
        value=(0),
        disabled=bool(criterio_1==100),
        help='tooltip c2'
    )

    if criterio_1 + criterio_2 == 100:
        crit2 = 1
    else: crit2 = criterio_1 + criterio_2

    criterio_3 = st.slider(
        "Criterio 3:",
        min_value=0,
        max_value=100-crit2,
        value=(0),
        disabled=bool(criterio_1==100) or bool(criterio_1 + criterio_2==100),
        help='tooltip c3'
    )


# Columna derecha: gráfico
with col2:
    labels = ['C1', 'C2', 'C3', 'sin usar']
    values = [criterio_1, criterio_2, criterio_3, 100-criterio_1-criterio_2-criterio_3]
    colors = ["#F7FF05", '#FFA500', "#BAF17F", '#949494']

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=colors),
        sort=False
    )])
    
    # Ajustar márgenes del gráfico
    fig.update_layout(
        margin=dict(t=0, b=0, l=0, r=0),  # Elimina márgenes superiores
        height=300  # Ajusta la altura si es necesario
    )

    st.plotly_chart(fig, use_container_width=True)

"""
## Subir archivos
"""
st.file_uploader("Consumos ⚡", disabled=not bool(criterio_1), key='a')
st.file_uploader("Superficies 🏠", disabled=not bool(criterio_2), key='b')
st.file_uploader("Aportaciones 💶", disabled=not bool(criterio_3), key='c')

st.write("")
st.write("")

col1, col2, col3 = st.columns([2,1,2])

with col2:
    if st.button("Enviar",
                 use_container_width=True):
        st.write("yeeey")
