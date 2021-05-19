class Graph:
    """
    As with trees, a graph have nodes that connect to each other to create relationships. A graph can have more than one or two connections. In fact, graph nodes often have a  multitude of connections.

    Graph <==> Mapa <==> Diagrama

     thatGraph={'A' : ['B', 'F'],
                'B' : ['C', 'A'],
                'C' : ['B', 'D'],
                'D' : ['C', 'E'],
                'E' : ['D', 'F'],
                'F' : ['E', 'A']}

           +---+
       +-- | A | --+
       |   +---+   |
     +---+       +---+
     | B |       | F |
     +---+       +---+
       |           |
     +---+       +---+
     | C |       | E |
     +---+       +---+
       |   +---+   |
       +-- | D | --+
           +---+
    """

    def __init__(self, conn={}):
        self.conn = conn

    def find(self, start, end, path=[]):
        """find() -> list.

        Cria o primeiro caminho `path = path[star]`
        com base no valor passado a função `star`,
        seleciona a rota não visitada iterando pelos seus nós `nodes`,
        repete os passos trocando de input(o inicio
        `star` sera igual a nova rota `node` o destino `end` mantém, e
        é adicionado o caminho percorrido a função)
        ate que a rota seja igual ao destino
        """

        path = path + [start]
        print("Start", start)
        if start == end:
            return path
        for node in self.conn[start]:
            print("node", node)
            if node not in path:
                print("path", path)
                new_path = self.find(node, end, path)
                if new_path:
                    return new_path


graph ={'A' : ['B', 'F'],
        'B' : ['C', 'A'],
        'C' : ['B', 'D'],
        'D' : ['C', 'E'],
        'E' : ['D', 'F'],
        'F' : ['E', 'A']}

gph = Graph(graph)
gph.find('A', 'E')
