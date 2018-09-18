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
    dl = len(tab)*2
    for _ in range(dl):
        tab.append(0)

dlugoscStrumienia = 50

bity = [generujDaneBinarne(dlugoscStrumienia)]

out=[]
for strumien in bity:
    zmodulowany = moduluj(strumien)
    for x in zmodulowany:
        out.append(x)

plt.subplot(2,1,1)
plt.plot(np.real(out))

plt.subplot(2,1,2)
plt.stem(np.abs(np.fft.fft(out[:len(out)//2])))
plt.show()

# plt.subplot(2,1,1)
# plt.plot(np.real(sinusy))

# plt.subplot(2,1,2)
# plt.plot(np.imag(sinusy))
# plt.show()