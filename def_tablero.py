# 1. Crear la matriz 10x10 vacía (llena de None)
# Cada posición representa una casilla de agua inicialmente.
# La matriz es una lista que contendrá a su vez otras listas (las filas).
matriz = []

# Recorremos un bucle para crear cada una de las 10 filas (0 a 9)
for fila in range(10):
    # Para cada fila, creamos una lista vacía que contendrá sus columnas
    fila_actual = []

    # Recorremos otro bucle para crear cada columna dentro de la fila actual
    for columna in range(10):
        # Añadimos 'None' a la fila para indicar que la casilla está vacía
        fila_actual.append(None)

    # Una vez terminada la fila con sus 10 columnas, la añadimos a la matriz principal
    matriz.append(fila_actual)

# 2. Definir las naves por separado (4 submarinos, 3 fragatas, 1 portaaviones)
# Estos objetos se definen una sola vez.
portaaviones = Nave("Enterprise", "portaaviones", 5)

fragata_1 = Nave("Bismarck", "fragata", 3)
fragata_2 = Nave("Prince of Wales", "fragata", 3)
fragata_3 = Nave("Graf Spee", "fragata", 3)

sub_1 = Nave("U-47", "submarino", 1)
sub_2 = Nave("U-96", "submarino", 1)
sub_3 = Nave("U-505", "submarino", 1)
sub_4 = Nave("U-534", "submarino", 1)

# 3. Ejemplo de cómo asignar una nave a las coordenadas
# El mismo objeto 'portaaviones' se asigna a varias posiciones.
for col in range(1, 6):
    matriz[1][col] = portaaviones

# 4. Comprobar si hay una nave en una posición
def disparar(x, y):
    nave = matriz[x][y]
    if nave:
        print(f"¡Tocado! Has dado a: {nave.nombre}")
        nave.recibir_disparo()
    else:
        print("Agua")