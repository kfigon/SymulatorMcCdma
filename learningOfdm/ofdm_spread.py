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
    dl-=len(tab) # 5 bitow, padding 50, wychodzi 55. A ja chce 50 na wyjsciu
    for _ in range(dl):
        tab.append(0)

dlugoscStrumienia = 90
# bawiac sie algorytmem mozna ustawic dl strumienia na 2 i duzo strumieni
# i bedzie zwykle QPSK
bity = [generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),
        generujDaneBinarne(dlugoscStrumienia),]

out=[]
rozproszony = []
for strumien in bity:
    zmodulowany = moduluj(strumien)
    bipolar = lambda x: 1 if x>=0.5 else -1
    for x in zmodulowany:
        out.append(x)
        rozproszony.append(x*bipolar(random.random()))

plt.subplot(2,1,1)
plt.plot(np.real(out))

plt.subplot(2,1,2)
plt.plot(np.abs(fft.fft(out[:len(out)//2])))
plt.plot(np.abs(fft.fft(rozproszony[:len(rozproszony)//2]))) # zle! to rozprasza calosc, a ma byc chip na symbol (nosna)
plt.show()


# odbiornik
podzielone = []
ileProbekNaStrumien = len(out)//len(bity)
ileStrumieni = len(out)//ileProbekNaStrumien
for i in range(ileStrumieni):
    podzielone.append(out[i*ileProbekNaStrumien:(i+1)*ileProbekNaStrumien])

def demod(val):
    if (val < 0.000001 and val >= 0) or (val > -0.00001 and val <= 0):
        return 0
    if val > 0:
        return 1
    else:
        return -1

zdemodulowane=[]
for strumien in podzielone:
    probkiCzestotliwosci = fft.fft(strumien)
    zdemodulowaneBity=[]
    for p in probkiCzestotliwosci:
        bi=demod(p.real)
        bq = demod(p.imag)
        toAdd = 0
        if bi != 0 and bq != 0:
            toAdd = complex(bi, bq)
        zdemodulowaneBity.append(toAdd)
    zdemodulowane.append(zdemodulowaneBity)

for i in range(len(bity)):
    assert zdemodulowane[i] == bity[i]
print("YEAH!")