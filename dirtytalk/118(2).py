import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))  # Увеличиваем размер фигуры

# Увеличиваем размер цифр на осях
plt.tick_params(axis='both', which='major', labelsize=14)  # Установите нужный размер
plt.xlabel('t_n, с', fontsize=14)
plt.ylabel('nl/t_n, м/с', fontsize=14)

x = np.array([0.11765, 0.20725, 0.28384, 0.35055, 0.4109])
y = np.array([3.24, 3.68, 4.03, 4.36, 4.64])
sigmax = [0.00042, 0.00021, 0.00069, 0.00153, 0.00127]
sigmay = [0.054, 0.052, 0.063, 0.076, 0.075]

plt.errorbar(x, y, xerr=sigmax, yerr=sigmay, fmt="o", color='k', capsize=5)

sxy = 0
sx = 0
sy = 0
sx2 = 0

for i in range(len(x)):
    sxy += x[i] * y[i]
    sx += x[i]
    sy += y[i]
    sx2 += x[i] ** 2

k = (len(x) * sxy - sx * sy) / (len(x) * sx2 - sx ** 2)
b = (sy - k * sx) / len(x)

plt.plot(x, k * x + b, '-r')
print(k, b)

plt.grid()
plt.show()
