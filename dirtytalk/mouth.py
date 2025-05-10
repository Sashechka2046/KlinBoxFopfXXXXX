import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize =(6,4),dpi=200)
m = np.array([0, 461.8, 504.0, 467.5, 466.3, 502.9, 510.6])
for i in range(1,len(m)):
    m[i]+= m[i-1]
latun = np.array([9.77, 8.67, 7.53, 6.27, 5.13, 3.90, 2.65])
stal = np.array([6.54, 5.92, 5.29, 4.60, 3.95 ,3.26, 2.53])
tree = np.array([8.58, 8.19, 7.79, 7.37, 6.97, 6.55, 6.12])
a = np.polyfit(m*0.001*9.8,latun,1)
b = np.polyfit(m*0.001*9.8,stal,1)
c = np.polyfit(m*0.001*9.8,tree,1)
print(a[0],b[0],c[0])
f = m*0.001*9.8
ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])
ax.set_xlabel('P, Н')
ax.set_ylabel('l, м * 10^-3')
ax.scatter(f, latun,s=20,color='k',label='Экспериментальные точки латуни')
ax.scatter(f, stal,s=20,color='b',label='Экспериментальные стали стали')
ax.scatter(f, tree,s=20,color='g',label='Экспериментальные точки дерева')
ax.plot(f,a[0]*f+a[1],'-r',label='Аппроксимация зависимости отклонения от нагрузки у латуни')
ax.plot(f,b[0]*f + b[1],'-g',label='Аппроксимация зависимости отклонения от нагрузки у стали')
ax.plot(f,c[0]*f + c[1],'-b',label='Аппроксимация зависимости отклонения от нагрузки у дерева')
ax.legend(loc='upper left', fontsize=7.5)
ax.grid()
plt.show()