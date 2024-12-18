import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('BTC_data.csv')

k = list(df['time'])
for i in range(len(k)):
    k[i] = k[i][8:10] + k[i][4:8] + k[i][:4]
plt.plot(k, np.array(df['close']))
plt.show()
