import streamlit as st

"""
# Proyecto reparto
"""

"""Pruebas de slider"""

# Inicializar valores si no existen
if 'c1' not in st.session_state:
    st.session_state.c1 = 0
if 'c2' not in st.session_state:
    st.session_state.c2 = 0
if 'c3' not in st.session_state:
    st.session_state.c3 = 0

def ajustar_sliders(slider_modificado):
    total = st.session_state.c1 + st.session_state.c2 + st.session_state.c3

    if total > 100:
        exceso = total - 100

        # Identificar los otros dos sliders
        if slider_modificado == 'c1':
            otros = ['c2', 'c3']
        elif slider_modificado == 'c2':
            otros = ['c1', 'c3']
        else:  # c3
            otros = ['c1', 'c2']
        
        valor1 = st.session_state[otros[0]]
        valor2 = st.session_state[otros[1]]
        
        # Calcular reducción base (división entera)
        reduccion_base = exceso // 2  # Por ejemplo: 5//2 = 2
        resto = exceso % 2  # Por ejemplo: 5%2 = 1
        
        # Reducir ambos por la base
        reduccion1 = min(valor1, reduccion_base)
        reduccion2 = min(valor2, reduccion_base)
        
        # El resto lo absorbe el que más tiene
        if resto > 0:
            if valor1 - reduccion1 >= valor2 - reduccion2:
                reduccion1 += min(valor1 - reduccion1, resto)
            else:
                reduccion2 += min(valor2 - reduccion2, resto)
        
        st.session_state[otros[0]] = valor1 - reduccion1
        st.session_state[otros[1]] = valor2 - reduccion2


st.slider(
    "Criterio 1:",
    min_value=0,
    max_value=100,
    key='c1',
    on_change=ajustar_sliders,
    args=('c1',)
)

st.slider(
    "Criterio 2:",
    min_value=0,
    max_value=100,
    key='c2',
    on_change=ajustar_sliders,
    args=('c2',)
)

st.slider(
    "Criterio 3:",
    min_value=0,
    max_value=100,
    key='c3',
    on_change=ajustar_sliders,
    args=('c3',)
)
