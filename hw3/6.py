import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from tkinter import *
from tkinter import filedialog, ttk


# def round_l(num, digits=2):
#     if num == 0: return 0
#     scale = int(-math.floor(math.log10(abs(num - int(num))))) + digits - 1
#     if scale < digits: scale = digits
#     return round(num, scale)

df = pd.read_csv('GRAS.csv')

x = np.array(list(df['x']))
y = np.array(list(df['y']))
x_error = np.array(list(df['x_error']))
y_error = np.array(list(df['y_error']))

def graph():
    global x, y, x_error, y_error
    k = (np.mean(x*y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2) #МНК:
    b = np.mean(y) - np.mean(x) * k

    n = len(x)
    sk = 1 / n ** 0.5 * ((np.mean(y ** 2) - np.mean(y) ** 2) / (np.mean(x ** 2) - np.mean(x) ** 2) - k ** 2)**0.5
    sb = sk * (np.mean(x ** 2) - np.mean(x) ** 2) ** 0.5

    plt.figure(figsize=(8,5), dpi=100) # Инициализировать рисунок/Figure dpi -- количество пикселей на дюйм в рисунке figsize -- пропорции "поля" рисунка

    x = np.append(x, 0)
    plt.plot(x, k*x + b, '-r', label=f'Аппроксимация зависимости u^2 от F \n y=kx+b, где k = {k} ± {sk}, b = {b} ± {sb}')
    x = x[:-1]
    plt.scatter(x, y, s=40, color='k', label='Экспериментальные точки')
    plt.errorbar(x, y, xerr=x_error, yerr=y_error, fmt='none', color='w', )

    plt.xlabel('F, Н', color='#1C2833')
    plt.ylabel( 'u^2, м^2/c^2', color='#1C2833')

    plt.grid() # сделаем по этим штрихам сетку
    plt.legend(loc='upper left') # функция легенды графика для отображения label'ов графиков
    plt.savefig('mygraph1.png', dpi=300) # Можем сохранить график в высоком качестве
    print(k, b, sk, sb)

    plt.show()



root = Tk()
root.title("Построить график и рассчитать МНК")
root.minsize(width=250, height=70)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# ttk.Label(mainframe, textvariable=GRA).grid(column=2, row=2, sticky=(W, E))

# косметические подписи, обратите внимание на расположение
ttk.Label(mainframe, text="k см. в консоли").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="b см. в консоли").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="y=kx+b").grid(column=1, row=3, sticky=W)

def open_file_dialog():
    global x, y, x_error, y_error
    in_filename = filedialog.askopenfilename(filetypes=[("CSV files", ".csv")])
    if in_filename:
        df = pd.read_csv(in_filename)
        x = np.array(list(df['x']))
        y = np.array(list(df['y']))
        x_error = np.array(list(df['x_error']))
        y_error = np.array(list(df['y_error']))
        print("да!")

ttk.Button(mainframe, text="Открыть файл", command=open_file_dialog).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="Build!", command=graph).grid(column=3, row=3, sticky=W)

# этот цикл позволяет "разбросать" элементы подальше друг от друга
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось calculate
root.bind("<Return>", graph)

# циклим наше окно
root.mainloop()