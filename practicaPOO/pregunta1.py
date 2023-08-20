# creacion de clase
class DCCivilizacion:
    # atributos
    nombre: str
    edad: int
    mapa: list
    oro: int
    soldados: int
    tecnologia: int
    proteccion: int
    moral: int

    # metodo inicializa datos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.mapa = []
        self.oro = 0
        self.soldados = 0
        self.tecnologia = 0
        self.proteccion = 0
        self.moral = 100
    # metodo __str__
    def __str__(self):
        # return f"""Esta es la gran {self.nombre} que ha sobrevivido {self.edad} inviernos.
        # La gran {self.nombre} tiene:
        # {self.oro} kilos de oro
        # {self.soldados} miles de soldados
        # {self.tecnologia} puntos de avance tecnologicos
        # {self.proteccion} kilometros de muralla de proteccion"""
        return "Esta es la gran "+ self.nombre+" que ha sobrevivido "+str(self.edad)+" inviernos.\nLa gran "+self.nombre+" tiene:\n"+str(self.oro)+ " kilos de oro\n" +str(self.soldados)+ " miles de soldados\n" +str(self.tecnologia)+ " puntos de avance tecnologicos\n" +str(self.proteccion)+ " kilometros de muralla de proteccion"


ls=input().split(",")
nombre_civ=ls[0]
edad_civ=int(ls[1])

A=DCCivilizacion(nombre_civ,edad_civ)
print(A)
# nombre_civ, edad_civ = input().split(",")
# # Crear el objeto A de clase DCCivilizacion
# A = DCCivilizacion(nombre_civ, int(edad_civ))

# print(A)

