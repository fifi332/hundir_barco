# Clase que representa una nave en el juego
class Nave:
    # Crea una nave con su nombre, tipo y cantidad de vida inicial
    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre        # Nombre identificador de la nave
        self.tipo = tipo            # Tipo de nave ("submarino", "fragata", etc.)
        self.vida = vida            # Puntos de vida que tiene la nave
        self.hundido = False        # Estado: True si la nave está hundida
        self.TOCADO = 1             # Constante que representa el estado "tocado"
        self.HUNDIDO = 2            # Constante que representa el estado "hundido"

    # Metodo que gestiona que pasa cuando la nave recibe un disparo
    def recibir_disparo(self):
        # Si ya esta hundida, devuelve el estado "hundido"
        if self.hundido:
            return self.HUNDIDO

        # Se reduce la vida de la nave en 1 punto
        self.vida -= 1

        # Si su vida llega a cero o menos, se marca como hundido
        if self.vida <= 0:
            self.hundido = True
            print(f"{self.nombre} hundido")
            return self.HUNDIDO
        else:
            # Si aun tiene vida, solo se marca como "tocado"
            print(f"{self.nombre} tocado. Vida restante: {self.vida}")
            return self.TOCADO
