def _read_graph_as_edges_list(a, b):
    T = False
    E = 1
    B = 0
    j = 1
    edges = [[0, a]]
    while not T:
        for i in range(B, E):
            papa = edges[i][1]
            if papa == b:
                T = True
                break
            if 9999 >= papa >= 1:
                e = [papa, papa - 2]
                edges.append(e)
                e = [papa, papa * 3]
                edges.append(e)
                c = 0
                qu = papa
                while qu:
                    c += qu % 10
                    qu //= 10
                e = [papa, papa + c]
                edges.append(e)

        B = E
        E += 3 ** j
        j += 1
    edges.pop(0)
    return edges


def read_graph_as_list(a, b):
    edges = _read_graph_as_edges_list(a, b)
    adj_dict = {}
    for e in edges:
        if e[0] not in adj_dict.keys():
            adj_dict[e[0]] = [e[1]]
        else:
            adj_dict[e[0]].append(e[1])
    return adj_dict

def bfs_shortest_way(graph, start):
    queue = [start]
    dist = {start: 0}
    parent = {start: None}

    while queue:
        v = queue.pop(0)
        if v == end:
            break

        for u in graph.get(v, []):
            if u not in dist:
                dist[u] = dist[v] + 1
                parent[u] = v
                queue.append(u)

    return parent

def get_path(parent, end):
    s = 0
    while end != None:
        s += 1
        end = parent[end]
    return s


start, end = map(int, input().split())
path = get_path(bfs_shortest_way(read_graph_as_list(start, end), start), end)

print(path-1)
