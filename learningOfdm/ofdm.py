import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import random

# ofdm + qpsk

def generujDaneBinarne(ile):
    out = []
    ile//2
    bipolar = lambda x: 1 if x>=0.5 else -1
    for _ in range(ile):
        bitI = bipolar(random.random())
        bitQ = bipolar(random.random())
        out.append(complex(bitI, bitQ)) 
    return out

def moduluj(bity):
    addPadding(bity)
    return fft.ifft(bity)

def addPadding(tab):
    # to jest w celu dostosowania bitow do nyquista i IFFT w OFDM
    # tab = [0] + tab
    tab[0]=0
    dl = len(tab)*10

    for _ in range(dl):
        tab.append(0)

dlugoscStrumienia = 10

bity = [generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),]

out=[]
zmodulowane = []
for strumien in bity:
    zmodulowany = moduluj(strumien)
    zmodulowane.append(zmodulowany)
    for x in zmodulowany:
        out.append(x)

plt.subplot(2,1,1)
plt.plot(np.real(out))

plt.subplot(2,1,2)
plt.plot(np.abs(np.fft.fft(out[:len(out)//2])))
plt.show()


# pojedyncze bity i nosne
strumien = generujDaneBinarne(4)
strumien[0]=0
plt.subplot(2,1,1)
plt.stem(strumien)

for i,b in enumerate(strumien):
    nosna = [0 for _ in range(80)]
    nosna[i] = b
    zmodulowanySymbol = fft.ifft(nosna)
    plt.subplot(2,1,2)
    plt.plot(zmodulowanySymbol)
    
plt.show()
