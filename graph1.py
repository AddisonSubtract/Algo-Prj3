import networkx as nx
import matplotlib.pyplot as plt

ch = 'A'

#Graph creation
G = nx.petersen_graph()
G.clear()

for x in range(16):
    G.add_node(chr(ord(ch) + x))

#Edge creation
edges =(('A','B'),('A','E'),('A','F'),('B','C'),('B','F'),
         ('C','D'),('C','G'),('D','G'),('E','F'),('E','I'),
         ('F','I'),('G','J'),('H','K'),('H','L'),('I','J'),
         ('I','M'),('K','L'),('K','O'),('L','P'),('M','N'),)
G.add_edges_from(edges)

#Graph drawing
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
G.clear()