from networkx import from_numpy_matrix

from graph_functions import drawGraph
from graph_import import get_graph
from grasp import grasp, calcular_costo_vecino
from greedy import greedy

MAX_ITERACIONES = 500
MAX_MEJORAS_MINIMAS = 5
RATIO_MEJORA_MINIMA = 0.01
POS_INICIAL = 0

if __name__ == '__main__':
    nombre_test = 'd198'
    G = get_graph(nombre_test)

    # get_graph devuelve un grafo construido con numpy (gracias a la funcion que agrega la diagonal)
    # luego construyo el grafo de networkx, lo que me permite graficarlo y utilizar sus funciones
    grafo = from_numpy_matrix(G)
    #drawGraph(grafo)

    camino, costo = grasp(grafo, MAX_ITERACIONES, MAX_MEJORAS_MINIMAS, RATIO_MEJORA_MINIMA, POS_INICIAL)

    print("Camino: ", camino, " - costo: ", costo)

    #with open('resultado.txt', 'w') as file:
    #    file.write("Resultado para " + nombre_test + '\n')
    #    file.write("Camino hamiltoniano: " + str(camino) + '\n')
    #    file.write("Valor: " + str(valor))
    #    file.close()
