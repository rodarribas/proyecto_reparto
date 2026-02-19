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


st.image("assets/images/Cabecera_Linkedin.png", use_container_width=True)


"""
# Objetivo

Esta aplicación calcula qué porción de la energía generada en un proyecto de autoconsumo colectivo le corresponde a cada participante de una comunidad de energía renovable a partir de tres criterios como máximo:

- **Primer criterio**: el consumo eléctrico a cada hora de cada participante durante todo un año
- **Segundo criterio**: la aportación económica que cada participante haga al proyecto
- **Tercer criterio**: la superficie del inmueble destinatario de la energía generada

El usuario debe ponderar la importancia que concede a cada criterio mediante la asignación de un porcentaje. La suma de los porcentajes deberá ser 100%. Si el usuario no quisiera conceder ninguna importancia a alguno de los criterios, bastaría con asignarle una ponderación de 0%.

La inclusión de un número mayor de criterios apenas aportaría equidad al reparto.

Formalmente la "porción de energía" destinada a cada participante se denomina **coeficiente beta (β)**. La aplicación generará un fichero en el formato que exige la ley con tantos coeficientes β como horas tenga un año no bisiesto (8 760) por cada participante en el proyecto.

Existen plataformas específicas para gestionar íntegramente las comunidades de energía renovable, como [Somcomunitats](https://somcomunitats.coop/).

Utilícese la aplicación [Solidarenergia](https://solidarenergia.somenergia.coop/) (modo colectivo) quien quiera realizar una simulación de instalación fotovoltaica en una comunidad de propietarios.
"""

# Sección desplegable
with st.expander("📚 Más información"):
    st.markdown("""
        ### Contexto legal
        
        La creación de lo que comúnmente se entiende por comunidad energética local acarrea un sinfín de trámites y gestiones jurídicas, sociales y administrativas. Una de esas gestiones consiste en repartir la energía generada (los denominados **coeficientes β** según el Real Decreto 244/2019 sobre autoconsumo de energía eléctrica) entre los participantes mediante un fichero cuyo formato está descrito con precisión en el Anexo I del antedicho real decreto.
        
        Esta aplicación genera dicho fichero a partir de uno, dos o tres datos o variables como máximo de cada participante: su consumo eléctrico anual, la aportación económica al proyecto y superficie de su inmueble (las dos últimas variables podrían sustituirse por cualquiera otras que el usuario facilite mediante un fichero en el formato esperado: CSV).
        
        ### Denominaciones oficiales
        
        Existen dos denominaciones oficiales para las comunidades energéticas recogidas en la actualización de la Ley 24/2013 del Sector Eléctrico de cuya definición (ofrecida a continuación) se observa que deberían de carecer de afán de lucro y perseguir un beneficio medioambiental:
        
        **Comunidades de energías renovables:**
        
        «Son entidades jurídicas basadas en la participación abierta y voluntaria, autónomas y efectivamente controladas por socios o miembros que están situados en las proximidades de los proyectos de energías renovables que sean propiedad de dichas entidades jurídicas y que estas hayan desarrollado, cuyos socios o miembros sean personas físicas, pymes o autoridades locales, incluidos los municipios y cuya finalidad primordial sea proporcionar beneficios medioambientales, económicos o sociales a sus socios o miembros o a las zonas locales donde operan, en lugar de ganancias financieras».""")
    

"""
# Requisitos

Si se utilizaran los **consumos eléctricos** de los participantes (muy recomendable) para calcular los coeficientes β, será preciso descargar por cada participante un fichero con los consumos horarios de todo un año. Este fichero lo proporciona la empresa distribuidora de electricidad. Las instrucciones para obtener dicho fichero se pueden consultar en [este enlace](#).

Si se utilizaran las **aportaciones económicas** de los participantes para calcular los coeficientes β, el usuario deberá confeccionar un fichero con tantas filas como participantes haya en el proyecto. Cada fila responderá al formato siguiente:

- **CUPS**: el identificador de este suministro eléctrico
- **aportación**: la cantidad de capital (en euros) aportada al proyecto (preferiblemente sin decimales)

Si se utilizaran las **superficies de los inmuebles** de los participantes para calcular los coeficientes β, el usuario deberá confeccionar un fichero con tantas filas como participantes haya en el proyecto. Cada fila responderá al formato siguiente:

- **CUPS**: el identificador de este suministro eléctrico
- **superficie**: la cantidad en m² del inmueble del participante en el proyecto (preferiblemente sin decimales)

> **Nota:** Obsérvese que tanto el criterio 2 (aportaciones económicas) como el criterio 3 (superficie de los inmuebles) podrían ser otros que el usuario de la aplicación considerara más pertinentes para realizar el reparto. Lo importante es que se ajusten a los requisitos descritos.
"""

st.write("")

with st.expander("📋 Detalles técnicos"):
    st.markdown("""
    ### Formato del fichero de consumos
    
    El fichero facilitado por las compañías distribuidoras con el consumo eléctrico horario de todo un año comienza con una fila con el nombre de todos los campos que figurarán en las filas siguientes. Cada fila contendrá los consumos eléctricos de cada hora para este participante. Concretamente el formato empleado será:
    
    - **CUPS**: el identificador de este suministro eléctrico
    - **fecha**: día del año
    - **hora**: hora del día
    - **consumo**: kWh consumidos en esa hora
    - **método de obtención**: cómo se ha obtenido el consumo ('R' si se ha leído o 'E' si se ha estimado)
    
    Tanto el nombre de los campos como los valores para cada uno de esos campos están separados por `;`. Es lo que se conoce como formato **CSV** (comma separated values).
    
    ### Ejemplos de ficheros
    
    **Ejemplo 1:** Fichero CUPS proporcionado por UFD con cabeceras.
    
    **Ejemplo 2:** Fichero CUPS proporcionado por i-DE con cabeceras. Obsérvese que faltan los dos últimos caracteres del código CUPS.
    
    **Ejemplo 3:** Fichero con las aportaciones económicas (o las superficies en m²) de los participantes en el proyecto de autoconsumo.
    """)