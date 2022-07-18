import os

from networkx import from_numpy_matrix
from graph_import import get_graph
from grasp import grasp
from graph_functions import drawGraph
from utils import plot_result, write_result

MAX_ITERACIONES = 3500
MAX_MEJORAS_MINIMAS = 5
RATIO_MEJORA_MINIMA = 0.01
POS_INICIAL = 0


def grasp_grafo_unico(nombre_test):
    G = get_graph(nombre_test)

    # get_graph devuelve un grafo construido con numpy (gracias a la funcion que agrega la diagonal)
    # luego construyo el grafo de networkx, lo que me permite graficarlo y utilizar sus funciones
    grafo = from_numpy_matrix(G)

    camino, costo, mejor_iteracion, iteraciones, iteraciones_costos = grasp(grafo, MAX_ITERACIONES, MAX_MEJORAS_MINIMAS,
                                                                            RATIO_MEJORA_MINIMA, POS_INICIAL)

    # Plot de evolucion a traves de las iteraciones
    plot_result(iteraciones, 'iteracion', iteraciones_costos, 'costo', nombre_test)

    # Guardo en un archivo el mejor camino encontrado y su costo
    write_result(camino, costo, nombre_test)

    # Retorno la mejor iteracion para poder graficarla en la funcion grasp_todos()
    return mejor_iteracion


def grasp_todos():
    nombres = []
    mejores_it = []

    for file in os.listdir('./tests/'):
        nombre = file.split('.')[0]
        res = grasp_grafo_unico(nombre)
        nombres.append(nombre)
        mejores_it.append(res)

    plot_result(nombres, "test", mejores_it, "mejor iteracion", 'scoring completo')


if __name__ == '__main__':
    # grasp_grafo_unico("att48")
    grasp_todos()
