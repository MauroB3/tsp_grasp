'''

Generar grafos de manera aleatoria y funciones para graficar

@References:
- https://networkx.org/ library to generate graph
- https://matplotlib.org/ library to create visualizations
'''

import networkx as nx
import matplotlib.pyplot as plt
import pydot
from random import randrange
from networkx import Graph, DiGraph
from networkx.generators import random_graphs
from networkx.drawing.nx_pydot import graphviz_layout


def plotEnd():
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    # plt.tight_layout()
    plt.show()


def draw(G, pos):
    # draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=400, alpha=0.9, node_color="green", node_shape="o")
    # draw node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # draw edges
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.4, edge_color="green")
    # draw edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    plotEnd()


def drawGraph(nxGraph):
    pos = nx.shell_layout(nxGraph)
    draw(nxGraph, pos)


def drawTree(nxGraph):
    pos = graphviz_layout(nxGraph, prog="dot")
    draw(nxGraph, pos)


def generateGraph(nodesCount: int, edgesCount: int) -> Graph:
    return random_graphs.gnm_random_graph(nodesCount, edgesCount, directed=False)


def generateDiGraph(nodesCount: int, edgesCount: int) -> DiGraph:
    return random_graphs.gnm_random_graph(nodesCount, edgesCount, directed=True)


def generateDenseGraph(V, E):
    return random_graphs.dense_gnm_random_graph(V, E, directed=True)


# add costs to each edge in the graph G with values between a and b
def addCosts(G, a: int, b: int) -> None:
    for e in G.edges:
        weight = randrange(a, b)
        G.add_edge(e[0], e[1], weight=weight)


def generateMatrix(rows_size, cols_size, val=None): return [[val for _ in range(cols_size)] for _ in range(rows_size)]


def getWeightFromEdgeValues(values, default=0):
    return values['weight'] if 'weight' in values else default


def fromNxGraphtoMatrix(G):
    matrix = generateMatrix(G.number_of_nodes(), G.number_of_nodes(), 0)
    for v, adjacencies in G.adjacency():
        for w, values in adjacencies.items():
            matrix[v][w] = getWeightFromEdgeValues(values, 1)
    return matrix


def fromNxGraphtoAdjacency(G):
    graph = [[] for _ in range(G.number_of_nodes())]
    for v, adjacencies in G.adjacency():
        for w, values in adjacencies.items():
            graph[v].append((w, getWeightFromEdgeValues(values, 0)))
    return graph


def fromMatrixToNxGraph(G):
    return Graph(G)


def printGraph(G):
    print("Graph:")
    for line in G:
        print(line)
