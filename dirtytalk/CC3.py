def _read_graph_as_edges_list(a, b):
    edges = []
    for i in range(a):
        for j in range(a, a + b):
            e = [i, j]
            edges.append(e)
    return edges

def read_graph_as_list(edges):
    adj_dict = {}
    for e in edges:
        if e[0] not in adj_dict.keys():
            adj_dict[e[0]] = [e[1]]
        else:
            adj_dict[e[0]].append(e[1])
        if e[1] not in adj_dict.keys():
            adj_dict[e[1]] = [e[0]]
        else:
            adj_dict[e[1]].append(e[0])

    return adj_dict

def bipartite(graph):
    colors = {}

    for start in graph.keys():
        if start not in colors:
            queue = [start]
            colors[start] = 0

            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if v not in colors:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    # Если сосед уже окрашен в тот же цвет, граф не двудольный
                    elif colors[v] == colors[u]:
                        return False, []

    set1 = [i for i, j in colors.items() if j == 0]
    set2 = [i for i, j in colors.items() if j == 1]

    return True, (set1, set2)

def kuhn(graph):
    match = {}
    visited = {}
    _, parts = bipartite(graph)
    L = parts[0]
    def dfs(v):
        for u in graph[v]:
            if u not in visited or not visited[u]:
                visited[u] = True
                if u not in match or dfs(match[u]):
                    match[u] = v
                    return True
        return False

    max_matching = 0
    for v in L:
        visited.clear()
        if dfs(v):
            max_matching += 1
    return max_matching

# print(bipartite(G))
# print(kuhn(G))
for i in range(int(input())):
    a, b, c = map(int, input().split())
    all_cuts = list(map(int, input().split()))

    all_edges = _read_graph_as_edges_list(a, b)
    cuted_edges = set((all_cuts[i * 2], a + all_cuts[i * 2 + 1]) for i in range(c))
    all_edges = [edge for edge in all_edges if tuple(edge) not in cuted_edges]

    graph = read_graph_as_list(all_edges)
    # print(graph)
    # print(bipartite(graph))
    print(kuhn(graph))