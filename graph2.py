import networkx as nx
G = nx.DiGraph()
G.add_nodes_from(range(1,13))
G.add_edge(1,3)
G.add_edge(2,1)
G.add_edges_from([(3,2), (3,5)])
G.add_edges_from([(4,1), (4,2), (4,12)])
G.add_edges_from([(5,6), (5,8)])
G.add_edges_from([(6,7), (6,8), (6,10)])
G.add_edge(7,10)
G.add_edges_from([(8,9), (8,10)])
G.add_edges_from([(9,5), (9,11)])
G.add_edges_from([(10,9), (10,11)])
G.add_edge(11,12)
SCC = nx.strongly_connected_components(G)
for c in SCC:
    print(c)
print(SCC)

