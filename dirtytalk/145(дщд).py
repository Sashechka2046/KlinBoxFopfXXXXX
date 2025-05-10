import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

def round_l(num, digits=2):
    if num == 0: return 0
    scale = int(-math.floor(math.log10(abs(num - int(num))))) + digits - 1
    if scale < digits: scale = digits
    return round(num, scale)

x = np.array(list(map(float, '0.0125 & 0.0100 & 0.0081 & 0.0064 & 0.0049 & 0.0042'.split(' & '))))
y = np.array(list(map(float, '10.61 & 8.92 & 7.82 & 6.95 & 5.50 & 5.01'.split(' & '))))
x_error = list(map(float, '0.0002 & 0.0002 & 0.0002 & 0.0002 & 0.0001 & 0.0001'.split(' & ')))
y_error = list(map(float, '0.01 & 0.02 & 0.02 & 0.02 & 0.01 & 0.01'.split(' & ')))

plt.figure(figsize=(8,5), dpi=100) # Инициализировать рисунок/Figure dpi -- количество пикселей на дюйм в рисунке figsize -- пропорции "поля" рисунка

k = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2) #МНК:
b = np.mean(y) - np.mean(x) * k

n = len(x)
sk = 1 / n ** 0.5 * ((np.mean(y ** 2) - np.mean(y) ** 2) / (np.mean(x ** 2) - np.mean(x) ** 2) - k ** 2)**0.5
sb = sk * (np.mean(x ** 2) - np.mean(x) ** 2) ** 0.5

x = np.append(x, 0)
plt.plot(x, k*x + b, '-r', label=f'Аппроксимация зависимости T^2 от l^2 \n y=kx+b, где k = {round_l(k)} ± {round_l(sk)}, b = {round_l(b)} ± {round_l(sb)}')
x = x[:-1]
plt.scatter(x, y, s=40, color='k', label='Экспериментальные точки')
plt.errorbar(x, y, xerr=x_error, yerr=y_error, fmt='none', color='b', )

plt.xlabel('l^2, м^2', color='#1C2833')
plt.ylabel( 'T^2, c^2', color='#1C2833')

plt.grid() # сделаем по этим штрихам сетку
plt.legend(loc='upper left') # функция легенды графика для отображения label'ов графиков
#plt.savefig('mygraph1.png', dpi=300) # Можем сохранить график в высоком качестве

plt.show()

