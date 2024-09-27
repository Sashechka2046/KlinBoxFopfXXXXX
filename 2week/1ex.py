def fib(n, c=1, s=0):
    if n == c:
        s += n
        return s
    s += c
    c += 1
    return fib(n, c, s)


print(fib(int(input())))
