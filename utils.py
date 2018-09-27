from random import randint, randrange
import math
import numpy as np
import random

# tablice
def odlegloscHamminga(daneA, daneB):
    assert (len(daneA) == len(daneB))
    roznica = 0
    for i in range(len(daneA)):
        if (daneA[i] != daneB[i]):
            roznica += 1
    return roznica

def podziel(dane, ileNaRaz):
    ''' podzialListy z X bitami '''

    assert (len(dane) % ileNaRaz == 0)
    out=[None]* (len(dane)//ileNaRaz)
    for i in range(len(out)):
        out[i] = dane[i*ileNaRaz: ((i+1)*ileNaRaz)]
    
    return out

def str2List(data):
    out = [0]*len(data)
    for i in range(len(data)):
        out[i]=int(data[i])
    return out

def generujDaneBinarne(ile):
    out = [0 for _ in range(ile)]
    for i in range(ile):
        out[i] = randint(0,1)
    return out

def bipolar(binarne):
    return 1 if binarne == 0 else -1

def flat(tab):
    return [item for sublist in tab for item in sublist]

def generujSymboleBipolarneZespolone(ile):
    out = []
    ile=ile//2
    bipolar = lambda x: 1 if x>=0.5 else -1
    for _ in range(ile):
        bitI = bipolar(random.random())
        bitQ = bipolar(random.random())
        out.append(complex(bitI, bitQ)) 
    return out

def generujQpskZBitow(bity):
    if len(bity) % 2 == 1:
        raise Exception("dlugosc bitow musi byc parzysta, jest {}".format(str(len(bity))))
    
    out = []
    for i in range(0, len(bity),2):
        bitI = bipolar(bity[i])
        bitQ = bipolar(bity[i+1])
        out.append(complex(bitI, bitQ)) 
    return out

def demodulujQpsk(symbole):
    '''zwraca bity'''
    out = []
    binar = lambda x : 1 if x == -1 else 0

    for s in symbole:
        out.append(binar(s.real))
        out.append(binar(s.imag))

    return out

def liczEbN0(sygnal, snrDb):
    rate = 1
    dlSygnalu = len(sygnal)

    sredniaEnergia = np.sum(np.abs(sygnal) * np.abs(sygnal))/dlSygnalu
    srnLin = 10**(snrDb/10.0)
    wariancjaSzumu =sredniaEnergia/(2*rate*srnLin)
    
    return sredniaEnergia, wariancjaSzumu 

def awgn(sygnal, snrDb):

    dlSygnalu = len(sygnal)
    sredniaEnergia, wariancjaSzumu = liczEbN0(sygnal, snrDb)
    szum = None

    if isinstance(sygnal[0], complex):
        szum = (np.sqrt(wariancjaSzumu) * np.random.randn(dlSygnalu))
        +(np.sqrt(wariancjaSzumu) * np.random.randn(dlSygnalu))*1j
    else:
        szum = np.sqrt(2*wariancjaSzumu) * np.random.randn(dlSygnalu)

    return sygnal + szum

def zerujKoniec(tab, ile):
    '''zeruje ostatnie <ile> elementow tablicy'''
    tab[-ile:] = [0 for _ in range(ile)]