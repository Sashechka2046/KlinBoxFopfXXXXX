"""
# расстояние ливенштейна удаление замена
# добавление три операции чтобы из одной строки
# получить вторую

a = 'aasd'
b = 'asdasd'
c = a
a = b
b = c


def levenstein(a, b):
    len_a = len(a)
    len_b = len(b)
    res = [[-1 for i in range(len_a+1)] for j in range(len_b+1)]
    k = 0
    for i in range(len_a+1):
        res[0][i] = k
        k += 1
    k = 0
    for i in range(len_b+1):
        res[i][0] = k
        k += 1
    for j in range(1, len_a+1):
        for i in range(1, len_b+1):
            if b[i-1] == a[j-1]:
                res[i][j] = min(res[i-1][j] + 1, res[i][j-1] + 1, res[i-1][j-1])
            else:
                res[i][j] = min(res[i - 1][j] + 1, res[i][j - 1] + 1, res[i - 1][j - 1] + 1)
    for i in res:
        print(*i)


levenstein(a, b)
"""
