#import Jugador, imprimirPinta, c=

class Jugador:
    nombre: str
    puntaje_total: int
    puntaje_ronda: int
    mano: list
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje_total = 0
        self.puntaje_ronda = 0
        self.mano = []

rondas = int(input())
n_jugadores = int(input())
jugadores = []
for i in range(n_jugadores):
    nombre = input()
    jugadores.append(Jugador(nombre))
pintas = []
for i in range(rondas): #2
    for elem in range(n_jugadores):
        pintas.append(input().split(";"))

for i in range(rondas):
    print("Ronda", i)
    print("Se reparten las cartas!")

