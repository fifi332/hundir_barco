from tablero import Tablero

# Clase principal que gestiona el juego en general
class Juego:
    # Crea un tablero y lanza algunos ataques
    def __init__(self):
        self.tablero = Tablero()  # Se inicia el tablero con las naves colocadas

        # Ejemplo de ataques para probar el funcionamiento
        self.lanzar_ataque(1, 0)
        self.lanzar_ataque(1, 0)
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(1, 3)
        self.lanzar_ataque(1, 4)

    # Muestra el resultado del disparo
    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    # Lanza un ataque sobre las coordenadas (x, y) del tablero
    def lanzar_ataque(self, x, y):
        print(f"Ataque a {x},{y}")
        casilla = self.tablero.casillero[x][y]  # Se localiza la casilla objetivo

        resultado = casilla.recibir_disparo()   # Se ejecuta el disparo sobre la casilla

        self.mostrar_resultado(resultado)        # Se muestra el resultado por pantalla

if __name__ == "__main__":
    Juego()
