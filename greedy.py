# Margen es la variable que vamos a utilizar para la aleatoriedad
import random


# O(n*m)
def greedy(grafo, inicio, margen=3):
    peso_final = 0
    actual = inicio
    camino = [inicio]

    # O(n) porque recorre todos los vertices del grafo
    while len(camino) < len(grafo):
        nodo, peso = agarrar_menor_arista(grafo[actual], camino, margen)
        camino.append(nodo)
        peso_final += peso
        actual = nodo

    camino.append(inicio)
    peso_final += grafo[actual][inicio]['weight']

    return camino, peso_final

# O(m-1) ya que mira todas las aristas y se trata de un grafo completo
def agarrar_menor_arista(lista_de_aristas, camino_actual, margen):
    diccionario_aristas = dict(lista_de_aristas)
    lista_tuplas = [(key, diccionario_aristas[key]['weight']) for key in diccionario_aristas]
    lista_tuplas_posibles = filter(lambda elem: elem[0] not in camino_actual, lista_tuplas)
    aristas_ordenadas = sorted(lista_tuplas_posibles, key=lambda elem: elem[1])
    primeras_n = aristas_ordenadas[0:margen]
    return random.choice(primeras_n)
