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

def podzielDaneNaKanaly(dane, ileKanalow=2):
    '''
    podzial danych jak przy qpsk - co drugi bit
    '''
    if len(dane) % ileKanalow != 0:
        raise Exception('nierowny sturmien danych, len: {}, ileKanalow: {}'.format(str(len(dane)), str(ileKanalow)))
    
    out=[]
    for i in range(ileKanalow):
        skipped = [dane[i] for i in range(i, len(dane), ileKanalow)]
        out.append(skipped)
    return out

def str2List(data):
    out = [0]*len(data)
    for i in range(len(data)):
        out[i]=int(data[i])
    return out

def generujDaneBinarne(ile):
    return list(generujDaneBinarneGen(ile))

def generujDaneBinarneGen(ile):
    '''
    generator
    '''
    for _ in range(ile):
        yield randint(0,1)

def probkuj(dane, fp, fs):
    '''
    :param dane: dane binarne
    :param fp: cz. probkowania
    :param fs: cz. sygnalu
    :return:  sprobkowane dane
    '''
    return list(probkujGen(dane, fp, fs))

def probkujGen(dane, fp, fs):
    ileProbekNaBit = int(fp/fs)
    for b in dane:
        for _ in range(ileProbekNaBit):
            yield b

def getCzasTransmisji(ileBitow, fb):
    return math.ceil(ileBitow/fb)

def bipolar(binarne):
    return 1 if binarne == 0 else -1

def flat(tab):
    return [item for sublist in tab for item in sublist]

def generujSzum(ile, a=0,b=1):
    return np.random.normal(a,b,ile)

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