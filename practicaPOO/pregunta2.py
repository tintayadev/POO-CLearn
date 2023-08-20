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
                        


    

# ls1=input().split(",")
# nombre_civ=ls1[0]
# edad_civ=int(ls1[1])

# A = DCCivilizacion(nombre_civ,edad_civ)

# # print(A)
# n = int(input())

# A.crear_mapa(n)


# ls2 = input().split(",") #nombre_ciudad, tipo_ciudad
# ls3 = input().split(",") #fila, columna
# nombre_ciudad = ls2[0]
# tipo_ciudad = ls2[1]
# fil = ls3[0]
# col = ls3[1]

# C1 = DCCiudad(nombre_ciudad, tipo_ciudad, int(fil), int(col))

# ls2 = input().split(",") #nombre_ciudad, tipo_ciudad
# ls3 = input().split(",") #fila, columna
# nombre_ciudad = ls2[0]
# tipo_ciudad = ls2[1]
# fil = ls3[0]
# col = ls3[1]

# C2 = DCCiudad(nombre_ciudad, tipo_ciudad, int(fil), int(col))

# print(C1)
# print(C2)

# A.agregar_ciudad(C1)
# A.agregar_ciudad(C2)


# mapas.mostrar_mapa(A.mapa)

# A.recolectar()
# print(A)

import mapas
# Escribe aquí tu código
class DCCiudad:
    def _init_ (self,nombre,tipo,fila,columna):
        self.nombre=nombre
        self.tipo=tipo
        self.vida=100
        self.fila=fila
        self.columna=columna
    def _str_ (self):
        return "Esta es la gran DCCiudad de "+self.nombre+" de tipo "+self.tipo+" con "+str(self.vida)+" de vida."


class DCCivilizacion:
    def _init_(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.mapa=[]
        self.oro=0
        self.soldados=0
        self.tecnologia=0
        self.proteccion=0
        self.moral=100
        #str
    def _str_(self):
        return "Esta es la gran "+ self.nombre+" que ha sobrevivido "+str(self.edad)+" inviernos.\nLa gran "+self.nombre+" tiene:\n"+str(self.oro)+ " kilos de oro\n" +str(self.soldados)+ " miles de soldados\n" +str(self.tecnologia)+ " puntos de avance tecnologicos\n" +str(self.proteccion)+ " kilometros de muralla de proteccion"

    def crear_mapa(self,n):
        for i in range (n):
            lista=[]
            for j in range (n):
                lista.append("")
            self.mapa.append(lista)
    def agregar_ciudad (self,ciudad):
        ciudad=self.mapa[ciudad.fila][ciudad.columna]=ciudad #asignar a la ciudad en ese lugar
    
    def recolectar (self):
        for elem in self.mapa:
            for elem2 in elem:
                if elem2 !="":
                    if elem2.tipo=="financiera":
                        self.oro+=100
                        print(elem2.nombre,"recolecto 100 de oro")
                    if elem2.tipo=="militar":
                        self.soldados+=10
                        print(elem2.nombre,"ha entrenado 10 mil soldados")
                    if elem2.tipo=="cientifica":
                        self.tecnologia+=10
                        print(elem2.nombre,"ha generado 10 puntos de avance tecnologico")
                    if elem2.tipo=="fortaleza":
                        self.proteccion+=15
                        print(elem2.nombre,"ha aportado con 15 puntos de proteccion")

ls1=input().split(",")
nombre_civ=ls1[0]
edad_civ=int(ls1[1])

A=DCCivilizacion(nombre_civ,edad_civ)

n=int(input())
A.crear_mapa(n)

ls2=input().split(",")#nombre de la ciudad y el tipo ciudad
ls3=input().split(",")#fila y columna
nombre_ciudad=ls2[0]
tipo_ciudad=ls2[1]
fila=ls3[0]
columna=ls3[1]

C1=DCCiudad(nombre_ciudad,tipo_ciudad,int(fila),int(columna))

ls2=input().split(",")#nombre de la ciudad y el tipo ciudad
ls3=input().split(",")#fila y columna
nombre_ciudad=ls2[0]
tipo_ciudad=ls2[1]
fila=ls3[0]
columna=ls3[1]

C2=DCCiudad(nombre_ciudad,tipo_ciudad,int(fila),int(columna))

print(C1)
print(C2)

A.agregar_ciudad(C1)
A.agregar_ciudad(C2)

mapas.imprimir_mapa(A.mapa)

A.recolectar()
print(A)