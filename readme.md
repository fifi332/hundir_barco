# Hundir la Flota

## Descripción general

El código está dividido en cuatro módulos principales, cada uno con una responsabilidad diferente:

- `nave.py`: Define las características y el comportamiento de las naves.
- `casilla.py`: Representa cada casilla del tablero, que puede contener una nave o ser agua.
- `tablero.py`: Construye el tablero del juego con las naves colocadas.
- `juego.py`: Controla el flujo del juego y los disparos de prueba.

---

##  Funcionamiento general

### 1. `Nave`
La clase `Nave` representa cada tipo de barco: **portaaviones**, **fragata**, o **submarino**.  
Cada nave tiene un nombre, tipo y puntos de vida.  
Cuando recibe un disparo:
- Resta 1 punto a su vida.
- Si la vida llega a 0, se considera *hundida*.
- Si aún tiene vida, se considera *tocada*.

### 2. `Casilla`
Cada casilla del tablero puede tener una nave o agua.  
La clase `Casilla` gestiona:
- Si la casilla ya fue disparada antes.
- Si un disparo impacta en el agua o en una nave.
- Llama al método `recibir_disparo` de la nave cuando corresponde.

### 3. `Tablero`
`Tablero` crea la matriz del juego (por defecto de 10x10).  
Inicializa varias naves y las coloca en posiciones fijas.  
Cada celda es un objeto `Casilla`, y puede ser:
- `'agua'` (sin nave)
- Un objeto `Nave` compartido (representando una parte de la nave)

Ejemplo de fragmento del tablero:
```
[Casilla(por1), Casilla(por1), Casilla(por1), Casilla('agua'), ...]
```
Esto significa que hay una nave (por1) ocupando varias casillas consecutivas.

### 4. `Juego`

Juego actúa como controlador principal del programa.

Al iniciarse:

    Crea un tablero con las naves ya colocadas.

    Realiza automáticamente varios disparos de prueba para mostrar los resultados (por consola).


Cada disparo se imprime así:

    Ataque a 1,0
    pipi tocado. Vida restante: 4
    Tocado

El juego muestra:

    "Agua" si no hay nave.

    "Tocado" si la nave fue dañada pero no hundida.

    "Hundido" si la nave fue destruida por completo.
