# b = int(input())
a = list(map(int, input().split()))
t = []

def r(t, a, m):

    if sum(t) == m:
        return t

    if a == []:
        return

    first = r(t.copy(), a[:-1], m)
    if first == None:
        second = r(t.copy() + [a[-1]], a[:-1], m)
        return second
    else:
        return first


if sum(a) % 3 == 0:
    m = sum(a) // 3
    g = r(t, a, m)
    if g != None:
        for i in g:
            a.remove(i)
        g = r(t, a, m)
        if g != None:
            for i in g:
                a.remove(i)
            g = r(t, a, m)
            if g != None:
                print(1)
            else:
                print(0)
        else:
            print(0)
    else:
        print(0)
else:
    print(0)