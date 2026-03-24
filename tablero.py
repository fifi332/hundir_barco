from casilla import *

# Clase que representa el tablero de juego, formado por casillas con naves o agua
class Tablero:
    # Crea un tablero cuadrado (por defecto de 10x10)
    def __init__(self, tamanho=10):
        self.AGUA = 0         # Constante para indicar disparo al agua
        self.TOCADO = 1       # Constante para indicar nave tocada
        self.HUNDIDO = 2      # Constante para indicar nave hundida

        # Se crean varios objetos Nave con diferentes tipos y vidas
        por1 = Nave("pipi", "portaaviones", 5)
        fra1 = Nave("toto", "fragata", 3)
        fra2 = Nave("pata", "fragata", 3)
        fra3 = Nave("potete", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        # Se inicializa la matriz del tablero con objetos Casilla (cada uno puede contener agua o una nave)
        self.casillero = [
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(por1), Casilla(por1), Casilla(por1), Casilla(por1), Casilla(por1), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(fra1), Casilla(fra1), Casilla(fra1), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla(sub1), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(fra2), Casilla(fra2), Casilla(fra2), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(fra3), Casilla(fra3), Casilla(fra3), Casilla('agua'), Casilla('agua'), Casilla(sub3), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla(sub4), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla(sub2)]
        ]
