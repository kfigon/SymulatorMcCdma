import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import random

def generujDaneBinarne(ile):
    out = []
    for _ in range(ile):
        bit = 1 if random.random() >=0.5 else -1
        out.append(bit) 
    return out

def moduluj(bity):
    addPadding(bity)
    return fft.ifft(bity)

def addPadding(tab):
    # to jest w celu dostosowania bitow do nyquista i IFFT w OFDM
    # tab = [0] + tab
    dl = len(tab)*30

    for _ in range(dl):
        tab.append(0)

dlugoscStrumienia = 20

bity = [generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),]

out=[]
for strumien in bity:
    zmodulowany = moduluj(strumien)
    for x in zmodulowany:
        out.append(x)

plt.subplot(2,1,1)
plt.plot(np.real(out))

plt.subplot(2,1,2)
plt.plot(np.abs(np.fft.fft(out[:len(out)//2])))
plt.show()
