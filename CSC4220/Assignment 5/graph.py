import heapq
from collections import OrderedDict

class Graph:
    def __init__(self, data):
        self.g = {}
        self.vertices = []
        self.distances = {}
        self.predecessors = {}
        self.paths_with_costs = []
        for each in data:
            source, dest, weight = each.split()
            if source not in self.vertices:
                self.vertices.append(source)
            if source in self.g:
                self.g[source].append([dest, int(weight)])
            else:
                self.g[source] = [[dest, int(weight)]]
            if dest in self.g:
                self.g[dest].append([source, int(weight)])
            else:
                self.g[dest] = [[source, int(weight)]]
            if dest not in self.vertices:
                self.vertices.append(dest)
        self.g = dict(sorted(self.g.items()))
        self.vertices.sort()
        for k in self.g:
            self.g[k] = sorted(self.g[k], key=lambda x:[x[1], x[0]])

    def print_graph(self):
        print(self.g)
        return
    
    def add_edge(self, info):
        s, d, weight = info
        if s in self.g and d in self.g:
            if weight > 0:
                for lst in self.g[s]:
                    if d in lst:
                        lst[-1] = weight
                for lst in self.g[d]:
                    if s in lst:
                        lst[-1] = weight
                        return
                self.g[s].append([d, weight])
                self.g[d].append([s, weight])
                for k in self.g:
                    self.g[k] = sorted(self.g[k], key=lambda x: [x[1], x[0]])
                return
        if weight <= 0:
            self.g[s] = [each for each in self.g[s] if each[0] != d]
            self.g[d] = [each for each in self.g[d] if each[0] != s]
            if self.g[s] == []:
                del self.g[s]
                self.vertices = [vert for vert in self.vertices if vert != s]
            if self.g[d] == []:
                del self.g[d]
                self.vertices = [vert for vert in self.vertices if vert != d]
            for k in self.g:
                self.g[k] = sorted(self.g[k], key=lambda x: [x[1], x[0]])
            return
        else:
            if s in self.g:
                self.g[s].append([d, weight])
            if d in self.g:
                self.g[d].append([s, weight])
            elif s not in self.g:
                self.g[s] = [[d, weight]]
                if s not in self.vertices:
                    self.vertices.append(s)
            elif d not in self.g:
                self.g[d] = [[s, weight]]
                if d not in self.vertices:
                    self.vertices.append(d)
            self.vertices.sort()
            for k in self.g:
                self.g[k] = sorted(self.g[k], key=lambda x: [x[1], x[0]])
            return
    
    def dfs_run(self, start, end, visited, path, cost):
        if start == end:
            path.append(end)
            self.paths_with_costs.append((path.copy(), cost))
            path.pop()
            return
        if start not in self.g:
            return
        visited.add(start)
        path.append(start)
        for neighbor, weight in self.g[start]:
            if neighbor not in visited:
                self.dfs_run(neighbor, end, visited, path, cost + weight)
        visited.remove(start)
        path.pop()
    
    def get_best_path(self):
        tmp = {}
        min_cost = float('inf')
        for item in self.paths_with_costs:
            cost = item[1]
            path = item[0]
            if cost < min_cost:
                min_cost = cost
            if cost in tmp:
                tmp[cost].append(path)
            else:
                tmp[cost] = [path]
        if tmp:
            paths = tmp[min_cost]
            length = len(paths)
            min_ind = 0
            last_min = paths[0][-2]
            for each in range(1, length):
                if paths[each][-2] < last_min:
                    last_min = paths[each][-2]
                    min_ind = each
            return paths[min_ind][:-1]
        else:
            return "inf"

    def link_state(self, s, d, m):
        distances = {n:float('inf') for n in self.g}
        tmp = {}
        tmp[s] = 0
        cter = 0
        distances[s] = cter
        predecessors = {node: None for node in self.g}
        if s not in self.g:
            return
        q = [(s, 0)]
        while q:
            (curr, cost) = heapq.heappop(q)
            for vertex, c in self.g[curr]:
                curr_c = c+cost
                if curr_c < distances[vertex]:
                    distances[vertex] = curr_c
                    predecessors[vertex] = curr
                    heapq.heappush(q, (vertex, curr_c))
        self.predecessors = predecessors
        self.distances = distances
        return distances
    
    def forward_tables(self):
        res = []
        for start in self.vertices:
            self.link_state(start, "", "")
            f_t = {start:{'next_hop':start, 'distance':0}}
            for node in self.g:
                if node != start:
                    current_node = node
                    distance = self.distances[node]

                    while current_node and self.predecessors[current_node] != start:
                        current_node = self.predecessors[current_node]

                    f_t[node] = {'next_hop': current_node, 'distance': distance}
            f_t = dict(OrderedDict(sorted(f_t.items())))
            res.append(f_t)
        return res
