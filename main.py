import streamlit as st
import plotly.graph_objects as go

"""
# Proyecto reparto
Lorem ipsum y algo más
"""

"""
## 1. Ponderación de criterios
"""
st.write("")

# Crear dos columnas con un espacio entre ellas
col1, col2 = st.columns([2, 3], gap="large")

# Columna izquierda: sliders
with col1:
    criterio_1 = st.slider(
        "Consumo",
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
        "Superficie",
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
        "Aportación",
        min_value=0,
        max_value=100-crit2,
        value=(0),
        disabled=bool(criterio_1==100) or bool(criterio_1 + criterio_2==100),
        help='tooltip c3'
    )


# Columna derecha: gráfico
with col2:
    labels = ['Consumo', 'Superficie', 'Aportación', 'sin usar']
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
## 2. Subir archivos
"""
csvs_consumos = st.file_uploader("Consumos ⚡",
                                type=['csv'],
                                accept_multiple_files=True,
                                disabled=not bool(criterio_1),
                                key='a')
if bool(csvs_consumos):
    from funciones import analisis_consumos
    st.write(f"{analisis_consumos(csvs_consumos)}")

csv_superficies = st.file_uploader("Superficies 🏠",
                                   type=['csv'],
                                   disabled=not bool(criterio_2),
                                   key='b')
if bool(csv_superficies):
    from funciones import analisis_superficies
    st.write(f"{analisis_superficies(csv_superficies)}")

csv_aportaciones = st.file_uploader("Aportaciones 💶",
                                    type=['csv'],
                                    disabled=not bool(criterio_3),
                                    key='c')
if bool(csv_aportaciones):
    from funciones import analisis_aportaciones
    st.write(f"{analisis_aportaciones(csv_aportaciones)}")

st.write("")
st.write("")

col1, col2, col3, col4 = st.columns([1,2,2,1])

with col2:
    if st.button("Generar archivo", type='primary', use_container_width=True):
        if criterio_1+criterio_2+criterio_3 != 100:
            st.error("La suma de porcentajes de los criterios debe ser 100")
        else:
            from funciones import generar_csv
            csv_final = generar_csv(csvs_consumos, csv_superficies, csv_aportaciones)
            st.session_state['csv_final'] = csv_final # Guardar en session_state para el download_button
            st.success('¡Archivo generado!')

with col3:
    st.download_button(
        label="Descargar CSV",
        data=st.session_state.get('csv_final'),
        file_name="resultado.csv",
        mime="text/csv",
        disabled=csv_final not in st.session_state,
        use_container_width=True
    )
