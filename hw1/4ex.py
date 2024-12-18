def curcurcur(size, symbol, s=1):
    if size // 2 + 1 == s and size % 2 != 0:
        print(symbol * s)
        return
    elif size // 2 == s and size % 2 == 0:
        print(symbol * s)
        print(symbol * s)
        return
    print(symbol * s)
    curcurcur(size, symbol, s+1)
    print(symbol * s)
    return


a, b = map(str, input().split())
curcurcur(int(a), b)
