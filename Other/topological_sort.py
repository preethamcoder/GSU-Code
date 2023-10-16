### Topological sort helps you sort actions in succh a way that the parent action always comes before the dependent actions.

def topological_sort(g, visited, stack):
    def helper(g, v, visited, stack):
        visited.add(v)
        for each in g[v]:
            if each not in visited:
                helper(g, each, visited, stack)
        stack.insert(0, v)
    for each in g:
        if each not in visited:
            helper(g, each, visited, stack)
    return stack

if __name__ == '__main__':
    g = {'A':['C'], 'B':['C', 'D'], 'C':['E'], 'D':['F'], 'E':['H', 'F'], 'F':['G'], 'H':[], 'G':[]}
    print(topological_sort(g, set(), []))
