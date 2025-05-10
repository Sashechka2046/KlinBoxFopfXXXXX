def _read_graph_as_edges_list(n):
    edges = []
    points = []
    for i in range(n):
        a, b = map(int, input().split())
        points.append((a, b))
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            weight = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            edges.append([i + 1, j + 1, weight])
    return edges

# def read_graph_as_list(N):
#     edges = _read_graph_as_edges_list(N)
#     adj_dict = {}
#     for e in edges:
#         if e[0] not in adj_dict.keys():
#             adj_dict[e[0]] = [[e[1], e[2]]]
#         else:
#             adj_dict[e[0]].append([e[1], e[2]])
#         if e[1] not in adj_dict.keys():
#             adj_dict[e[1]] = [[e[0], e[2]]]
#         else:
#             adj_dict[e[1]].append([e[0], e[2]])
#
#     return adj_dict


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    xroot = find(x)
    yroot = find(y)
    if xroot == yroot:
        return False
    if ranks[xroot] < ranks[yroot]:
        parents[xroot] = yroot
    else:
        parents[yroot] = xroot
        if ranks[xroot] == ranks[yroot]:
            ranks[xroot] += 1
    return True

for i in range(int(input())):
    points_quantity = int(input())

    edges = _read_graph_as_edges_list(points_quantity)
#    print(edges)

    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(points_quantity + 1)]
    ranks = [0] * (points_quantity + 1)

    s = 0
    g = 0
    for a, b, weight in edges:
        if union(a,b):
            s += weight
            g += 1
        if g == points_quantity - 1:
            break
    if g == points_quantity - 1:
        print(f"{s:.2f}")
    else:
        print('impossible')