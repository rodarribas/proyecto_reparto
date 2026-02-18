import streamlit as st
import base64

# Función para cargar la fuente
def load_font(font_path):
    with open(font_path, "rb") as f:
        font_data = base64.b64encode(f.read()).decode()
    return font_data

# Cargar las fuentes
outfit_regular = load_font("assets/fonts/Outfit-Regular.ttf")
outfit_bold = load_font("assets/fonts/Outfit-Bold.ttf")

# Aplicar CSS con selectores más amplios
st.markdown(f"""
    <style>
    @font-face {{
        font-family: 'Outfit';
        src: url(data:font/truetype;charset=utf-8;base64,{outfit_regular}) format('truetype');
        font-weight: 400;
    }}
    @font-face {{
        font-family: 'Outfit';
        src: url(data:font/truetype;charset=utf-8;base64,{outfit_bold}) format('truetype');
        font-weight: 700;
    }}
    
    /* Aplicar a TODO */
    html, body, [class*="css"], 
    h1, h2, h3, h4, h5, h6,
    p, div, span, label, button,
    .stMarkdown, .stText {{
        font-family: 'Outfit', sans-serif !important;
    }}
    </style>
    """, unsafe_allow_html=True)


st.image("assets/images/SomEnergia-Participa.png", use_container_width=True)

"""
# Proyecto reparto
Lorem ipsum y algo más
"""

"""
## 1. Ponderación de criterios
"""
st.write("")

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
        
        # Calcular cuánto necesitamos reducir en total
        total_disponible = valor1 + valor2
        
        if total_disponible >= exceso:
            # Hay suficiente para reducir proporcionalmente
            if total_disponible > 0:
                # Reducción proporcional
                reduccion1 = int((valor1 / total_disponible) * exceso)
                reduccion2 = exceso - reduccion1  # Asegurar que sume exacto
                
                st.session_state[otros[0]] = max(0, valor1 - reduccion1)
                st.session_state[otros[1]] = max(0, valor2 - reduccion2)
        else:
            # No hay suficiente, poner ambos a 0
            st.session_state[otros[0]] = 0
            st.session_state[otros[1]] = 0
            # Y ajustar el que se movió
            st.session_state[slider_modificado] = 100

criterio_1 = st.slider(
    "Criterio 1:",
    min_value=0,
    max_value=100,
    key='c1',
    on_change=ajustar_sliders,
    args=('c1',),
    help='tooltip 1'
)

criterio_2 = st.slider(
    "Criterio 2:",
    min_value=0,
    max_value=100,
    key='c2',
    on_change=ajustar_sliders,
    args=('c2',),
    help='tooltip 2'
)

criterio_3 = st.slider(
    "Criterio 3:",
    min_value=0,
    max_value=100,
    key='c3',
    on_change=ajustar_sliders,
    args=('c3',),
    help='tooltip 3'
)

col1, col2, col3 = st.columns([1.25,1,1.25])
with col2:
    st.write(f"Suma de criterios: {criterio_1+criterio_2+criterio_3}%")

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
    if 'csv_final' in st.session_state:
        st.download_button(
            label="Descargar CSV",
            data=st.session_state['csv_final'],
            file_name="resultado.csv",
            mime="text/csv",
            use_container_width=True
        )
    else:
        st.button(
            label="Descargar CSV",
            disabled=True,
            use_container_width=True
        )
