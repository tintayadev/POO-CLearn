def porOrden(string):
    return string[0]

def estaciones_comunes(metro):

    todas_est=[]#ya revisado=[]
    est_revisados = []

    for linea in metro:
        sub_estaciones=linea[1]
        for estacion in sub_estaciones: # Tottenham Court Road
            if estacion not in est_revisados:
                est_revisados.append(estacion)
                #vamos a hacer la busqueda: va a comparar estacion con todas las estaciones del metro
                comunes = []
                for linea2 in metro:
                    sub_estaciones2 = linea2[1]
                    for estacion2 in sub_estaciones2:
                        if estacion == estacion2:
                            comunes.append(linea2[0])
                if len(comunes) > 1:
                    todas_est.append([estacion, comunes])

                
    todas_est.sort(key=porOrden)
    
    return todas_est

def porOrden2(string):
    return string[1], string[0]

def porOrden3(string):
    return string[0]

def k_menos_conectadas(metro, k):
    comunes = estaciones_comunes(metro)
    lineas_estaciones = [] #[[linea, n_estac], [linea, n_estac]]
    revisados = []

    for estacion in comunes:
        lineas_comunes = estacion[1]
        for linea in lineas_comunes: #'Central Line'
            if linea not in revisados:
                #print(f"Busqueda {linea}")
                revisados.append(linea)
                # conteo
                cnt = 0

                for estacion2 in comunes:
                    lineas_comunes2 = estacion2[1]
                    if linea in lineas_comunes2:
                        cnt += 1
                lineas_estaciones.append([linea, cnt])
    resultado = []
    if lineas_estaciones:
        lineas_estaciones.sort(key=porOrden2)
        
        for i in range(k):
            resultado.append(lineas_estaciones[i][0])
    else:
        metro.sort(key=porOrden3)
        for i in range(k):
            resultado.append(metro[i][0])
    return resultado
    

metro = [
    ['Bakerloo', ['South Kenton', 'North Wembley']],
    ['District', ['Ealing Broadway', 'Ealing Common', 'South Ealing', 'Chiswick Park']],
    ['Jubiles', ['Green Park', 'Westminster', 'Waterloo']],
    ['DLR', ['Gallions Reach', 'Beckton']],
    ['Northern', ['Morden', 'South Wimbledon', 'Colliers Wood']],
]
print(k_menos_conectadas(metro, 5))