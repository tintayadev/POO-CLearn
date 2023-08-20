n = int(input())  # Leer la cantidad de archivos de chatbots

resultados = open("resultados.txt", "w")

for i in range(n):
    chatbot_file = f"chatbot_{i}.txt"  # Nombre del archivo de chatbot
    errores = 0  # Contador de errores
    conversaciones = 0  # Contador de conversaciones
    mensajes = 0 # Contador de mensajes
    registro_errores = 0 
    
    lines = open(chatbot_file, "r")

    resultados.write(f"CHATBOT {i}\n")
    for line in lines:
        if "CHATBOT:" in line:
            mensajes += 1

        if "Eso no esta dentro de mis protocolos." in line:
            errores += 1
        elif "----FIN DE LA CONVERSACION----" in line:
            conversaciones += 1
            resultados.write(f"Conversacion {conversaciones} -> {errores}/{mensajes}\n")
            registro_errores += errores
            errores = 0
            mensajes = 0

    media_errores = round(registro_errores / conversaciones, 2)
    resultados.write(f"Errores por conversacion: {media_errores}\n")

resultados.close()