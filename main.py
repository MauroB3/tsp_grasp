from networkx import from_numpy_matrix
from graph_import import get_graph
from grasp import grasp

if __name__ == '__main__':
    nombre_test = 'brg180'
    G = get_graph(nombre_test)

    # get_graph devuelve un grafo construido con numpy (gracias a la funcion que agrega la diagonal)
    # luego construyo el grafo de networkx, lo que me permite graficarlo y utilizar sus funciones
    graph = from_numpy_matrix(G)

    # drawGraph(graph)
    camino, valor = grasp(graph, 0, 3, 3)
    with open('resultado.txt', 'w') as file:
        file.write("Resultado para " + nombre_test + '\n')
        file.write("Camino hamiltoniano: " + str(camino) + '\n')
        file.write("Valor: " + str(valor))
        file.close()
