import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from("ABCDEFGHI")

edges = [('A','B',22), ('A','C',9), ('A','D',12),
         ('B','C',35), ('B',"F",36), ('B','H',34),
         ('C','D',4), ('C','E',65), ('C','F',42),
         ('D','E',33), ('D','I',30),
         ('E','F',18), ('E','G',23),
         ('F','G',39), ('F','H',24),
         ('G','H',25), ('G','I',21),
         ('H','I',19)]

weight = (22,9,12,35,36,34,4,65,42,33,30,18,23,39,24,25,21,19)

G.add_weighted_edges_from(edges)

nx.draw(G, with_labels=1)
plt.show()

#Question a
print(nx.shortest_path(G, source='A', target='I'))
print(nx.shortest_path(G, source='A', target='G'))

#Question b
tree = nx.minimum_spanning_tree(G)
print(sorted(tree.edges(data=True)))