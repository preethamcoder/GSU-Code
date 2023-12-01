from graph import *

def read_topology(file_name):
    file = open(file_name, 'r')
    data = file.readlines()
    g = Graph(data)
    file.close()
    return g

def read_soruce_and_dest(file_name):
    file = open(file_name, 'r')
    data = file.readlines()
    res = []
    for line in data:
        pieces = line.split()
        s = pieces[0]
        d = pieces[1]
        message = ' '.join(pieces[2:])
        res.append([s, d, message])
    file.close()
    return res

def read_changes(file_name):
    file = open(file_name, 'r')
    data = file.readlines()
    res = []
    for line in data:
        pieces = line.split()
        s = pieces[0]
        d = pieces[1]
        weight = int(pieces[2])
        res.append([s, d, weight])
    file.close()
    return res

def get_f_t(grr):
    tab = grr.forward_tables()
    return tab

def tables(grr, s, d):
    grr.dfs_run(s, d, set(), [], 0)
    p = grr.get_best_path()
    grr.paths_with_costs = []
    return p

def l_s(grr, operation):
    s, d, m = operation
    res = grr.link_state(s, d, m)
    p = tables(grr, s, d)
    if res:
        if d in res and res[d] != float('inf'):
            return f"from {s} to {d} cost {res[d]} hops {' '.join(p)} message {m}\n"
    return f"from {s} to {d} cost infinite hops unreachable message {m}\n"

if __name__ == '__main__':
    c = 0
    output = open("output.txt", 'w')
    gr = read_topology("topofile.txt")
    s_d_m = read_soruce_and_dest("messagefile.txt")
    get_tabs = get_f_t(gr)
    for t in get_tabs:
        for key, vals in t.items():
            string = "Node: "+key+"\t"+"Next_Hop: "+vals['next_hop']+"\t"+f"Cost: {vals['distance']}"
            output.write(string)
            output.write('\n')
        output.write('\n')
    for op in s_d_m:
        r = l_s(gr, op)
        output.write(r)
    s_d_w = read_changes("changesfile.txt")
    for op in s_d_w:
        r = gr.add_edge(op)
        get_tabs = get_f_t(gr)
        c += 1
        output.write('\n'+f"------ At this point, change {c} is added\n")
        for t in get_tabs:
            for key, vals in t.items():
                string = "Node: "+key+"\t"+"Next_Hop: "+vals['next_hop']+"\t"+f"Cost: {vals['distance']}"
                output.write(string)
                output.write('\n')
            output.write('\n')
        for every in s_d_m:
            result = l_s(gr, every)
            output.write(result)
    output.close()