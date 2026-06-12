# 🌏 Religiomundo: El Hub Intercultural
### 🏫 CETis 64 - Cultura Digital II

¡Bienvenido al repositorio oficial del proyecto! Esta es una aplicación web interactiva desarrollada en Python orientada a la difusión cultural y el análisis de las grandes religiones del mundo.

---

## 👥 Integrantes del Equipo (Proyecto General)
* **Angelli Enríquez Nieto**
* **Osvaldo Peña González**
* **Melany Mariel Alvarado Colin**
* **Valeria Valdez Mendoza**
* **Eric Emanuel Yaxi Celaya**

---

## 🛠️ 1. Manual Técnico (Estructura del Código)

### 📚 Librerías Utilizadas
* **Streamlit (`st`):** Empleada para el diseño completo de la interfaz de usuario gráfica, manejo de pestañas, textos interactivos y componentes web.
* **Requests (`requests`):** Utilizada para realizar las peticiones HTTP externas y conectar de forma dinámica el chatbot con la API de inteligencia artificial.

### 🤖 Funcionamiento del Chatbot (Teo)
El sistema del chatbot opera bajo un modelo híbrido de contingencia:
1. **Flujo Principal:** El usuario ingresa una duda, el script procesa el texto mediante la función `preguntar_a_ia()` y realiza una consulta en tiempo real a una API externa (`pollinations.ai`).
2. **Flujo de Emergencia (Offline):** En caso de que el servidor externo falle o no haya internet en el laboratorio, el sistema activa de forma automática un bloque `try-except`. Este busca palabras clave dentro de un diccionario local (`respuestas_emergencia`) que contiene información estructurada sobre el Islam, Cristianismo y Judaísmo, garantizando que la aplicación nunca se quede colgada.

---

## 📖 2. Manual de Usuario (Instrucciones de Uso)

Para interactuar con la plataforma web, siga estos sencillos pasos:
1. **Sección de Inicio:** Visualice los datos de identificación del equipo o del estudiante y la introducción general del Hub Intercultural.
2. **Módulos de Aprendizaje:** Explore el contenido educativo estructurado mediante las herramientas de diseño integradas.
3. **Consulta al Asistente Virtual:** Diríjase al apartado del chatbot **Teo**, escriba su pregunta sobre las religiones analizadas en el cuadro de texto y presione Enter para recibir una respuesta inmediata.

---

## 🚀 3. Archivos del Repositorio y Versiones de Evaluación
Este repositorio aloja de manera limpia e independiente los scripts optimizados para la evaluación final:
* **`app.py`** (o el nombre de tu archivo grupal) -> Código fuente oficial del **Proyecto en Equipo**.
* **`osvaldo.py`** -> Código fuente de la entrega **Individual de Osvaldo Peña**.
* **`angelli.py`** -> Código fuente de la entrega **Individual de Angelli Enríquez**.
