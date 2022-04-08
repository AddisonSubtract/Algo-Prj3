import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_nodes_from("ABCDEFGHIJKLMNOP")


#Edge creation
edges =[('A','B'),('A','E'),('A','F'),('B','C'),('B','F'),
         ('C','D'),('C','G'),('D','G'),('E','F'),('E','I'),
         ('F','I'),('G','J'),('H','K'),('H','L'),('I','J'),
         ('I','M'),('K','L'),('K','O'),('L','P'),('M','N')]
G.add_edges_from(edges)

#print(G.to_undirected(G))

nx.draw(G, with_labels=1)
plt.show()

#Question a
print("Node A DFS:", list(nx.dfs_edges(G, source='A')),'\n')
print("Node A BFS:", list(nx.bfs_edges(G, source='A')),'\n')
print("Node H DFS:", list(nx.dfs_edges(G, source='H')),'\n')
print("Node H BFS:", list(nx.bfs_edges(G, source='H')),'\n')

#Question b
print("Node A DFS:", list(nx.dfs_edges(G, source='A', depth_limit=2)),'\n')
print("Node A BFS:", list(nx.bfs_edges(G, source='A', depth_limit=2)),'\n')

#Question c
print("Node A DFS:", list(nx.dfs_edges(G, source='A', depth_limit=10)),'\n')
print("Node A BFS:", list(nx.bfs_edges(G, source='A', depth_limit=10)),'\n')