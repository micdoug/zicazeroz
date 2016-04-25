import math

class ZicaZeroZ:
    def __init__(self, friendships, contributions, focuses):
        """
        Construtor da classe de resolução do problema ZicaZeroZ.
        :param friendships:
        Grafo com a descrição das amizades entre os voluntários.
        :param contributions:
        Grafo com a descrição da contribuição dos voluntários para os focus de zica.
        :param focuses:
        Lista de focus a serem cobertos pelo algoritmo
        """
        # Armazena grafos de amizades
        self.friendships = friendships
        self.contributions = contributions
        self.focuses = focuses

        self.contributions_t = contributions.transposed()
        for r in self.friendships.vertexes():
            self.contributions_t.graph.pop(r, None)

        self.focuses_count = {f: len(self.contributions_t.graph[f]) for f in self.contributions_t.graph}



    def less_known_focus(self):
        """
        Retorna o foco menos conhecido.
        :return:
        O foco menos conhecido.
        """
        return min(self.focuses_count, key=self.focuses_count.get)

    def bfs_zica(self, orig):
        # Dicionário de parâmetros dos vértices
        # d -> distância a partir da origem
        # visited -> define se o vértice já foi visitado
        # pi -> antecessor do vértice
        # bridge -> indica tentativa de uso do vértice como ponto para conhecer novos focus, usado para limpeza
        vparams = {s: dict(d=math.inf, visited=False, pi=None, bridge=False) for s in self.friendships.vertexes()}
        vparams[orig]['visited'] = True
        vparams[orig]['d'] = 0

        queue = self.friendships.graph[orig][:]  # Fila de exploração
        for v in queue:
            vparams[v]['pi'] = orig
            vparams[v]['d'] = 1
        focuses = set(self.contributions.graph[orig]) # Lista de focus já alcançados
        total_focuses = len(self.focuses)
        while len(focuses) != total_focuses:
            u = self.get_max(queue, focuses)
            queue.remove(u)
            vparams[u]['visited'] = True # Marca como visitado
            # Adiciona novos focos na lista de focos conhecidos
            new_focuses = set(self.contributions.graph[u]) - focuses
            if len(new_focuses) == 0:
                vparams[u]['bridge'] = True  # Define se o vértice é uma ponte para exploração
            focuses |= new_focuses
            # Adicionar novos voluntários na lista de exploração
            for v in self.friendships.graph[u]:
                if vparams[v]['d'] == math.inf:
                    queue.append(v)
                    vparams[v]['d'] = vparams[u]['d'] + 1
                    vparams[v]['pi'] = u

        # Procedimento de limpeza da resposta
        # Parte 1: Remover os vértices não visitados
        remove = [r for r in vparams if not vparams[r]['visited']]
        for r in remove:
            vparams.pop(r, None)
        # Parte 2: Remover bridges que não tem sucessores
        repeat = True
        while repeat:
            repeat = False
            bridges = [v for v in vparams if vparams[v]['bridge']]
            for b in bridges:
                if len([v for v in vparams if vparams[v]['pi'] == b]) == 0:
                    vparams.pop(b, None)
                    repeat = True

        return vparams



    def get_max(self, queue, focuses):
        """
        Busca o voluntário que mais contribui para minha solução atual.
        :param queue:
        Fila de voluntários a serem analisados.
        :param focuses:
        Lista de focos que já conheço.
        :return:
        Voluntário que mais contribui para adicionar novos focus à solução.
        """
        max = queue[0]
        for x in queue[1:]:
            if len(set(self.contributions.graph[max]) - focuses) < len(set(self.contributions.graph[x]) - focuses):
                max = x
        return max

    def get_min_volunteers_graph(self):
        """
        Constrói um grafo conexo que cobre todos os focos de combate
        utilizando a menor quantidade de voluntários possível.
        :return:
        Dicionário com a descrição dos antecessores de cada vértice presente na resposta.
        A partir deste dicionário é possível reconstruir o grafo resposta.
        """
        focus = self.less_known_focus()
        initial_volunteers = self.contributions_t.graph[focus]
        graphs = []
        for v in initial_volunteers:
            graphs.append(self.bfs_zica(v))
        # todo: No caso de empate das respostas disponíveis, escolher aquela cuja a soma dos vértices seja a menor
        return min(graphs, key=len)