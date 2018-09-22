import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import random
from transmiterOfdm import TransmiterOfdm
from przetwornikSP import PrzetwornikSzeregowoRownolegly
from koderTurbo import *
import utils


symboleBipolarne = utils.generujSymboleBipolarneZespolone(40)
pSP = PrzetwornikSzeregowoRownolegly(4)

strumienie = pSP.rozdziel(symboleBipolarne)

transmiter = TransmiterOfdm(10)

zmodulowany = []
for strumien in strumienie:
    zmodulowanyStrumien = transmiter.modulujStrumien(strumien)
    for x in zmodulowanyStrumien:
        zmodulowany.append(x)


# plt.subplot(2,1,1)
# plt.plot(np.real(zmodulowany))

# plt.subplot(2,1,2)
# plt.plot(np.abs(fft.fft(zmodulowany[:len(zmodulowany)//2])))
# plt.show()

odebraneStrumienie = pSP.rozdziel(zmodulowany)
zdemodulowane = []
for strumien in odebraneStrumienie:
    zdemodulowanyStrumien = transmiter.demoduluj(strumien)
    zdemodulowane.append(zdemodulowanyStrumien)

for i in range(len(strumienie)):
    assert zdemodulowane[i] == strumienie[i]
print("yeah")

