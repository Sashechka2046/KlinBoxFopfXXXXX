b = int(input())
a = list(map(int, input().split()))
# print(a)
t = []
t.extend(a)

if sum(a) % 3 == 0:
    m = sum(a) // 3
    # print(m)
    c = 0
    for j in range(b):
        for i in range(j, b):
            if c + a[i] <= m:
                c += a[i]
                t.remove(a[i])
        if c == m:
            break
        else:
            t = []
            t.extend(a)
            c = 0
    a =[]
    a.extend(t)
    # print(sum(a))
    # print(a)
    c = 0
    d = []
    d.extend(a)
    if sum(a) % (2 * m) == 0:
        for j in range(len(a)):
            for i in range(j, len(a)):
                if c + a[i] <= m:
                    c += a[i]
                    d.remove(a[i])
            if c == m:
                break
            else:
                d = []
                d.extend(a)
                c = 0

        if sum(d) % m == 0 and d != a:
            print(1)
        else:
            print(0)
    else:
        print(0)
else:
    print(0)