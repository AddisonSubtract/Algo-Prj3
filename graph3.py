# Python program for Kruskal's algorithm to find Minimum Spanning Tree
# of a given connected, undirected and weighted graph

#http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/
 
#Class to represent a graph
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary to store graph
         
  
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
 
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        #If ranks are same, then make one as root and increment
        # its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's algorithm
    def KruskalMST(self):
 
        result =[] #This will store the resultant MST
 
        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]
 
        #Step 1:  Sort all the edges in non-decreasing order of their
        # weight.  If we are not allowed to change the given graph, we
        # can create a copy of graph
        self.graph =  sorted(self.graph,key=lambda item: item[2])
        #print self.graph
 
        parent = [] ; rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
     
        # Number of edges to be taken is equal to V-1
        while e < self.V -1 :
 
            # Step 2: Pick the smallest edge and increment the index
            # for next iteration
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
 
            # If including this edge does't cause cycle, include it
            # in result and increment the index of result for next edge
            if x != y:
                e = e + 1  
                result.append([u,v,w])
                self.union(parent, rank, x, y)          
            # Else discard the edge
 
        # print the contents of result[] to display the built MST
        print ("Following are the edges in the constructed MST")
        for u,v,weight  in result:
            #print str(u) + " -- " + str(v) + " == " + str(weight)
            print ("%d -- %d == %d" % (u,v,weight))
 
 
'''g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)'''

'''
g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 7, 11)
g.addEdge(1, 2, 8 )
g.addEdge(2, 8, 2)
g.addEdge(2, 3, 7)
g.addEdge(2, 5, 4)
g.addEdge(3, 5, 14)
g.addEdge(3, 4, 9)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2 )
g.addEdge(6, 8, 6 )
g.addEdge(6, 7, 1 )
g.addEdge(7, 8, 7 )
'''

'''
A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
H = 7
I = 8
'''

#Test Graph - TODO
g = Graph(9)
g.addEdge(0,1,22)#A to B
g.addEdge(0,2,9)#A to C
g.addEdge(0,3,12)#A to D
g.addEdge(1,2,35)#B to C
g.addEdge(1,5,36)#B to F
g.addEdge(1,7,34)#B to H
g.addEdge(2,3,4)#B to D
g.addEdge(2,4,65)#C to E
g.addEdge(2,5,42)#C to F
g.addEdge(3,4,33)#D to E
g.addEdge(3,8,30)#D to I
g.addEdge(4,5,18)#E to F
g.addEdge(4,6,23)#E to G
g.addEdge(5,6,39)#F to G
g.addEdge(5,7,24)#F to H
g.addEdge(6,7,25)#G to H
g.addEdge(6,8,21)#G to I
g.addEdge(7,8,19)#H to I


g.KruskalMST()
 
#This code is contributed by Neelam Yadav
