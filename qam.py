import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import numpy as np
import random as rand

def getAmplitudes(bits):
    for i in range(len(bits)-1):
        pair = (bits[i],bits[i+1])
        if pair == (0,0):
            yield 1
        elif pair == (0,1):
            yield 3
        elif pair == (1,0):
            yield -1
        else:
            yield -3

def moduluj(dane, nosna):
    out=[]
    for ampl in getAmplitudes(dane):
        for n in nosna:
            out.append(ampl*n)
    return out

t = np.arange(start=0, stop=1, step=0.01)
cosinus = np.cos(2*np.pi*2*t)
sinus = np.sin(2*np.pi*2*t)

I = [1,0,1,0,0,1]
Q = [0,0,1,0,1,1]

modI = moduluj(I, cosinus)
modQ = moduluj(Q, sinus)

zmodulowany = modI + modQ
plt.plot(zmodulowany)
plt.show()