from collections import deque


def read_graph_as_list(N, k, x, M):
    edges = _read_graph_as_edges_list(N, k, x, M)
    adj_dict = {}
    for e in edges:
        if e[0] not in adj_dict:
            adj_dict[e[0]] = {}
        adj_dict[e[0]][e[1]] = adj_dict[e[0]].get(e[1], 0) + e[2]
        if e[1] not in adj_dict:
            adj_dict[e[1]] = {}
        adj_dict[e[1]][e[0]] = adj_dict[e[1]].get(e[0], 0)
    return adj_dict


def _read_graph_as_edges_list(N, k, x, M):
    edges = []
    istok = 4 * N + 1
    stok = 4 * N + 2

    for i in range(N):
        e = [istok, i, x]
        edges.append(e)

    for i in range(N):
        e = [3 * N + i, stok, x]
        edges.append(e)

    for i in range(N):
        e = [i, N + i, k]
        edges.append(e)
        e = [2 * N + i, 3 * N + i, k]
        edges.append(e)

    for i in range(N):
        for j in range(N):
            if M[i][j] == 1:
                e = [i, 3 * N + j, 1]
                edges.append(e)
            if M[i][j] == 0:
                e = [N + i, 2 * N + j, 1]
                edges.append(e)
    return edges


def max_flow(graph, s, t):
    residual = {u: {v: graph[u][v] for v in graph[u]} for u in graph}
    flow = 0

    while True:
        parent = {}
        visited = set()
        queue = deque([s])
        visited.add(s)
        found = False

        while queue:
            u = queue.popleft()
            for v in residual[u]:
                if v not in visited and residual[u][v] > 0:
                    parent[v] = u
                    visited.add(v)
                    queue.append(v)
                    if v == t:
                        found = True
                        break
            if found:
                break
        if not found:
            break 

        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] = residual[v].get(u, 0) + path_flow 
            v = u

        flow += path_flow

    return flow


N, k = map(int, input().split())
pro_druzbu = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    pro_druzbu[i] = list(map(int, input().strip()))

for x in range(1, N + 2):
    graph = read_graph_as_list(N, k, x, pro_druzbu)
    if max_flow(graph, 4 * N + 1, 4 * N + 2) != N * x:
        print(x - 1)
        break
