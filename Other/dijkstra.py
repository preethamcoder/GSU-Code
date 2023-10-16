import heapq
# # class for edges

# class Edge:
#     def __init__(self, weight, start_vertex, target_vertex):
#         self.weight = weight
#         self.start_vertex = start_vertex
#         self.target_vertex = target_vertex

# # class for Nodes
# class Node:
#     def __init__(self, name):
#         self.name = name
#         self.visited = False
#         # previous node that we come to this node
#         self.predecessor = None
#         self.neighbors = []
#         self.min_distance = float("inf")
    
#     def __lt__(self, other_node):
#         return self.min_distance < other_node.min_distance
    
#     def add_edge(self, weight, destination_vertex):
#         edge = Edge(weight, self, destination_vertex)
#         self.neighbors.append(edge)

# # Dijkstra Algorithm
# class Dijkstra:
#     def __init__(self):
#         self.heap = []
    
#     def calculate(self, start_vertex):
#         start_vertex.min_distance = 0
#         heapq.heappush(self.heap, start_vertex)
        
#         while self.heap:
#             # pop element with the lowest distance
#             actual_vertex = heapq.heappop(self.heap)
#             print(actual_vertex.name)
#             if actual_vertex.visited:
#                 continue
#             #  consider the neighbors
#             for edge in actual_vertex.neighbors:
#                 print("bro", edge.start_vertex.name, edge.target_vertex.name, edge.start_vertex.min_distance, edge.target_vertex.min_distance)
#                 start = edge.start_vertex
#                 target = edge.target_vertex
#                 new_distance = start.min_distance + edge.weight
#                 if new_distance < target.min_distance:
#                     target.min_distance = new_distance
#                     target.predecessor = start
#                     # update the heap
#                     print(target.name, "gets pushed", "min dist is", target.min_distance, "new predecessor is", target.predecessor.name)
#                     heapq.heappush(self.heap, target)
#                     # [F-19, F-17]
#             actual_vertex.visited = True
    
#     def get_shortest_path(self, vertex):
#         print(f"The shortest path to the vertext is: {vertex.min_distance}")
#         actual_vertex = vertex
#         while actual_vertex is not None:
#             print(actual_vertex.name, end=" ")
#             actual_vertex = actual_vertex.predecessor



# # Step 1 - create nodes
# nodeA = Node("A")
# nodeB = Node("B")
# nodeC = Node("C")
# nodeD = Node("D")
# nodeE = Node("E")
# nodeF = Node("F")
# nodeG = Node("G")
# nodeH = Node("H")

# # Step 2 - create edges
# nodeA.add_edge(6, nodeB)
# nodeA.add_edge(10, nodeC)
# nodeA.add_edge(9, nodeD)

# nodeB.add_edge(5, nodeD)
# nodeB.add_edge(16, nodeE)
# nodeB.add_edge(13, nodeF)

# nodeC.add_edge(6, nodeD)
# nodeC.add_edge(5, nodeH)
# nodeC.add_edge(21, nodeG)

# nodeD.add_edge(8, nodeF)
# nodeD.add_edge(7, nodeH)

# nodeE.add_edge(10, nodeG)

# nodeF.add_edge(4, nodeE)
# nodeF.add_edge(12, nodeG)

# nodeH.add_edge(2, nodeF)
# nodeH.add_edge(14, nodeG)

# algorithm = Dijkstra()
# algorithm.calculate(nodeA)
# algorithm.get_shortest_path(nodeG)

G = {
    "A": [["B", 2], ["C", 5]],
    "B": [["A", 2], ["D", 3], ["E", 1], ["F", 1]],
    "C": [["A", 5], ["F", 3]],
    "D": [["B", 3]],
    "E": [["B", 4], ["F", 3]],
    "F": [["C", 3], ["E", 3]],
}

def dijkstra(g, start, end):
    visited = set()
    q = [(start, 0)]
    while q:
        (curr, cost) = heapq.heappop(q)
        if curr in visited:
            pass
        visited.add(curr)
        if curr == end:
            return cost
        for ver, c in g[curr]:
            if ver in visited:
                continue
            curr_c = c+cost
            heapq.heappush(q, (ver, curr_c))
    return -1

print(dijkstra(G, "A", "N"))