import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import math

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import utils

# dane = [1,0,1,1, 0,1,0,1, 0,1,1,1, 1,0,0,1, 0,1,1,1, 1,1,1,1, 0,1,1,0, 1,0,0,1]
dane = utils.generujDaneBinarne(1024)
bipolar = lambda x: 1 if x==0 else -1

# BPSK:
bipolarne = [bipolar(d) for d in dane]

# 4 nosne, s/p
podzielone = utils.podziel(bipolarne, ileNaRaz = 4)

kanaly = []
for p in podzielone:
    # todo: to jest jeden duzy symbol
    # nosne powinny byc bardziej rozstrzelone!
    # dlatego dostaje tylko jeden prazek!

    # add zero frequency (DC) as 0 - non existing
    p = [0] + p
    # padding to fulfill nyquist theorem
    while len(p) < 500:
        p.append(0)
    kanal = fft.ifft(p)
    kanaly.append(kanal)

# p/s - sum stuff
suma = [complex(0,0) for i in range(500)]
for kanal in kanaly:
    for i in range(len(kanal)):
        suma[i] += kanal[i]

# todo: chyba dobrze?
plt.plot(suma)
plt.show()

plt.plot(np.abs(fft.fft(suma)))
plt.show()