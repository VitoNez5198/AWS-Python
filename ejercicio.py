from google import genai

# Inicializas el cliente (asegúrate de tener tu API KEY configurada)
client = genai.Client(api_key="AIzaSyAcX5nXh4ZO9qA8QMGNDqkpTuY5HdC30xo")

print("--- Chat con Gemini Iniciado (Escribe 'salir' para terminar) ---")

# Ciclo infinito para mantener el programa corriendo
while True:
    # Captura lo que escribes en la terminal
    user_input = input("\nTú: ")

    # Condición de salida para que no se quede atrapado para siempre
    if user_input.lower() in ["salir", "exit", "quit"]:
        print("¡Nos vemos!")
        break

    # Si presionaste Enter sin escribir nada, se salta el ciclo para evitar errores
    if not user_input.strip():
        continue

    # Envía tu mensaje a la API
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
    )

    # Imprime la respuesta en la terminal
    print(f"\nGemini: {response.text}")