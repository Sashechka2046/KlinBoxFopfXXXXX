import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy.io import wavfile
from scipy.fft import ifft

def iterative_fft(x):
    x = np.asarray(x, dtype=complex)
    n = len(x)
    indices = np.arange(n)
    bits = int(np.log2(n))
    indices = indices.reshape((-1, 1)) >> np.arange(bits) & 1
    rev = indices[:, ::-1].dot(1 << np.arange(bits))
    x = x[rev]
    m = 2
    while m <= n:
        wm = np.exp(-2j * pi / m)
        for k in range(0, n, m):
            w = 1
            for j in range(m // 2):
                t = w * x[k + j + m // 2]
                u = x[k + j]
                x[k + j] = u + t
                x[k + j + m // 2] = u - t
                w *= wm
        m *= 2
    return x

signal, data = wavfile.read('o-privet.wav')
data = data.astype(float)
if len(data.shape) > 1:
    data = data[:, 0]

n = 2 ** int(np.ceil(np.log2(len(data))))
padded = np.zeros(n)
padded[:len(data)] = data

fft_data = iterative_fft(padded)

high = fft_data.copy()
high[:int(n * 0.05)] = 0
high[int(n * 0.95):] = 0

end = np.real(ifft(high))[:len(data)]

wavfile.write('high.wav', signal, end.astype(np.int16))

plt.figure(figsize=(12, 6))
plt.subplot(211)
plt.title('Сигнал')
plt.plot(data, color='gray')
plt.subplot(212)
plt.title('Высокие частоты')
plt.plot(end, color='gray')
plt.tight_layout()
plt.show()
