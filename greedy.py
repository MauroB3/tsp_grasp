# Margen es la variable que vamos a utilizar para la aleatoriedad
import math
import random


# O(n*m)
def greedy(grafo, inicio):
    peso_final = 0
    actual = inicio
    camino = [inicio]

    # O(n) porque recorre todos los vertices del grafo
    while len(camino) < len(grafo):
        nodo, peso = agarrar_menor_arista(grafo[actual], camino)
        camino.append(nodo)
        peso_final += peso
        actual = nodo

    camino.append(inicio)
    peso_final += grafo[actual][inicio]['weight']

    return camino, peso_final


# O(m-1) ya que mira todas las aristas y se trata de un grafo completo
def agarrar_menor_arista(lista_de_aristas, camino_actual):
    diccionario_aristas = dict(lista_de_aristas)
    lista_tuplas = [(key, diccionario_aristas[key]['weight']) for key in diccionario_aristas]
    lista_tuplas_posibles = filter(lambda elem: elem[0] not in camino_actual, lista_tuplas)
    aristas_ordenadas = sorted(lista_tuplas_posibles, key=lambda elem: elem[1])
    margen = calcular_margen(len(aristas_ordenadas))
    primeras_n = aristas_ordenadas[0:margen]
    return random.choice(primeras_n)


# Calculo el numero del top de soluciones que voy a ver
# O(1)
def calcular_margen(n_nodos):
    n_porcentaje = math.ceil(n_nodos * 0.05)  # Me quedo con el 5% redodeando hacia arriba

    if n_porcentaje > 5:  # en este caso miro el 5% de soluciones
        return n_porcentaje
    elif n_nodos > 5:  # si es mayor que 5 significa que puedo agarrar las 5 primeras opciones
        return 5
    else:  # en este caso tengo menos de 5 soluciones, asi que solamente tomo la primera (al menos una debe haber)
        return 1


