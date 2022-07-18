import math

from greedy import greedy

# Si consideramos a max_iteraciones como una constante, el costo de la funcion es O(busqueda_local),
# sino O(busqueda_local * max_iteraciones)
def grasp(grafo_inicial, max_iteraciones, max_mejoras_minimas, ratio_mejora_minima, pos_inicial):
    n_interaciones = 0
    mejor_sol = [], math.inf

    while n_interaciones < max_iteraciones:
        camino_greedy, peso_greedy = greedy(grafo_inicial, pos_inicial)
        sol_local = busqueda_local(camino_greedy, peso_greedy, max_mejoras_minimas, ratio_mejora_minima, grafo_inicial)

        if sol_local[1] < mejor_sol[1]:
            mejor_sol = sol_local

        n_interaciones += 1

    return mejor_sol


# El costo es O(n^2 * x), donde O(n^2) es el costo de generar_mejor_vecino, y x es la cantidad de iteraciones que haga
# el while
def busqueda_local(camino_inicial, peso_inicial, max_mejoras_minimas, ratio_mejora_minima, grafo_inicial):
    mejor_camino, mejor_peso = camino_inicial, peso_inicial
    cant_mejoras_minimas = 0
    continuar_busqueda = True

    while continuar_busqueda and cant_mejoras_minimas < max_mejoras_minimas:
        camino_vecino, costo_vecino = generar_mejor_vecino(mejor_camino, mejor_peso, grafo_inicial)

        if costo_vecino < mejor_peso: # Si el vecino es mejor que la solucion anterior
            minimo_de_mejora = mejor_peso * ratio_mejora_minima
            if (costo_vecino - mejor_peso) <= minimo_de_mejora:
                # Si entra en este if significa que la mejora fue muy pequeña
                # entonces sumo una mejora minima
                cant_mejoras_minimas += 1

            mejor_camino, mejor_peso = camino_vecino, costo_vecino
        else:
            # Si entra al else es porque ningun vecino es mejor que la solucion que encontramos
            # por ende, llegó al maximo local
            continuar_busqueda = False

    return mejor_camino, mejor_peso


# Devuelve el mejor vecino a partir de una solucion
# En peor caso es O(n^2), porque recorre todos los vecinos (O(n)) y si es una mejor solucion hace un copy del recorrido
# inicial, lo que tiene costo O(n)
# Sin embargo en promedio es mejor que realizar la copia para cada uno de los vecinos
def generar_mejor_vecino(recorrido_inicial, costo_inicial, grafo_inicial):
    mejor_recorrido, mejor_costo = recorrido_inicial, costo_inicial
    pos_final = len(recorrido_inicial) - 2

    for i in range(1, pos_final):
        costo_vecino = calcular_costo_vecino(recorrido_inicial, costo_inicial, i, grafo_inicial)

        if costo_vecino < mejor_costo:
            nuevo_mejor_recorrido = recorrido_inicial.copy()
            mejor_costo = costo_vecino
            if i == pos_final:  # Estoy en el ultimo nodo, lo swapeo con el primero
                nuevo_mejor_recorrido[1] = recorrido_inicial[i]
                nuevo_mejor_recorrido[i] = recorrido_inicial[1]
            else:
                nuevo_mejor_recorrido[i] = recorrido_inicial[i + 1]
                nuevo_mejor_recorrido[i + 1] = recorrido_inicial[i]
            mejor_recorrido = nuevo_mejor_recorrido

    return mejor_recorrido, mejor_costo


# Swapea la posicion 'indice' con la posicion siguiente
# (entendiendo como posicion siguiente a indice + 1 o a la primer posicion si indice es el ultimo elemento)
# O(1)
def calcular_costo_vecino(recorrido, costo, i, grafo_inicial):
    siguiente_posicion = i + 1 if i < len(recorrido) - 2 else 1 # Si estoy en la ultima posicion swapeo con el primero
    nodo_anterior = recorrido[i - 1]
    nodo_actual = recorrido[i]
    nodo_siguiente = recorrido[siguiente_posicion]
    nodo_siguiente_siguiente = recorrido[siguiente_posicion + 1]

    return costo \
        - grafo_inicial[nodo_anterior][nodo_actual]['weight'] \
        - grafo_inicial[nodo_actual][nodo_siguiente]['weight'] \
        - grafo_inicial[nodo_siguiente][nodo_siguiente_siguiente]['weight'] \
        + grafo_inicial[nodo_anterior][nodo_siguiente]['weight'] \
        + grafo_inicial[nodo_siguiente][nodo_actual]['weight'] \
        + grafo_inicial[nodo_actual][nodo_siguiente_siguiente]['weight']



