def _read_graph_as_edges_list(n):
    edges = []
    for i in range(n):
        e = list(map(int,input().split()))
        edges.append(e)
    return edges

def read_graph_as_list(N, oriented = True, weighted = False):
    edges = _read_graph_as_edges_list(N)
    adj_dict = {}
    if weighted:
        if oriented:
            for e in edges:
                if e[0] not in adj_dict.keys():
                    adj_dict[e[0]] = [[e[1], e[2]]]
                else:
                    adj_dict[e[0]].append([e[1], e[2]])
        else:
            for e in edges:
                if e[0] not in adj_dict.keys():
                    adj_dict[e[0]] = [[e[1], e[2]]]
                else:
                    adj_dict[e[0]].append([e[1], e[2]])
                if e[1] not in adj_dict.keys():
                    adj_dict[e[1]] = [[e[0], e[2]]]
                else:
                    adj_dict[e[1]].append([e[0], e[2]])
    else:
        if oriented:
            for e in edges:
                if e[0] not in adj_dict.keys():
                    adj_dict[e[0]] = [e[1]]
                else:
                    adj_dict[e[0]].append(e[1])
        else:
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

def dfs_visit(graph, v):
    color[v] = 'gray'
    print(v)

    for u in graph.get(v, []):
        if color[u] == 'white':
            dfs_visit(graph, u)

    color[v] = 'black'

def TopSortDFS(G,v, color, topsorted):
    color[v] = 'gray'
    global Flash
    TUTU = False
    if len(graph.get(v, [])) != 1:
        TUTU = True
    for u in graph.get(v, []):
        if color[u] == 'gray':
            return False
        if color[u] == 'black' or TUTU:
            Flash = True
        if color[u] == 'white':
            if not TopSortDFS(G,u, color, topsorted):
                return False

    color[v] = 'black'
    topsorted.append(v)
    return True

def TopSort(G):
    color = {i: 'white' for i in G.keys()}
    topsorted = []
 #   global Flash

    for v in G.keys():
        if color[v] == 'white':
            if not TopSortDFS(G,v, color, topsorted):
                return None
    return topsorted[::-1]

V, E = map(int, input().split())
"""
3 2
1 2
2 3
"""

graph = read_graph_as_list(E)

color = ['white' for i in graph.keys()]
Flash = False

for i in range(1, V + 1):
    if i not in graph:
        graph[i] = []

ans = TopSort(graph)


if not ans:
    print(-1)
else:
    for i in range(len(ans) - 1):
        if ans[i + 1] not in graph[ans[i]]:
            print("NO")
            exit()
    print("YES")