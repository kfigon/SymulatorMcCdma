import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import numpy as np
import random as rand
from utils import podzielDaneNaKanaly

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

def modulujKanal(dane, nosna):
    out=[]
    for ampl in getAmplitudes(dane):
        for n in nosna:
            out.append(ampl*n)
    return out

def moduluj(I, Q):
    t = np.arange(start=0, stop=1, step=0.01)
    cosinus = np.cos(2*np.pi*2*t)
    sinus = np.sin(2*np.pi*2*t)

    modI = modulujKanal(I, cosinus)
    modQ = modulujKanal(Q, sinus)

    return modI + modQ

def main():
    dane = [1,0,0,0,1,1,0,0,0,1,1,1]
    podzielone = podzielDaneNaKanaly(dane, ileKanalow=2)
    I = podzielone[0]
    Q = podzielone[1]

    plt.plot(moduluj(I,Q))
    plt.show()

if __name__ == '__main__':
    main()