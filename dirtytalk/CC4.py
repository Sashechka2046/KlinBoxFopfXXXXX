def _read_graph_as_matrix(n):
    M = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        row = list(map(int, list(input().strip())))
        M[i] = row

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((i, j, M[i][j]))
    return edges

 # def read_graph_as_matrix(N, weighted = True):
 #    M = _read_graph_as_matrix(N)
 #    adj_dict = {}
 #    for i in range(len(M)):
 #        adj_dict[i] = []
 #        for j in range(len(M[i])):
 #            if M[i][j]:
 #                adj_dict[i].append([j, M[i][j]])
 #    return adj_dict

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        # Поиск с сжатием пути
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

def pochti_kruskal(n, edges):
    dsu = DSU(n)
    edges.sort(key=lambda x: x[2])
    s = 0
    for a, b, weight in edges:
        if not dsu.union(a, b):
            s += weight

    return s

cities_quality = int(input())

print(pochti_kruskal(cities_quality, _read_graph_as_matrix(cities_quality)))
