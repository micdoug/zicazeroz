from .matrixgraph import MatrixGraph
from .listgraph import ListGraph

def create_graph(vertexes, t='list'):
    """
        Cria um novo grafo utilizando a implementação especificada.
        Se o tipo não é especificado cria uma instância com implementação por lista de adjacência.
    """
    if t == 'matrix':
        return MatrixGraph(vertexes)
    else:
        return ListGraph(vertexes)