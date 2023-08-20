# import mapas
# class DCCiudad:
#     nombre: str
#     tipo: str
#     vida: int
#     fila: int
#     columna: int

#     def __init__(self, nombre, tipo, fila, columna):
#         self.nombre = nombre
#         self.tipo = tipo
#         self.vida = 100
#         self.fila = fila
#         self.columna = columna
    
#     def __str__(self):
#         #return f"Esta es la gran DCCiudad de {self.nombre} de tipo {self.tipo} con {self.vida} de vida."
#         return "Esta es la gran DCCiudad de "+ self.nombre + " de tipo "+self.tipo+" con "+ str(self.vida)+ " de vida."

# class DCCivilizacion:
#     nombre: str
#     edad: int
#     mapa: list
#     oro: int
#     soldados: int
#     tecnologia: int
#     proteccion: int
#     moral: int

#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
#         self.mapa = []
#         self.oro = 0
#         self.soldados = 0
#         self.tecnologia = 0
#         self.proteccion = 0
#         self.moral = 100

#     def __str__(self):
#         return "Esta es la gran "+ self.nombre+" que ha sobrevivido "+str(self.edad)+" inviernos.\nLa gran "+self.nombre+" tiene:\n"+str(self.oro)+ " kilos de oro\n" +str(self.soldados)+ " miles de soldados\n" +str(self.tecnologia)+ " puntos de avance tecnologicos\n" +str(self.proteccion)+ " kilometros de muralla de proteccion"
    
#     def crear_mapa(self, n):
#         for i in range(n):
#             lista = []
#             for j in range(n):
#                 lista.append("")
#             self.mapa.append(lista)

#     def agregar_ciudad(self, ciudad: DCCiudad):
#         self.mapa[ciudad.fila][ciudad.columna] = ciudad

#     def recolectar(self):
#         for elem in self.mapa:
#             for elem2 in elem:
#                 if elem2 != "":
#                     if elem2.tipo == "financiera":
#                         self.oro += 100
#                         print(elem2.nombre, "recolecto 100 de oro")
#                     if elem2.tipo == "militar":
#                         self.soldados += 10
#                         print(elem2.nombre, "ha entrenado 10 mil soldados")
#                     if elem2.tipo == "cientifica":
#                         self.tecnologia += 10
#                         print(elem2.nombre, "ha generado 10 puntos de avance tecnologico")
#                     if elem2.tipo == "fortaleza":
#                         self.proteccion += 15
#                         print(elem2.nombre, "ha aportado con 15 puntos de proteccion")
                        

# archivo = open(input(),'r')
# sw = 0
# for elem in archivo.readlines():
#     datos = elem.split(",") #Aca cambio
#     if sw == 0:
#         nom_civ = datos[0]
#         edad_civ = int(datos[1])
#         n = int(datos[2])  #Aca cambio
#         # print(nom_civ, edad_civ, n)
#         A = DCCivilizacion(nom_civ,edad_civ)
#         A.crear_mapa(n)
#         # mapas.imprimir_mapa(A.mapa)
#         sw = 1
#     else:
#         nom_ciu = datos[0]
#         tipo_ciu = datos[1]
#         fil = int(datos[2])
#         col = int(datos[3])
#         C = DCCiudad(nom_ciu, tipo_ciu, fil, col)
#         A.agregar_ciudad(C)
        

# mapas.imprimir_mapa(A.mapa)
# A.recolectar()
# print(A)

# archivo.close()

import mapas
class DCCiudad:
    nombre: str
    tipo: str
    vida: int
    fila: int
    columna: int

    def __init__(self, nombre, tipo, fila, columna):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = 100
        self.fila = fila
        self.columna = columna
    
    def __str__(self):
        #return f"Esta es la gran DCCiudad de {self.nombre} de tipo {self.tipo} con {self.vida} de vida."
        return "Esta es la gran DCCiudad de "+ self.nombre + " de tipo "+self.tipo+" con "+ str(self.vida)+ " de vida."

class DCCivilizacion:
    nombre: str
    edad: int
    mapa: list
    oro: int
    soldados: int
    tecnologia: int
    proteccion: int
    moral: int

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.mapa = []
        self.oro = 0
        self.soldados = 0
        self.tecnologia = 0
        self.proteccion = 0
        self.moral = 100

    def __str__(self):
        return "Esta es la gran "+ self.nombre+" que ha sobrevivido "+str(self.edad)+" inviernos.\nLa gran "+self.nombre+" tiene:\n"+str(self.oro)+ " kilos de oro\n" +str(self.soldados)+ " miles de soldados\n" +str(self.tecnologia)+ " puntos de avance tecnologicos\n" +str(self.proteccion)+ " kilometros de muralla de proteccion"
    
    def crear_mapa(self, n):
        for i in range(n):
            lista = []
            for j in range(n):
                lista.append("")
            self.mapa.append(lista)

    def agregar_ciudad(self, ciudad: DCCiudad):
        self.mapa[ciudad.fila][ciudad.columna] = ciudad

    def recolectar(self):
        for elem in self.mapa:
            for elem2 in elem:
                if elem2 != "":
                    if elem2.tipo == "financiera":
                        self.oro += 100
                        print(elem2.nombre, "recolecto 100 de oro")
                    if elem2.tipo == "militar":
                        self.soldados += 10
                        print(elem2.nombre, "ha entrenado 10 mil soldados")
                    if elem2.tipo == "cientifica":
                        self.tecnologia += 10
                        print(elem2.nombre, "ha generado 10 puntos de avance tecnologico")
                    if elem2.tipo == "fortaleza":
                        self.proteccion += 15
                        print(elem2.nombre, "ha aportado con 15 puntos de proteccion")
                        
archivo=open(input(),"r")
sw=0
for elem in archivo.readlines():
    datos=elem.split(",")
    if sw==0:
        nom_civ=datos[0]
        edad_civ=int(datos[1])
        print(nom_civ, type(nom_civ))
        print(edad_civ, type(edad_civ))
        n=int(datos[2])
        A=DCCivilizacion(nom_civ,edad_civ)
        A.crear_mapa(n)
        sw=1
    else:
        nom_ciu=datos[0]
        tipo_ciu=datos[1]
        fil=int(datos[2])
        col=int(datos[3])
        C=DCCiudad(nom_ciu,tipo_ciu,fil,col)
        A.agregar_ciudad(C)

mapas.imprimir_mapa(A.mapa)
A.recolectar()
print(A)
archivo.close()