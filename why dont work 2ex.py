def mn(n, c=2):
    if n == c:
        return c
    elif n % c == 0:
        n = n / c
        print(c)
        mn(n)
    else:
        c += 1
        mn(n, c)


print(mn(int(input())))
