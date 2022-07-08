from greedy import greedy


def grasp(grafo, inicio, margen, limite_sin_mejorar):
    camino_inicial, costo_incial = greedy(grafo, inicio, margen)

    mejor_camino = camino_inicial
    mejor_costo = costo_incial
    veces_sin_mejorar = 0
    vecinos = obtener_vecinos(mejor_camino)

    for vecino in vecinos:
        peso = calcular_peso(vecino, grafo)
        if peso < mejor_costo:
            mejor_costo = peso
            mejor_camino = vecino
        else:
            veces_sin_mejorar += 1

        if veces_sin_mejorar == limite_sin_mejorar:
            return mejor_camino, mejor_costo

    return mejor_camino, mejor_costo

# O(n^2+2n) = O(n^2)
# Genero la lista de vecinos
# Los vecinos son aquellas soluciones donde solo cambia un paso, es decir, permutaciones de 2 elementos
def obtener_vecinos(solucion_inicial):
    solucion_inicial_copia = solucion_inicial.copy()  # O(n)
    pos_final = len(solucion_inicial) - 1
    elemento_inicial_final = solucion_inicial[0]
    # Saco el primer y el ultimo elemento, ya que el punto de partida y el final no quiero que cambie
    solucion_inicial_copia.pop(0)
    solucion_inicial_copia.pop(pos_final - 1)
    lista_soluciones = []

    # O(n*n)
    for i in range(len(solucion_inicial_copia) - 1):  # O(n-1): recorre la solucion que contiene todos los vertices menos el inicial
        sol_parcial = solucion_inicial_copia.copy()  # O(n)
        sol_parcial[i] = solucion_inicial_copia[i+1]
        sol_parcial[i+1] = solucion_inicial_copia[i]
        # Agrego el primer elemento al principio y al final, ya que es donde el recorrido debe empezar y terminar
        lista_soluciones.append([elemento_inicial_final] + sol_parcial + [elemento_inicial_final])

    sol_parcial = solucion_inicial_copia.copy()  # O(n)
    sol_parcial[0] = solucion_inicial_copia[pos_final - 2]
    sol_parcial[pos_final - 2] = solucion_inicial_copia[0]
    lista_soluciones.append([elemento_inicial_final] + sol_parcial + [elemento_inicial_final])

    return lista_soluciones

# O(n)
def calcular_peso(camino, grafo):
    peso_total = 0

    # O(n): recorre una solucion que contiene n-1 vertices
    for i in range(len(camino) - 1):
        nodo_actual = grafo[camino[i]]
        siguiente_nodo = camino[i+1]
        peso_total += nodo_actual[siguiente_nodo]['weight']

    return peso_total

