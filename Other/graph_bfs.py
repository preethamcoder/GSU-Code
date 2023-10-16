from collections import deque
def graph_bfs_video(graph, v):
    visited = set()
    visited.add(v)
    q = deque([v])
    while q:
        curr = q.popleft()
        print(curr)
        for each in graph[curr]:
            if each not in visited:
                visited.add(each)
                q.append(each)

def graphbfs(graph, vertex):
    visited = set()
    res = []
    q = deque([vertex])
    while q:
        curr = q.popleft()
        if curr not in visited:
            visited.add(curr)
            res.append(curr)
        for each in graph[curr]:
            if each not in visited:
                q.append(each)
    '''start = list(graph.keys())[0]
    q = [start]
    while q:
        curr = q.pop(0)
        print(curr)
        if curr not in visited:
            visited.add(curr)
            res.append(curr)
        for each in graph[curr]:
            if each not in visited:
                q.append(each)'''
    return res
def graphdfs(graph, vertex, visited, res):
    if vertex not in visited:
        visited.add(vertex)
        res.append(vertex)
    else:
        return
    for each in graph[vertex]:
        graphdfs(graph, each, visited, res)
    return res

def dfs_iter(graph, vertex):
    visited = set()
    visited.add(vertex)
    res = [vertex]
    stack = [vertex]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            res.append(curr)
            visited.add(curr)
        for each in graph[curr]:
            if each not in visited:
                stack.append(each)
    return res

if __name__ == '__main__':
    g = {'A':['B', 'C'], 'B':['A', 'E'], 'C':['A', 'D'], 'D':['C', 'E'], 'E':['B', 'D']}
    print(graphbfs(g, 'A'))
    graph_bfs_video(g, 'A')
    print(graphdfs(g, 'A', set(), []))
    print(dfs_iter(g, 'A'))