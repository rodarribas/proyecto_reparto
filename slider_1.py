import streamlit as st

"""
# Proyecto reparto
"""

"""Pruebas de slider"""

# Slider
criterios = st.slider(
    "Selecciona la magnitud de los criterios:",
    min_value=0,
    max_value=100,
    value=(25, 75),
    format=''
)

criterio_1 = criterios[0]
criterio_2 = criterios[1] - criterio_1
criterio_3 = 100 - (criterio_1 + criterio_2)

st.write("Criterios seleccionados:")
st.write(f"Criterio 1: {criterio_1}%")
st.file_uploader("Subir consumos",
                 disabled=not bool(criterio_1))
st.write(f"Criterio 2: {criterio_2}%")
st.file_uploader("Subir aportaciones",
                 disabled=not bool(criterio_2))
st.write(f"Criterio 3: {criterio_3}%")
st.file_uploader("Subir superficies",
                 disabled=not bool(criterio_3))


