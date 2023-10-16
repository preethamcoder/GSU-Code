from collections import deque
class Graph:
    def __init__(self, stuff):
        self.adjlist = stuff if stuff is not None else {}
        self.res = []
    def addVertex(self, vertex):
        if vertex in self.adjlist:
            return
        self.adjlist[vertex] = []
    def addEdge(self, v1, v2):
        if v1 in self.adjlist:
            if v2 not in self.adjlist[v1]:
                self.adjlist[v1].append(v2)
        else:
            self.adjlist[v1] = [v2]
        if v2 in self.adjlist:
            if v1 not in self.adjlist[v2]:
                self.adjlist[v2].append(v1)
        else:
            self.adjlist[v2] = [v1]
    def removeEdge(self, v1, v2):
        if v1 in self.adjlist and v2 in self.adjlist[v1]:
            self.adjlist[v1].remove(v2)
        if v2 in self.adjlist and v1 in self.adjlist[v2]:
            self.adjlist[v2].remove(v1)
    def removeVertex(self, v):
        if v in self.adjlist:
            del self.adjlist[v]
        for each in self.adjlist:
            if v in self.adjlist[each]:
                self.adjlist[each].remove(v)
    def bfs(self, v):
        visited = set()
        res = []
        visited.add(v)
        q = deque([v])
        while q:
            curr = q.popleft()
            res.append(curr)
            for each in self.adjlist[curr]:
                if each not in visited:
                    visited.add(each)
                    q.append(each)
        return res
    def dfs_recur(self, v, visited, res):
        #visited = set()
        if v not in visited:
            res.append(v)
            visited.add(v)
        else:
            return
        for each in self.adjlist[v][::-1]:
            if each not in visited:
                self.dfs_recur(each, visited, res)
        return res
    
    def dfs_iter(self, v):
        visited = set()
        visited.add(v)
        res = [v]
        stack = [v]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                res.append(curr)
                visited.add(curr)
            for each in self.adjlist[curr]:
                if each not in visited:
                    stack.append(each)
        return res
    
    def bfs_f_t(self, start, end):
        q = [[start]]
        while q:
            curr = q.pop(0)
            node = curr[-1]
            if node == end:
                return curr
            if node in self.adjlist:
                for each in self.adjlist[node]:
                    new_path = list(curr)
                    new_path.append(each)
                    q.append(new_path)
    def extract_all_paths_dfs(self, visited, src, end, res):
        visited.add(src)
        res.append(src)
        if src == end:
            print(res)
        else:
            if src in self.adjlist:
                for each in self.adjlist[src]:
                    if each not in visited:
                        self.extract_all_paths_dfs(visited, each, end, res)
        res.pop()
        visited.remove(src)

if __name__ == '__main__':
    cg = Graph({})
    cg.addVertex("A")
    cg.addEdge("A", "B")
    cg.addVertex("C")
    cg.addEdge("A", "C")
    new_g = Graph({'A':['B', 'C'], 'B':['A', 'E'], 'C':['A', 'D'], 'D':['C', 'E'], 'E':['B', 'D']})
    n_g = Graph({'A':['B', 'C'], 'B':['D', 'G'], 'C':['D', 'E'], 'D':['F'], 'E':['F'], 'G':['F']})
    print(new_g.bfs("A"))
    print(n_g.bfs_f_t('A', 'F'))
    print(new_g.adjlist)
    print(new_g.dfs_recur('A', set(), []))
    print(new_g.dfs_iter('A'))
    cg.removeEdge("A", "B")
    print(cg.adjlist)
    cg.removeVertex("C")
    print(cg.adjlist)
    n_g.extract_all_paths_dfs(set(), 'A', 'G', [])