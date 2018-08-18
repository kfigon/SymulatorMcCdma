import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import numpy as np
import random as rand

def moduluj(dane, nosna):
    out=[]
    for d in dane:
        for n in nosna:
            out.append(d*n)
    return out

def modulujSpread(dane, nosna):
    out=[]
    for d,n in zip(dane,nosna):
        out.append(d*n)
    return out    

def generujPN(t):
    for _ in t:
        prog = lambda x: 1 if x>=0.5 else -1
        val = prog(rand.random())
        yield val

t = np.arange(start=0, stop=1, step=0.01)
cosinus = np.cos(2*np.pi*2*t)
sinus = np.sin(2*np.pi*2*t)

data = [-1,1,1,-1,1,-1]
I = [-1,1,1]
Q=[1,-1,-1]

modI=moduluj(I, cosinus)
modQ=moduluj(Q, sinus)
# plt.plot(modI+modQ)
# plt.show()

# generuje PN tak gesty jak cz probkowania
# kazda probka jest rozproszona
# w przypadku mnozenia nie ma
# znaczenia kolejnosc, cyz mnozymy probki nosnej czy sygnalu
# mnozenie jest przemienne
modIs = modulujSpread(generujPN(t), cosinus)
# plt.plot(modIs)
# plt.show()
fIs = fourier.fft(modIs)
fI = fourier.fft(modI)

plt.plot(np.abs(fI[:len(fI)//2]), label='zmodulowany')
plt.plot(np.abs(fIs[:len(fIs)//2]), label='rozproszony')
plt.legend()
plt.show()