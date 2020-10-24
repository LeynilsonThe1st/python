import networkx as nx
import matplotlib.pyplot as plt
 

mapa = nx.Graph()
nos = range(1, 5)
bordas = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (1, 5)]
mapa.add_nodes_from(nos)
mapa.add_edges_from(bordas)
mapa.add_node(6)
mapa.add_edge(1,6)
sorted(nx.connected_components(mapa))
nx.degree_centrality(mapa)
nx.to_numpy_matrix(mapa)

nx.draw(mapa, with_labels=True)
plt.show()