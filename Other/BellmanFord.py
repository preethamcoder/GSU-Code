#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.


class Graph:

    def __init__(self, vertices):
        self.V = vertices   
        self.graph = []     
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def addNode(self,value):
        self.nodes.append(value)

    def bellmanFord(self, src):
        dist = {i : float("Inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.V-1):
            for s, d, w in self.graph:
                mg = dist[s]+w
                if dist[s] != float("Inf") and mg < dist[d]:
                    dist[d] = mg
        
        for s, d, w in self.graph:
            mg = dist[s]+w
            print(dist[d], mg)
            if dist[s] != float("Inf") and mg < dist[d]:
                print("Graph contains negative cycle")
                return
        print("Vertex Distance from Source")
        for key, value in dist.items():
            print('  ' + key, ':', value)
        #self.print_solution(dist)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", -4)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
print(g.graph)
g.bellmanFord("E")


        

  
