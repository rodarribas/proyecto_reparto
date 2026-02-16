import streamlit as st
import plotly.graph_objects as go

"""
# Proyecto reparto
"""

"""Pruebas de slider"""

# Crear dos columnas con un espacio entre ellas
col1, col2 = st.columns([2, 3], gap="large")  # gap="large" añade más espacio

# Columna izquierda: sliders
with col1:
    criterio_1 = st.slider(
        "Criterio 1:",
        min_value=0,
        max_value=100,
        value=(0),
        key='key1'
    )

    if criterio_1 == 100:
        crit1 = 1
    else: crit1 = criterio_1

    criterio_2 = st.slider(
        "Criterio 2:",
        min_value=0,
        max_value=100-crit1,
        value=(0),
        disabled=bool(criterio_1==100)
    )

    if criterio_1 + criterio_2 == 100:
        crit2 = 1
    else: crit2 = criterio_1 + criterio_2

    criterio_3 = st.slider(
        "Criterio 3:",
        min_value=0,
        max_value=100-crit2,
        value=(0),
        disabled=bool(criterio_1==100) or bool(criterio_1 + criterio_2==100)
    )

# Columna derecha: gráfico
with col2:
    labels = ['C1', 'C2', 'C3', 'sin usar']
    values = [criterio_1, criterio_2, criterio_3, 100-criterio_1-criterio_2-criterio_3]
    colors = ['#FF6B6B', '#FFA500', '#FFE66D', '#949494']

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
