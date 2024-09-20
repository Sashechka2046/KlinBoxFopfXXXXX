def triangle(h, depth = 1, n = 'L'):
    if h % 2 != 0 and depth == h // 2 + 1:
        print(n * depth)
        return
    if h % 2 == 0 and depth == h // 2:
        print(n * depth)
        print(n * depth)
        return
    print(n * depth)
    triangle(h, depth = depth + 1)
    print(n * depth)
triangle(8)