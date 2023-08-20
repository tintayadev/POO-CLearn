archivo = open("lineas.txt", "r")
lineas = archivo.readlines()
archivo.close()

artista = "Shakira"

lista_limpia=[]
for linea in lineas:
    lista_limpia.append(linea.strip().split(";"))
for linea in lista_limpia:
    artistas = linea[1].split("-")
    if artista in artistas and len(artistas)>1: #cuando no esta sola
        artistas.remove(artista)
        # "shakira" in "shakira jr-maluma"  truenue
        # "shakira" in ["maluma"] false
    
    if artista in artistas and len(artistas)==1: 
        artistas = ["Anonimo"]
    cad_aux = ""
    for x in artistas:
        cad_aux += x +"-"
    linea[1] = cad_aux

print(lista_limpia)
resultados = open("restultados.txt","w")
cnt = 0 #len(lista_limpia) # 7
for linea in lista_limpia: 
    aux = ""
    for elem in linea:
        aux += elem+";"
    aux = aux[0:len(aux)-1] # [:-1]
    if cnt == len(lista_limpia)-1:
        resultados.write(aux)
    else:
        resultados.write(aux+"\n")
    cnt+=1
resultados.close()

# result = censurar_artista(lineas, "Shakira")
# print(result)

lista = ['Please Please Me', 'The Beatles', 'Please Please Me']
cad = ";".join(lista)
print(cad)