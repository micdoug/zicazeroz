import math

class ListGraph:
    def __init__(self, vertexes):
        """
        Inicializa o grafo com a implementação via matriz de adjacência.
        Esta implementação considera grafos direcionados, portanto a ordem da origem e destino
        durante a inserção de arestas é importante.
        :param vertexes: Número de vértices que o grafo tem.
        """
        self.graph = {}
        if type(vertexes) is int:
            for i in range(1, vertexes+1):
                self.graph[i] = []
        else:
            for v in vertexes:
                self.graph[v] = []


    def vertexes(self):
        """
        Lista de vértices que fazem parte do grafo.
        :return: Tupla com vértices do grafo.
        """
        return tuple(self.graph.keys())

    def edges(self):
        """
        Lista de arestas do grafo.
        :return: Uma lista com as tuplas que representam as arestas do grafo.
        """
        ed = []
        for orig in self.graph:
            for dest in self.graph[orig]:
                ed.append((orig, dest))
        return ed

    def add_edge(self, orig, dest):
        """
        Adiciona uma nova aresta no grafo.
        :param orig: Vértice de origem
        :param dest: Vértice de destino
        """
        if type(dest) is list:
            for d in dest:
                self.graph[orig].append(d)
        else:
            self.graph[orig].append(dest)

    def remove_edge(self, orig, dest):
        """
        Remove uma aresta do grafo.
        :param orig: Vértice de origem
        :param dest: Vértice de destino
        """
        self.graph[orig].remove(dest)

    def vertex_degrees(self):
        """
        Cálcula os graus de entrada e saída de todos os vértices.
        :return: Dicionário com graus de entrada e saída (nesta ordem) de todos
        os vértices do grafo.
        """
        deg = {s: [0, 0] for s in self.graph.keys()}
        for k in self.graph:
            for v in self.graph[k]:
                deg[v][0] += 1 # Aumenta o grau de entrada do vértice alvo
                deg[k][1] += 1 # Aumenta o grau de saída do vértice alvo
        return deg

    def transposed(self):
        """
        Retorna o grafo transposto
        :return: Grafo transposto
        """
        g = ListGraph(self.vertexes())
        edges = self.edges()
        for edge in edges:
            g.add_edge(edge[1], edge[0])
        return g

    def bfs(self, orig):
        """
        Executa a busca em largura (breadth first search retornando um dicionário com os parâmetros dos vértices
        e um grafo direcionado com a árvore gerada.
        :param orig: Vértice de origem
        :return: Grafo direcionado gerado a partir da busca e um dicionário com os parâmetros de
        distência, cor e antecessor de cada vértice.
        """
        # Armazenando atributos dos vértices
        vparams = {s: dict(color='white', d=math.inf, pi=None) for s in self.vertexes()}
        vparams[orig]['color'] = 'gray'
        vparams[orig]['d'] = 0

        q = []
        q.append(orig)
        g = ListGraph(self.vertexes())
        while len(q) > 0:
            u = q.pop(0)
            for dest in self.graph[u]:
                if vparams[dest]['color'] == 'white':
                    vparams[dest]['color'] = 'gray'
                    vparams[dest]['d'] = vparams[u]['d'] + 1
                    vparams[dest]['pi'] = u
                    q.append(dest)
                    g.add_edge(u, dest)
                vparams[u]['color'] = 'black'
        return vparams, g

    def dfs(self):
        """
        Executa a busca em profundidade no grafo a partir de todos os vértice.
        A resposta retorna um dicionário com as informações de antecessores, tempo de descoberta e fechamento
        de cada vértice do grafo.
        """
        #Armazenando atributos dos vertices
        vparams = {s: dict(color='white', pi=None) for s in self.vertexes()}
        time = 0
        for v in self.vertexes():
            if vparams[v]['color'] == 'white':
                vparams, time = self.dfs_visit(v, time, vparams)
        return vparams

    def dfs_visit(self, origin, time, vparams):
        time += 1
        vparams[origin]['d'] = time
        vparams[origin]['color'] = 'gray'
        for v in self.graph[origin]:
            if vparams[v]['color'] == 'white':
                vparams[v]['pi'] = origin
                vparams, time = self.dfs_visit(v, time, vparams)
        vparams[origin]['color'] = 'black'
        time += 1
        vparams[origin]['f'] = time
        return vparams, time



