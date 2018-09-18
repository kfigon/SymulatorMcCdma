import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import random

# ofdm + qpsk
dopasowanieNyquista = 10 # parametr do wygladzenia przebiegu - dodania padingu x razy

def generujDaneBinarne(ile):
    out = []
    ile=ile//2
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
    dl = len(tab)*dopasowanieNyquista
    for _ in range(dl):
        tab.append(0)

dlugoscStrumienia = 10
# bawiac sie algorytmem mozna ustawic dl strumienia na 2 i duzo strumieni
# i bedzie zwykle QPSK
bity = [generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),]

out=[]
zmodulowane = []
rozproszony = []
for strumien in bity:
    zmodulowany = moduluj(strumien)
    zmodulowane.append(zmodulowany)
    bipolar = lambda x: 1 if x>=0.5 else -1
    for x in zmodulowany:
        out.append(x)
        rozproszony.append(x*bipolar(random.random()))

print(len(bity[0]))
print(len(out))

# plt.subplot(2,1,1)
# plt.plot(np.real(out))

# plt.subplot(2,1,2)
# plt.plot(np.abs(np.fft.fft(out[:len(out)//2])))
# plt.plot(np.abs(np.fft.fft(rozproszony[:len(rozproszony)//2])))
# plt.show()


# odbiornik
