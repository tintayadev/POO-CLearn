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
        return "Esta es la gran "+ self.nombre+" que ha sobrevivido "+str(self.edad)+" inviernos.\nLa gran "+self.nombre+" tiene:\n"+str(self.oro)+ " kilos de oro\n" +str(self.soldados)+ " miles de soldados\n" +str(self.tecnologia)+ " puntos de avance tecnologicos\n" +str(self.proteccion)+ " kilometros de muralla de proteccions\n"+str(self.moral)+" puntos de moral"
    
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
                        
    def aplicar_evento(self, nom_evento, e_oro, e_soldados, e_tecnologia, e_proteccion):
        print("Ha ocurrido", nom_evento)
        self.oro += e_oro
        self.soldados += e_soldados
        self.tecnologia += e_tecnologia
        self.proteccion += e_proteccion
        if self.oro < 0:
            self.oro = 0
        if self.soldados < 0:
            self.soldados = 0
        if self.tecnologia < 0:
            self.tecnologia = 0
        if self.proteccion < 0:
            self.proteccion = 0

    def invasion_ciudad(self,civilizacion_atacante, fila, columna):
        print(civilizacion_atacante, "ha atacado la ciudad de", self.mapa[fila][columna].nombre)
        self.mapa[fila][columna].vida -= 50
        self.moral -= 50
        self.oro -= 80
        self.soldados -= 10
        if self.moral < 0:
            self.moral =0
        if self.oro < 0:
            self.oro = 0
        if self.soldados < 0:
            self.soldados = 0

        if self.mapa[fila][columna].vida <= 0:
            print("Se perdio la ciudad de",self.mapa[fila][columna].nombre,"a manos de",civilizacion_atacante)
            self.mapa[fila][columna] = ""
        return self.mapa[fila][columna]
    
    def conquistar_ciudad(self, nombre_ciudad, tipo):
        sw = 0
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if not self.mapa[i][j] and sw == 0:
                    self.mapa[i][j] = DCCiudad(nombre_ciudad, tipo, i, j)
                    print(self.nombre, "ha conquistado la ciudad de", self.mapa[i][j].nombre)
                    if self.mapa[i][j].tipo == "financiera":
                        self.oro += 100
                        print(self.mapa[i][j].nombre, "recolecto 100 de oro")
                    if self.mapa[i][j].tipo == "militar":
                        self.soldados += 10
                        print(self.mapa[i][j].nombre, "ha entrenado 10 mil soldados")
                    if self.mapa[i][j].tipo == "cientifica":
                        self.tecnologia += 10
                        print(self.mapa[i][j].nombre, "ha generado 10 puntos de avance tecnologico")
                    if self.mapa[i][j].tipo == "fortaleza":
                        self.proteccion += 15
                        print(self.mapa[i][j].nombre, "ha aportado con 15 puntos de proteccion")
                    sw = 1

archivo = open(input(),'r')
sw = 0
for elem in archivo.readlines():
    datos = elem.strip().split(",")
    if sw == 0:
        nom_civ = datos[0]
        edad_civ = int(datos[1])
        n = int(datos[2])
        # print(nom_civ, edad_civ, n)
        A = DCCivilizacion(nom_civ,edad_civ)
        A.crear_mapa(n)
        # mapas.imprimir_mapa(A.mapa)
        sw = 1
    else:
        nom_ciu = datos[0]
        tipo_ciu = datos[1]
        fil = int(datos[2])
        col = int(datos[3])
        C = DCCiudad(nom_ciu, tipo_ciu, fil, col)
        A.agregar_ciudad(C)
archivo.close()

mapas.imprimir_mapa(A.mapa)
A.recolectar()
print(A)

for i in range(5):
    ls = input().split(",")
    if ls[0] == "Conquista":
        nombre = ls[1]
        tipo = ls[2]
        A.conquistar_ciudad(nombre, tipo)
    elif ls[0] == "Invasion":
        nombre_civ = ls[1]
        fil = int(ls[2])
        col = int(ls[3])
        A.invasion_ciudad(nombre_civ,fil,col)
    else:
        nom_evento = ls[0]
        e_oro = int(ls[1])
        e_soldados = int(ls[2])
        e_tecnologia = int(ls[3])
        e_proteccion = int(ls[4])
        A.aplicar_evento(nom_evento,e_oro,e_soldados,e_tecnologia,e_proteccion)
print(A)
mapas.imprimir_mapa(A.mapa)

if A.oro and A.soldados and A.tecnologia and A.proteccion and A.moral:
    print(A.nombre, "sobrevivio al paso del tiempo")
else:
    print(A.nombre, "cayo")


