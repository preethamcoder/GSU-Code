class Graph:
    def __init__(self, vertex_no, edges, nodes):
        self.vertex_no = vertex_no
        self.edges = edges
        self.nodes = nodes
        self.MST = []
    def printsoln(self):
        for s, d, w in self.MST:
            print(f"{s} - {d}: {w}")
    def prim(self):
        visited = [0]*self.vertex_no
        edges_num = 0
        visited[0] = True
        while edges_num < self.vertex_no-1:
            smol = float('inf')
            for each in range(self.vertex_no):
                if visited[each]:
                    for other in range(self.vertex_no):
                        if (not visited[other] and self.edges[each][other]):
                            if smol > self.edges[each][other]:
                                smol = self.edges[each][other]
                                s = each
                                d = other
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edges_num += 1
        self.printsoln()

edges = [[0, 10, 20, 0, 0], [10, 0, 30, 5, 0], [20, 30, 0, 15, 6], [0, 5, 15, 0, 8], [0, 0, 6, 8, 0]]
nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.prim()