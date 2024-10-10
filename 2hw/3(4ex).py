import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('iris_data (1).csv')

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax6 = fig.add_subplot(326)

ax1.scatter(list(df['SepalLengthCm']), list(df['SepalWidthCm']), s=6, c='r', marker='x')
ax2.scatter(list(df['SepalLengthCm']), list(df['PetalLengthCm']), s=6, c='m', marker='p')
ax3.scatter(list(df['SepalLengthCm']), list(df['PetalWidthCm']), s=6, c='g', marker='>')
ax4.scatter(list(df['SepalWidthCm']), list(df['PetalLengthCm']), s=6, c='c', marker='^')
ax5.scatter(list(df['SepalWidthCm']), list(df['PetalWidthCm']), s=6, c='b', marker='v')
ax6.scatter(list(df['PetalLengthCm']), list(df['PetalWidthCm']), s=15, c='y', marker='.')

x, y = np.array(df['SepalLengthCm']), np.array(df['SepalWidthCm'])
k = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
b = np.mean(y) - np.mean(x) * k
ax1.plot([4, 8], [k * 4 + b, k*8 + b], label=f'{round(k, 2)}, {round(b, 2)}')
ax1.legend()
x, y = np.array(df['SepalLengthCm']), np.array(df['PetalLengthCm'])
k = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
b = np.mean(y) - np.mean(x) * k
ax2.plot([4, 8], [k * 4 + b, k*8 + b], label=f'{round(k, 2)}, {round(b, 2)}')
ax2.legend()
x, y = np.array(df['SepalLengthCm']), np.array(df['PetalWidthCm'])
k = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
b = np.mean(y) - np.mean(x) * k
ax3.plot([4, 8], [k * 4 + b, k * 8 + b], label=f'{round(k, 2)}, {round(b, 2)}')
ax3.legend()
x, y = np.array(df['SepalWidthCm']), np.array(df['PetalLengthCm'])
k = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
b = np.mean(y) - np.mean(x) * k
ax4.plot([2, 4], [k * 2 + b, k * 4 + b], label=f'{round(k, 2)}, {round(b, 2)}')
ax4.legend()
x, y = np.array(df['SepalWidthCm']), np.array(df['PetalWidthCm'])
k = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
b = np.mean(y) - np.mean(x) * k
ax5.plot([2, 4], [k * 2 + b, k * 4 + b], label=f'{round(k, 2)}, {round(b, 2)}')
ax5.legend()
x, y = np.array(df['PetalLengthCm']), np.array(df['PetalWidthCm'])
k = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
b = np.mean(y) - np.mean(x) * k
ax6.plot([1, 7], [k * 1 + b, k * 7 + b], label=f'{round(k, 2)}, {round(b, 2)}')
ax6.legend()

plt.show()
