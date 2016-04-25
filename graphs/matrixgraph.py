class MatrixGraph:
    def __init__(self, vertexes):
        """
        Inicializa o grafo com a implementação via matriz de adjacência.
        Esta implementação considera grafos direcionados, portanto a ordem da origem e destino
        durante a inserção de arestas é importante.
        :param vertexes: Número de vértices que o grafo tem.
        """
        self.graph = []
        for i in range(0, vertexes):
            self.graph.append([])
            for j in range(0, vertexes):
                self.graph[i].append(0)

    def vertexes(self):
        """
        Lista de vértices que fazem parte do grafo.
        :return: Tupla com vértices do grafo.
        """
        return tuple(range(0, len(self.graph)))

    def edges(self):
        """
        Lista de arestas do grafo.
        :return: Returna lista com as tuplas que representam as arestas do grafo.
        """
        ed = []
        for i in range(0, len(self.graph)):
            for j in range(0, len(self.graph)):
                if self.graph[i][j]:
                    ed.append((i+1, j+1))
        return ed

    def add_edge(self, orig, dest):
        """
        Adiciona uma nova aresta no grafo.
        :param orig: Vértice de origem
        :param dest: Vértice de destino
        """
        self.graph[orig-1][dest-1] = 1

    def remove_edge(self, orig, dest):
        """
        Remove uma aresta do grafo.
        :param orig: Vértice de origem
        :param dest: Vértice de destino
        """
        self.graph[orig-1][dest-1] = 0

    def vertex_degrees(self):
        """
        Cálcula os graus de entrada e saída de todos os vértices.
        :return: Dicionário com graus de entrada e saída (nesta ordem) de todos
        os vértices do grafo.
        """
        deg = {s: [0, 0] for s in range(1, len(self.graph)+1)}
        for i in range(0, len(self.graph)):
            for j in range(0, len(self.graph)):
                if self.graph[i][j]:
                    deg[j+1][0] += 1
                    deg[i+1][1] += 1
        return deg

    def transposed(self):
        """
        Retorna o grafo transposto
        :return: Grafo transposto
        """
        g = MatrixGraph(len(self.graph))
        edges = self.edges()
        for edge in edges:
            g.add_edge(edge[1], edge[0])
        return g
