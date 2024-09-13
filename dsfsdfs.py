n = 111111
g = 0
k = 0
while n != 0:
    l = n % 10
    g += l * 2 ** k
    n = n // 10
    k += 1
print(g)