# рассчёты
a = [0.11778, 0.20729, 0.2838, 0.35047, 0.41096]
for i in range(1, 6):
    print(round(0.3816*i/a[i-1], 5), end='&')

print(list(map(float, input().split('&'))))
