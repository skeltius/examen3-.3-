laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

def imprimir_laberinto():
    print("Laberinto:")
    for fila in laberinto:
        print(' '.join(map(str, fila)))
    print()

def resolver():
    inicio = (8, 0)  # Posición de inicio 'I'
    fin = (0, 0)     # Posición de fin 'F'
    
    mejor_ruta = []
    max_puntos = 0
    
    def backtrack(x, y, puntos, visitados, ruta_actual):
        nonlocal mejor_ruta, max_puntos
        
        if (x, y) == fin:
            if puntos >= 23 and puntos > max_puntos:
                max_puntos = puntos
                mejor_ruta = ruta_actual.copy()
            return
        
        visitados.add((x, y))
        ruta_actual.append((x, y))

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 9 and 0 <= ny < 9 and laberinto[nx][ny] != 0 and (nx, ny) not in visitados:
                valor = laberinto[nx][ny]
                suma_puntos = 1 if valor in ['I', 'F', 1] else valor
                
                backtrack(nx, ny, puntos + suma_puntos, visitados, ruta_actual)

        visitados.remove((x, y))
        ruta_actual.pop()

    backtrack(inicio[0], inicio[1], 0, set(), [])
    
    if mejor_ruta:
        mejor_ruta.insert(0, inicio)
        print(f"¡Solución encontrada con {max_puntos} puntos!")
        print("Ruta seguida (coordenadas [fila, columna]):")
        for i, (x, y) in enumerate(mejor_ruta):
            print(f"Paso {i+1}: [{x}, {y}] -> {laberinto[x][y]}")
        
        for x, y in mejor_ruta[1:-1]:
            laberinto[x][y] = 'P'
        
        return mejor_ruta
    else:
        print("No se encontró un camino con 23 puntos o más")
        return None

if __name__ == "__main__":
    print("=== LABERINTO DEL RATÓN ===")
    imprimir_laberinto()
    solucion = resolver()
    
    if solucion:
        print("Laberinto con la solución marcada:")
        imprimir_laberinto()
    else:
        print("No se encontró solución válida")
