N, M = map(int, input().split())
mx = []
p = []
for j in range(1, N + 1):
    for i in range(1, M + 1):
        p.append(1)
    mx.append(p)
    p = []


def x(mx, N, M, j, c, d=1):
    if d == -1:
        j = j + N + M - 2 - 4 * c
        for i in range(N-1-c, c, d):
            mx[i][c] = j
            j += 1
        return mx
    x(mx, N, M, j, c, d=-1)
    g = M-1-c
    if d == 1:
        for i in range(c, N-1-c, d):
            mx[i][g] = j
            j += 1
        return mx


def y(mx, N, M, j, c, d=1):
    if d == -1:
        j = j + N - c + M - c - 2 - 2 * c
        g = N - c - 1
        for i in range(M-1-c, -1+c, -1):
            mx[g][i] = j
            j += 1
        return mx
    y(mx, N, M, j, c, d=-1)
    if d == 1:
        for i in range(c, M - c, d):
            mx[c][i] = j
            j += 1
        return mx


j = 1
c = 0
while j <= N * M:
    mx = y(mx, N, M, j, c)
    j = mx[c][M-1-c]
    mx = x(mx, N, M, j, c)
    c += 1
    if c > N - 1 or c > M or c < 0:
        break
    else:
        j = mx[c][c-1] + 1
print(*mx, sep="\n")
