from networkx import from_numpy_matrix
from graph_import import get_graph
from grasp import grasp

if __name__ == '__main__':
    nombre_test = 'brg180'
    G = get_graph(nombre_test)
    graph = from_numpy_matrix(G)
    # drawGraph(graph)
    camino, valor = grasp(graph, 0, 3, 3)
    with open('resultado.txt', 'w') as file:
        file.write("Resultado para " + nombre_test + '\n')
        file.write("Camino hamiltoniano: " + str(camino) + '\n')
        file.write("Valor: " + str(valor))
        file.close()
