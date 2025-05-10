# 1 3
# 1 2
# 2 4
# 5 4
def _read_graph_as_edges_list(n):
    edges = []
    for i in range(n):
        e = list(map(int,input().split()))
        edges.append(e)
    return edges
# 0 1 0
# 0 0 1
# 1 0 0
def _read_graph_as_matrix(n):
    M = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        row = list(map(int, input().split()))
        M[i] = row
    return M

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

def read_graph_as_matrix(N, weighted = False):
    M = _read_graph_as_matrix(N)
    adj_dict = {}
    if weighted:
        for i in range(len(M)):
            adj_dict[i] = []
            for j in range(len(M[i])):
                if M[i][j]:
                    adj_dict[i].append([j, M[i][j]])
    else:
        for i in range(len(M)):
            adj_dict[i] = []
            for j in range(len(M[i])):
                if M[i][j]:
                    adj_dict[i].append(j)

    return adj_dict


# {1: [[2,3],[3,4],[4,5]]}
