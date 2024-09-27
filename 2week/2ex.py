def mmm(n, c=2):
    if n == c:
        print(c)
        return
    if n % c == 0:
        print(c)
        n /= c
        mmm(n)
    else:
        c += 1
        mmm(n, c)


mmm(int(input()))
