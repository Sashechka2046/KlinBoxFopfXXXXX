def sd(a, b):
    d = []
    c = 0
    l1 = []
    while c != a:
        c += 1
        if a % c == 0:
            l1.append(c)
    c = 0
    while c != b:
        c += 1
        if b % c == 0 and c in l1:
            d.append(c)
    d = max(d)
    return d


def sxy(a, b, d):
    x1 = 0
    x2 = 0
    while True:
        y = - a * x1 / b + d / b
        if y % 1 == 0:
            yt1 = y
            xt1 = x1
            break
        x1 += 1
        x2 -= 1
        y = - a * x2 / b + d / b
        if y % 1 == 0:
            yt1 = y
            xt1 = x2
            break
    s1 = abs(xt1) + abs(yt1)
    y1 = 0
    y2 = 0
    while True:
        x = - b * y1 / a + d / a
        if x % 1 == 0:
            yt2 = y1
            xt2 = x
            break
        y1 += 1
        y2 -= 1
        x = - b * x2 / a + d / a
        if x % 1 == 0:
            yt2 = y2
            xt2 = x
            break
    s2 = abs(xt2) + abs(yt2)
    if s2 > s1:
        return xt1, yt1
    if s2 < s1:
        return xt2, yt2
    if s2 == s1:
        if xt1 < xt2:
            return xt1, yt1
        if xt1 >= xt2:
            return xt2, yt2


a, b = map(int, input().split())
d = sd(a, b)
x, y = sxy(a, b, d)
print(int(x), int(y), d, sep=" ")
