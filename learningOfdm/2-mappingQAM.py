import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np

def modulujKanal(dane, nosna):
    out=[]
    for d in dane:
        for n in nosna:
            out.append(d*n)
    return out

def moduluj(data):
    t = np.arange(start=0, stop=1, step=0.01)
    cosinus = np.cos(2*np.pi*2*t)
    


def mapuj(data):
    out = []
    for i in range(len(data)-1):
        d = (data[i], data[i+1])
        if d == (0,0):  out.append(complex(1,1))
        elif d ==(0,1): out.append(complex(-1,1))
        elif d == (1,0):out.append(complex(-1,-1))
        else:   out.append(complex(1,-1))
        
    return out

dane = [0,1,0,1,0,1,0,1,1,0]

probkiCzestotliwosci = mapuj(dane)
sinusy = fft.ifft(probkiCzestotliwosci)

plt.subplot(2,1,1)
plt.plot(np.real(sinusy))

plt.subplot(2,1,2)
plt.plot(np.imag(sinusy))
plt.show()
