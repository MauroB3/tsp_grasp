import numpy as np

from graph_functions import generateMatrix
from xml.etree import ElementTree as ET

GRAPH_LABEL = 'graph'
VERTEX_LABEL = 'vertex'
EDGES_LABEL = 'edge'
COST_LABEL = 'cost'


def filter_xmlelements(elem, tag):
    return list(filter(lambda x: x.tag == tag, list(elem)))


def get_cost_from_xmledge(xmledge):
    cost = xmledge.get(COST_LABEL)
    return float(cost)


def get_edges_from_xmlvertex(xmlvertex):
    xmledges = list(xmlvertex)
    return list(map(get_cost_from_xmledge, xmledges))


def get_graph_from_xmlgraph(xmlgraph):
    xmlvertexes = filter_xmlelements(xmlgraph, VERTEX_LABEL)
    total_vertexes = len(xmlvertexes)
    graph = generateMatrix(total_vertexes, total_vertexes)

    for vertex_index, xmlvertex in enumerate(xmlvertexes):
        graph[vertex_index] = get_edges_from_xmlvertex(xmlvertex)
    return graph


def get_graph(dataset):
    FULL_FILE_PATH = './tests/' + dataset + '.xml'
    tree = ET.parse(FULL_FILE_PATH)
    root = tree.getroot()
    xmlgraph = filter_xmlelements(root, GRAPH_LABEL)[0]
    graph = get_graph_from_xmlgraph(xmlgraph)
    final_grap = add_diagonal(graph)
    return final_grap


def add_diagonal(graph):
    np_g = np.array(graph)
    d = np_g.shape[0]
    new_g = np.ndarray((d, d+1), dtype=np_g.dtype)
    new_g[:, 0] = 0
    new_g[:-1, 1:] = np_g.reshape((d-1, d))
    new_g = new_g.reshape(-1)[:-d].reshape(d, d)
    return new_g

