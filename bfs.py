# Python3 BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict
 
# Class representation of a directed graph
# using adjacency list representation
class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
 
    # Method to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Method: BFS traversal of the graph starting with s
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as 
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
 
            # Dequeue a vertex from 
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
'''
  0 ---> 1
  ^    /
  |   /
  |  /
  V
s 2----> 3 <
'''
 
# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)
