# import DisjointSet as dst
# def bellmanFord(graph, source):
#     distances = {each:float('inf') for each in graph}
#     distances[source] = 0
#     for each in range(graph.nodes-1):
#         for s, dest, w in graph:
#             curr_d = distances[s] + w
#             if curr_d != float('inf') and curr_d < distances[dest]:
#                 distances[dest] = curr_d
    
#     for s, dest, w in graph:
#         curr_d = distances[s] + w
#         if curr_d != float('inf') and curr_d < distances[dest]:
#             print("Negative cycle")
#             return
    
#     for k, v in distances.items():
#         print(k, ":", v)
class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.MST = []
        self.graph = []
        self.nodes = []
    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])
    def addNode(self, value):
        self.nodes.append(value)
    def printsoln(self):
        for s, d, w, in self.MST:
            print(f"{s} - {d}: {w}")
    def kruskal(self):
        ind, edge = 0, 0
        ds = dst.DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda each: each[2])
        print(self.graph)
        while edge < self.v-1:
            s, d, w = self.graph[ind]
            print(self.graph[ind])
            ind += 1
            x = ds.find(s)
            y = ds.find(d)
            print("box", x, y)
            if x != y:
                edge += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
        self.printsoln()

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("B", "A", 5)
g.addEdge("A", "C", 13)
g.addEdge("C", "A", 13)
g.addEdge("A", "E", 15)
g.addEdge("E", "A", 15)
g.addEdge("B", "D", 8)
g.addEdge("D", "B", 8)
g.addEdge("B", "C", 10)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("E", "C", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "C", 6)
g.kruskal()