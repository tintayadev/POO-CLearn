#Lectura archivo
archivo = open('postulaciones.txt', 'r')
lineas = archivo.readlines()
archivo.close()

postulaciones = []
for linea in lineas:
    linea = linea.strip().split(';')
    postulaciones.append(linea)

universidades = []
puntajes = []
for postulacion in postulaciones:
    estudiante = postulacion[0]
    pref_1 = postulacion[1]
    pref_2 = postulacion[2]
    pref_3 = postulacion[3]

    encontrado_1 = False
    encontrado_2 = False
    encontrado_3 = False

    for i in range(len(universidades)):
        if universidades[i] == pref_1:
            puntajes[i] += 5
            encontrado_1 = True
        elif universidades[i] == pref_2:
            puntajes[i] += 3
            encontrado_2 = True
        elif universidades[i] == pref_3:
            puntajes[i] += 1
            encontrado_3 = True

    if not encontrado_1:
        universidades.append(pref_1)
        puntajes.append(5)
    if not encontrado_2:
        universidades.append(pref_2)
        puntajes.append(3)
    if not encontrado_3:
        universidades.append(pref_3)
        puntajes.append(1)


archivo = open('puntaje_universidades.txt', 'w')
results = []
for i in range(len(universidades)):
    elem = [universidades[i],puntajes[i]]
    results.append(elem)
results.sort()

for i in range(len(results)):
    archivo.write(f"{results[i][0]};{results[i][1]}\n")
archivo.close()
