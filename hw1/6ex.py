import numpy as np
x = np.array(list(map(int, input().split())))
y = np.array(list(map(int, input().split())))
k = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
b = np.mean(y) - np.mean(x) * k
print(k)
print(b)
