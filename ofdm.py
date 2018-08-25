import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import math
from utils import podziel

dane = [1,0,1,1, 0,1,0,1, 0,1,1,1, 1,0,0,1, 0,1,1,1, 1,1,1,1, 0,1,1,0, 1,0,0,1]
bipolar = lambda x: 1 if x==0 else -1

# BPSK:
bipolarne = [bipolar(d) for d in dane]

# 4 nosne, s/p
podzielone = podziel(bipolarne, ileNaRaz = 4)

kanaly = []
for p in podzielone:
    # add zero frequency (DC) as 0 - non existing
    p = [0] + p
    # padding to fulfill nyquist theorem
    while len(p) < 8:
        p.append(0)
    kanal = fft.ifft(p)
    kanaly.append(kanal)

# p/s - sum stuff
suma = [complex(0,0) for i in range(8)]
for kanal in kanaly:
    for i in range(len(kanal)):
        suma[i] += kanal[i]

# todo: dobrze?
plt.plot(suma)
plt.show()

