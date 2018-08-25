import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import math
from qam import moduluj
from utils import podzielDaneNaKanaly

dane = [1,0,1,1,0,1,0,1,0,1,1,1,1,0]
bipolar = lambda x: 1 if x==0 else -1
[I, Q] = podzielDaneNaKanaly(dane, 2)

zmodulowane = moduluj(I, Q)

ofdm = fft.ifft(zmodulowane)
ofdm = ofdm[:len(ofdm)//2]

plt.plot(abs(ofdm))
plt.show()