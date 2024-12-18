import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

from hw3.solar_visuals import scale_x


def round_l(num, digits=2):
    if num == 0: return 0
    scale = int(-math.floor(math.log10(abs(num - int(num))))) + digits - 1
    if scale < digits: scale = digits
    return round(num, scale)

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array(list(map(float, '130 & 258 & 389 & 518 & 650 & 781 & 911 & 1032 & 1197 & 1335'.split(' & '))))

plt.figure(figsize=(8,5), dpi=100) # Инициализировать рисунок/Figure dpi -- количество пикселей на дюйм в рисунке figsize -- пропорции "поля" рисунка

k = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2) #МНК:
b = np.mean(y) - np.mean(x) * k

n = len(x)
sk = 1 / n ** 0.5 * ((np.mean(y ** 2) - np.mean(y) ** 2) / (np.mean(x ** 2) - np.mean(x) ** 2) - k ** 2)**0.5
sb = sk * (np.mean(x ** 2) - np.mean(x) ** 2) ** 0.5

x = np.append(x, 0)
plt.plot(x, k*x + b, '-r', label=f'Аппроксимация зависимости частоты от n \n y=kx+b, где k = {round_l(k)} ± {round_l(sk)}, b = {round_l(b)} ± {round_l(sb)}')
x = x[:-1]
plt.scatter(x, y, s=20, color='k', label='Экспериментальные точки')
plt.errorbar(x, y, yerr=0.1, fmt='none', color='blue')

nu = chr(0x03BD)
plt.xlabel('n', color='#1C2833')
plt.ylabel(nu + ', Гц', color='#1C2833')

plt.grid() # сделаем по этим штрихам сетку
plt.legend(loc='upper left') # функция легенды графика для отображения label'ов графиков
#plt.savefig('mygraph1.png', dpi=300) # Можем сохранить график в высоком качестве

plt.show()

# Основные возможные аргументы функции plot. По умолчанию необходимы только x и y
# plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')
# Добавим заголовок (в fontdict нужен словарь, шрифт должен поддерживаться matplotlib'ом)
# plt.title('Our First Graph!', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
# Зададим какие-нибудь корявые "штрихи"/ticks на осях. в эти фунции можно передать любой список
# plt.xticks([0,1.12,2.66,3,3.5])
# plt.yticks([0,2,4,6,8,10])
