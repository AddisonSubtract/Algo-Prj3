# Python implementation of Dijkstra's algorithm
#https://gist.github.com/econchick/4666413

import collections

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = collections.defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
                                        
def dijkstra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

def main():
    graph = Graph()
    ''' The sample graph is on page 111 of printed text (p116 ebook)
           B-----D
         /||\   /| 
       A  || \ / |
        \ ||  \  | 
         \|| / \ | 
           C ----E
    '''
    graph.nodes = {'A','B','C','D','E','F','G','H','I'}
    graph.edges = {'A': ['B','C','D'], 'B':['A','C','F','H'], \
                'C':['A','B','D','E','F'], 'D':['A','C','E','I'],\
                'E': ['C', 'D', 'F','G'], 'F':['B','C','E','G','H'],\
                'G': ['E','F','H','I'], 'H': ['B','F','G','I'],\
                'I': ['D','G','H']}
        
    graph.distance = {('A', 'B'):22, ('A', 'C'):9, ('A', 'D'):12,\
                     ('B', 'A'):22, ('B','C'):35, ('B','F'):36, ('B','H'):34,\
                     ('C', 'A'):9,  ('C','B'):36, ('C','D'):4, ('C','F'):42, ('C','E'):65,\
                     ('D','A'):12, ('D','C'):4, ('D','E'):33, ('D','I'):30,\
                     ('E','C'):65, ('E','D'):33, ('E','F'):18, ('E','G'):23,\
                     ('F','B'):36, ('F','C'):42, ('F','E'):18, ('F','G'):39, ('F','H'):24,\
                     ('G','E'):23, ('G','F'):39, ('G','H'):25, ('G','I'):21,\
                     ('H','B'):34, ('H','F'):24, ('H','G'):25, ('H','I'):19,\
                     ('I','D'):30, ('I','G'):21, ('I','H'):19
                   }

    v, path = dijkstra(graph, 'A')
    print('Visited: ', v)
    print('Path :', path)

if __name__ == "__main__":
    main()
