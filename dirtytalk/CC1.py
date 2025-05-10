def _read_graph_as_edges_list(n):
    edges = []
    for i in range(n):
        e = list(map(int,input().split()))
        edges.append(e)
    return edges

def read_graph_as_list(N, oriented = False, weighted = True):
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



buildings_quantity, edges_quantity, virus_quantity = map(int, input().split())
if virus_quantity > 0:
    virus = list(map(int, input().split()))
else:
    virus = []

graph = read_graph_as_list(edges_quantity)
print(graph)
print(graph.keys())
for number_building in range(buildings_quantity):
    if number_building + 1 not in graph.keys():
        graph[number_building + 1] = list()

def dfs_visit(graph, v):
    color[v] = 'gray'
    print(v)
    checked.append(v)

    if graph[v] != list() and v not in virus:
        for u in graph[v]:
            if color[u[0]] == 'white':
                dfs_visit(graph, u[0])


    color[v] = 'black'

good = []
for i in range(buildings_quantity):
    color = {v: 'white' for v in graph.keys()}
    checked = []
    dfs_visit(graph, i+1)
    if len(checked) == buildings_quantity:
        good.append(checked)
    print(checked)
print(good)
if good == list():
    print('impossible')
else:
    s = 10001
    g = 0
    for j in range(len(good)):
            for i in range(buildings_quantity-1):
                for neighbor, weight in graph[good[j][i]]:
                    if neighbor == good[j][i+1]:
                        g += weight
            if  g < s:
                s = g
            g = 0
    print(s)