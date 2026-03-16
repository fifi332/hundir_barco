from nave import Nave

class Tablero:
    def __init__(self, tamano=10):
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

        self.nave = Nave("submarino","portaviones",1)

        self.nave_x = 3
        self.nave_y = 2

    def comprobar_impacto(self, x, y):
        print("[LOG] estoy en tablero comprobando impacto")
        if x == self.nave_x and y == self.nave_y:
            return self.nave.recibir_disparo()

        return self.AGUA