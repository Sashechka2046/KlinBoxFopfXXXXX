"""import numpy as np
import matplotlib.pyplot as plt
x = [1, 2]
y = [3, 4]

fig = plt.figure(figsize=(8,5), dpi=100)

plt.plot(x,y, 'b^--', label='2x')

x2 = np.arange(0,4.5,0.05)

plt.plot(x2, x2**2, 'r--', label='X^2')

# plt.xticks() штрихи
# plt.xlabel() подпись осей

plt.title('Our first graph!', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.legend()
plt.grid()
plt.savefig('mygraph.png', dpi=300)
plt.show()

# ax1 = fig.add_subplot(213) 2 - строк 1 - столбцов 3 - индекс

plt.errorbar(x,y, yerr=0.2, xerr=0.1, color='k', linestyle='None')
"""
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('iris_data.csv')
# plt.hist(list(df['SepalLengthCm']), 50)
# plt.show()

'''
sw = list(df[''])
sl
pw
pl
spec
fig = plt.figu
ax1 = fig.add_
ax1.plot(sw,pl, '.') - таких six
'''
a = dict()
a[(1,2)] = 'xxx'
print(a[(1,2)])

b = set()
b.add(4)
b.add(5)
b.add(4)
b.add((4,3))
print(b)
