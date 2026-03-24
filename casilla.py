from nave import Nave

# Clase que representa una casilla individual del tablero (puede contener una nave o ser agua)
class Casilla:
    # Asigna si la casilla tiene una nave o es "agua"
    def __init__(self, nave):
        self.nave = nave            # Puede ser un objeto Nave o agua
        self.disparada = False      # Indica si ya se ha disparado sobre esta casilla

    # Metodo que gestiona el disparo sobre la casilla
    def recibir_disparo(self):
        # Si ya se disparo antes sobre esta casilla
        if self.disparada == True:
            # Y contiene una nave
            if self.nave != 'agua':
                print(f'Casilla ya disparada con {self.nave.nombre},de tipo {self.nave.tipo},con {self.nave.vida} vidas ')
                self.disparada = True
            else:
                # Si era agua
                print(f'Casilla ya disparada es de agua')
                self.disparada = True

        # Si la casilla es agua, no hay impacto
        if self.nave == 'agua':
            self.disparada = True
            return 0  # 0 representa agua

        # Si aun no se habia disparado, se lanza el disparo a la nave
        if self.disparada == False:
            resultado = self.nave.recibir_disparo()  # Llama al metodo de nave
            self.disparada = True
            return resultado
