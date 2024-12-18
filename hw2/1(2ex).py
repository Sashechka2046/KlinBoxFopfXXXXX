a, b = map(str, input().split())
a = int(a)

n = len(b) // a
q = []
d = ''

for i in range(n):
    q.append(b[-1:-a-1:-1])
    b = b[:len(b)-a]

for i in range(len(q)-1, -1, -1):
    d += q[i]
print(d)
