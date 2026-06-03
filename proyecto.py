
import google.generativeai as genai
import sys

# ==========================================
# 1. CONFIGURACIÓN DE LA LLAVE SECRETA (API)
# ==========================================
# Su clave secreta que ya tenían lista
CONTRASENA_GEMINI = "AIzaSyAu8knH47oFlH7HoUynpJT3ReRbbI1JDMQ" 

try:
    # Conectamos con Google
    genai.configure(api_key=CONTRASENA_GEMINI)
    
    # EL CAMBIO CLAVE: Nombre exacto del modelo en minúsculas para que no falle
    model = genai.GenerativeModel('gemini-3.1-flash-lite')
    
except Exception as e:
    print(f"Error al configurar la IA: {e}")
    sys.exit()

# ==========================================
# 2. EL "DISFRAZ" DE HISTORIADOR (PROMPT)
# ==========================================
INSTRUCCIONES_HISTORIADOR = """
Actúa como un historiador y experto en religiones comparadas respetuoso, informado y objetivo.
Tu objetivo es responder preguntas sobre diferentes religiones del mundo de manera concisa, 
educativa y promoviendo el entendimiento y respeto intercultural.
No tomes posturas teológicas ni juzgues ninguna creencia, enfócate en hechos históricos, 
textos sagrados, símbolos y prácticas de forma imparcial.
Responde en español de forma amigable pero formal.
"""

# ==========================================
# 3. LA FUNCIÓN QUE HACE LA MAGIA
# ==========================================
def preguntar_a_gemini(pregunta_del_alumno):
    try:
        # Juntamos el disfraz con la pregunta del usuario
        prompt_completo = f"{INSTRUCCIONES_HISTORIADOR}\nPREGUNTA DEL ALUMNO: {pregunta_del_alumno}"
        
        # Le mandamos todo a Google
        respuesta = model.generate_content(prompt_completo)
        
        if respuesta.text:
            return respuesta.text
        else:
            return "El sistema no pudo generar una respuesta en este momento."
            
    except Exception as e:
        return f"Error de conexión con el servidor de la IA: {e}"

# ==========================================
# 4. EL PROGRAMA EN ACCIÓN (EL CHAT INFINITO)
# ==========================================
print("==================================================")
print("¡BIENVENIDO AL HUB DE RELIGIONES COMPARADAS!")
print("Sistema activado. Escribe 'salir' para cerrar.")
print("==================================================\n")

while True:
    # Le pedimos la pregunta al usuario
    entrada_usuario = input("Hazme una pregunta sobre cualquier religión: ")
    
    # Si escribe salir, se acaba el programa
    if entrada_usuario.lower() == "salir":
        print("\nCerrando el sistema. ¡Adiós!")
        break
        
    # Si le da Enter sin escribir nada, se salta la vuelta
    if not entrada_usuario.strip():
        continue
        
    print("\n[Pensando...] El Experto está analizando tu pregunta...")
    
    # Llamamos a la función para obtener la respuesta
    resultado_final = preguntar_a_gemini(entrada_usuario)
    
    # Mostramos el resultado bonito
    print("\n---------------- RESPUESTA ----------------")
    print(resultado_final)
    print("-------------------------------------------\n")