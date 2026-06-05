import streamlit as st
import requests
st.set_page_config(page_title="Religiomundo - Angelli", page_icon="✨")
def preguntar_a_ia(pregunta_alumno):
    # Diccionario de respuestas rápidas por si el servidor externo falla
    respuestas_emergencia = {
        "islam": "El Islam es una religión monoteísta abrahámica basada en el Corán, el cual establece que no hay más dios que Alá y que Mahoma es su profeta. Sus cinco pilares incluyen la profesión de fe, la oración, la caridad, el ayuno y la peregrinación a La Meca.",
        "cristianismo": "El Cristianismo es una religión monoteísta abrahámica basada en la vida y enseñanzas de Jesús de Nazaret. Es la religión más grande del mundo y sus textos sagrados se recopilan en la Biblia.",
        "jesus": "Jesús de Nazaret es la figura central del Cristianismo, considerado por sus seguidores como el Hijo de Dios y el Mesías profetizado en el Antiguo Testamento.",
        "judaísmo": "El Judaísmo es la religión monoteísta más antigua de las tres grandes religiones abrahámicas. Su texto sagrado principal es la Torá y su historia se basa en el pacto entre Dios y Abraham."
    }
    
    # Intentar conectar con la IA normal
    try:
        url = f"https://text.pollinations.ai/{requests.utils.quote(pregunta_alumno)}?system=Eres un experto historiador en religiones del mundo. Responde de forma educativa, breve y respetuosa."
        respuesta = requests.get(url, timeout=5)
        
        if respuesta.status_code == 200:
            return respuesta.text
        else:
            # Si da error 429 o cualquier otro, buscar en las respuestas de emergencia
            for clave, texto in respuestas_emergencia.items():
                if clave in pregunta_alumno.lower():
                    return texto
            return "El servidor de IA está saturado en este momento. Intenta preguntar sobre 'Islam', 'Cristianismo' o 'Judaísmo', o reintenta en unos minutos."
            
    except:
        # En caso de que se quede sin internet por completo
        for clave, texto in respuestas_emergencia.items():
            if clave in pregunta_alumno.lower():
                return texto
        return "Conexión inestable. Por favor, intenta de nuevo en un momento."
# ==========================================
# 2. DISEÑO DE LA INTERFAZ
# ==========================================
st.markdown("# :violet[✨ Religiomundo: El Hub Intercultural]")
st.markdown("### :violet[🌟 Versión Individual: Angelli Enríquez]")
# 2. AQUÍ PEGA LA IMAGEN (Justo abajo de los títulos)
st.image(
    "https://elordenmundial.com/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/2021/08/portada-religiones-cristianismo-islam-judaismo-confucianismo-sintoismo.jpg.webp",
    caption="Las grandes religiones y filosofías del mundo",
    use_container_width=True
)
st.write("---") # Esto pone una línea divisoria muy estética

# --- SECCIÓN 1: PRESENTACIÓN DEL EQUIPO (Fase 3) ---
st.markdown("---")
st.header("🏠 Inicio y Presentación")
st.write("### Integrantes:")
sst.write("### ✨ Presentación Individual")
st.write("**Estudiante:** Angelli Enríquez Nieto")
st.write("**Escuela:** CETis 64")
st.write("**Materia:** Cultura Digital II")
st.write("**Maestra:** Concepción de la Luz Mendoza Mendoza")

# --- SECCIÓN 2: EL HUB INTERACTIVO (Fase 3) ---
st.markdown("---")
st.header("🤖 El Hub Interactivo (Chatbot Virtual)")
st.write("Escribe cualquier duda que tengas sobre festividades, libros sagrados o símbolos de alguna religión.")

pregunta_usuario = st.text_input("Escribe tu pregunta aquí (ej. ¿Qué es la Torá? o ¿Qué es el Islam?):")
boton_preguntar = st.button("Consultar al experto historiador")

if boton_preguntar:
    if pregunta_usuario.strip():
        with st.spinner("El historiador está consultando los archivos..."):
            respuesta_web = preguntar_a_ia(pregunta_usuario)
            st.success("¡Análisis completado!")
            st.write(respuesta_web)
    else:
        st.warning("Por favor, escribe una pregunta válida.")

# --- SECCIÓN 3: ENCICLOPEDIA FUNDAMENTAL (Fase 3) ---
st.markdown("---")
st.header("📚 Enciclopedia Fundamental de la Religión")
st.write("Explora los conceptos básicos indispensables para comprender la diversidad cultural de nuestro mundo:")

# Organizamos la información en columnas organizadas para que se vea estético
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📝 ¿Qué es la religión?
    La religión es un conjunto de **creencias, valores, prácticas y símbolos** compartidos por una comunidad. Por lo general, está ligada a la búsqueda de respuestas sobre el origen del universo, el sentido de la vida, la moralidad y lo sagrado o divino.
    
    ### 🎯 ¿Para qué sirve?
    * **Identidad y Comunidad:** Une a las personas mediante tradiciones, rituales y celebraciones comunes.
    * **Guía Moral:** Proporciona un marco ético (normas y valores) que orienta el comportamiento diario de sus seguidores.
    * **Consuelo Espiritual:** Ofrece respuestas y esperanza ante momentos difíciles o grandes misterios como la muerte.
    
    ### 🌍 ¿Cuántas religiones existen?
    Se estima que existen **más de 4,200 religiones vivas** en todo el mundo. Aunque la gran mayoría de la población mundial se agrupa en unas cuantas principales, la diversidad de pequeñas creencias indígenas y espiritualidades locales es inmensa.
    """)
    
with col2:
    st.markdown("""
    ### 📈 Las Religiones más Populares (Por número de seguidores)
    1. **Cristianismo:** Cerca de 2,400 millones de seguidores. Centrado en la vida y enseñanzas de Jesús de Nazaret.
    2. **Islam:** Alrededor de 1,900 millones de seguidores. Basado en las revelaciones del profeta Mahoma recopiladas en el Corán.
    3. **Hinduismo:** Cerca de 1,200 millones de personas. Una de las tradiciones espirituales continuas más antiguas, centrada en el Karma y el Dharma.
    4. **Budismo:** Más de 500 millones de practicantes. Enfocado en el desarrollo espiritual y mental propuesto por Siddhartha Gautama (Buda).
    
    ### 🤝 El valor del Respeto Intercultural
    En un mundo globalizado, conocer sobre otras religiones no busca cambiar nuestras creencias individuales, sino **derribar prejuicios, combatir la discriminación y fomentar la empatía**. La paz social empieza por comprender que cada cultura tiene una forma única y respetable de ver la existencia.
    """)

# --- SECCIÓN 4: TRIVIA INTERACTIVA (Fase 4: Gamificación) ---
st.markdown("---")
st.header("🎮 Trivia Religiomundo: ¡Pon a prueba tus conocimientos!")
st.write("Demuestra lo aprendido en nuestra enciclopedia respondiendo este reto interactivo. ¡Ideal para competir con tus compañeros de clase!")

# Banco de 8 preguntas corregido y ampliado
banco_preguntas = [
    {
        "pregunta": "¿Cuál es la religión con el mayor número de seguidores a nivel mundial?",
        "opciones": ["Islam", "Hinduismo", "Cristianismo", "Budismo"],
        "correcta": "Cristianismo"
    },
    {
        "pregunta": "¿Qué libro sagrado pertenece a la religión del Islam?",
        "opciones": ["La Torá", "El Corán", "La Biblia", "Los Vedas"],
        "correcta": "El Corán"
    },
    {
        "pregunta": "¿Qué concepto del Hinduismo se refiere a que nuestras acciones tienen consecuencias en la vida?",
        "opciones": ["Karma", "Shabat", "Ramadán", "Dharma"],
        "correcta": "Karma"
    },
    {
        "pregunta": "De acuerdo con los cálculos históricos, ¿aproximadamente cuántas religiones vivas existen en el mundo?",
        "opciones": ["Cerca de 100", "Alrededor de 1,500", "Más de 4,200", "Exactamente 500"],
        "correcta": "Más de 4,200"
    },
    {
        "pregunta": "¿Quién fue el fundador espiritual del Budismo, enfocado en el desarrollo mental y la paz?",
        "opciones": ["Mahoma", "Siddhartha Gautama", "Moisés", "Confucio"],
        "correcta": "Siddhartha Gautama"
    },
    {
        "pregunta": "¿Cuál es el principal propósito de fomentar el respeto intercultural según nuestro proyecto?",
        "opciones": ["Cambiar de religión", "Derribar prejuicios y fomentar la empatía", "Aprender idiomas", "Viajar por el mundo"],
        "correcta": "Derribar prejuicios y fomentar la empatía"
    },
    {
        "pregunta": "¿Qué día de la semana es considerado sagrado para el descanso espiritual en el Judaísmo (llamado Shabat)?",
        "opciones": ["Lunes", "Miércoles", "Sábado", "Viernes"],
        "correcta": "Sábado"
    },
    {
        "pregunta": "¿Qué elemento es compartido comúnmente por casi todas las religiones del mundo?",
        "opciones": ["El mismo idioma", "Tener los mismos templos", "Creencias, valores, prácticas y símbolos", "Celebrar las mismas fechas"],
        "correcta": "Creencias, valores, prácticas y símbolos"
    }
]

# Inicializamos las variables de memoria interna de Streamlit del primer modelo lógico
if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0
if "puntos" not in st.session_state:
    st.session_state.puntos = 0
if "respondido" not in st.session_state:
    st.session_state.respondido = False
if "mensaje_resultado" not in st.session_state:
    st.session_state.mensaje_resultado = ""

# Verificar si el juego sigue activo
if st.session_state.pregunta_actual < len(banco_preguntas):
    datos_trivia = banco_preguntas[st.session_state.pregunta_actual]
    
    st.subheader(f"Pregunta {st.session_state.pregunta_actual + 1} de {len(banco_preguntas)}")
    st.write(f"### {datos_trivia['pregunta']}")
    
    # Mostrar los botones de respuestas de forma organizada en 2 columnas
    col_a, col_b = st.columns(2)
    
    for i, opcion in enumerate(datos_trivia["opciones"]):
        target_col = col_a if i % 2 == 0 else col_b
        
        # Al dar clic, el sistema del primer código procesa todo directo e instantáneo
        if target_col.button(opcion, key=f"btn_{st.session_state.pregunta_actual}_{i}", use_container_width=True, disabled=st.session_state.respondido):
            st.session_state.respondido = True
            if opcion == datos_trivia["correcta"]:
                st.session_state.puntos += 10
                st.session_state.mensaje_resultado = f"🎉 ¡Excelente! **{opcion}** es la respuesta correcta. (+10 puntos)"
            else:
                st.session_state.mensaje_resultado = f"❌ Incorrecto. La respuesta correcta era **{datos_trivia['correcta']}**."
            st.rerun()

    # Mostrar la alerta abajo de los botones
    if st.session_state.respondido:
        if "🎉" in st.session_state.mensaje_resultado:
            st.success(st.session_state.mensaje_resultado)
        else:
            st.error(st.session_state.mensaje_resultado)
            
        # Botón para pasar a la siguiente pregunta
        if st.button("Siguiente pregunta ➡️"):
            st.session_state.pregunta_actual += 1
            st.session_state.respondido = False
            st.session_state.mensaje_resultado = ""
            st.rerun()

else:
    # Pantalla final al terminar las 8 preguntas
    st.balloons()
    st.success(f"## 🏆 ¡Trivia Completada!")
    st.write(f"### Tu puntuación final es de: **{st.session_state.puntos} de 80 puntos posibles**")
    
    if st.session_state.puntos == 80:
        st.write("🥇 ¡Puntuación perfecta! Eres todo un experto historiador en religiones.")
    elif st.session_state.puntos >= 50:
        st.write("🥈 ¡Muy buen trabajo! Tienes un gran conocimiento intercultural.")
    else:
        st.write("📚 ¡Sigue practicando! Puedes leer la enciclopedia de arriba y volver a intentarlo.")

    # Botón para reiniciar todo el ciclo
    if st.button("🔄 Volver a jugar"):
        st.session_state.pregunta_actual = 0
        st.session_state.puntos = 0
        st.session_state.respondido = False
        st.session_state.mensaje_resultado = ""
        st.rerun()

# LA BARRA LATERAL: Muestra los puntos flotantes a la izquierda en tiempo real durante todo el juego
st.sidebar.metric(label="Score de la Trivia 🎯", value=f"{st.session_state.puntos} pts")