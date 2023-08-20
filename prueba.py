n = int(input())

resultados = open("resultados.txt", "w")

for i in range(n):
    archivo = open(f"chatbot_{i}.txt", "r")
    
    lineas = archivo.readlines() # lista de cadenas de chatbot_0.txt
    # print(type(archivo), type(lineas))
    # print(lineas)
    conversaciones = 0 
    suma_errores = 0
    errores = 0 # contar los errores en una conversacion
    mensajes = 0 # contar los mensajes del chatbot en una conversacion
    resultados.write(f"CHATBOT {i}\n") # escribir en un archivo
    for linea in lineas:
        # contar los mensajes del chatbot
        if "CHATBOT:" in linea:
            mensajes += 1
        # contar los errores
        if "CHATBOT: Eso no esta dentro de mis protocolos." in linea:
            errores += 1
        # verificar si acaba una conversacion
        if "----FIN DE LA CONVERSACION----" in linea:
            conversaciones += 1
            resultados.write(f"conversacion {conversaciones} -> {errores}/{mensajes}\n")
            suma_errores += errores
            errores = 0
            mensajes = 0

    # mostrar promedio de los erroes de la conversacion
    media = round(suma_errores / conversaciones, 2)
    resultados.write(f"errores por conversacion: {media}\n")

    archivo.close()

resultados.close()