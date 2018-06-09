import scipy.fftpack as fft
from modulatorQpsk import Qpsk
import utils
import matplotlib.pyplot as plt
import numpy as np
import math

class Ofdm(Qpsk):
    def __init__(self, fp, fn, fb, ampl=1):
        super().__init__(fp, fn, fb, ampl)
        self.__fp = fp
        self.__fn = fn
        self.__fb=fb
        self.__ampl = ampl

    def __bity2Symbole(self, bity):
        for i in range(len(bity)-1):
            yield self.__mapujNaSymbol(bity[i], bity[i+1])

    def __mapujNaSymbol(self, ib, qb):
        if ib == 0 and qb == 0:
            return complex(1,1)
        elif ib==0 and qb == 1:
            return complex(-1,1)
        elif ib==1 and qb==0:
            return complex(-1,-1)
        else:
            return complex(1, -1)

    def moduluj(self, dane):
        if(len(dane) % 2 != 0):
            raise Exception('Dlugosc danych powinna byc parzysta, jest {}'.format(str(len(dane))))
        
        symbole = self.__bity2Symbole(dane)
        probkiSymboli = list(utils.probkujGen(symbole, self.__fp, self.__fb/2))
        
        transformata = fft.ifft(probkiSymboli)

        czasTrwania = utils.getCzasTransmisji(len(dane), self.__fb) 
        czas = self.generujCzas(czasTrwania)

        out = []
        for t, f in zip(czas, transformata):
            
            x = self.__ampl*f.real*math.cos(2*math.pi*self.__fn*t)
            y = self.__ampl*f.imag*math.sin(2*math.pi*self.__fn*t)
            out.append(x+y)
        return out        

def main():
    dane = utils.generujDaneBinarne(30)
    fp = 200
    fn= 3
    fb =5
    ofdm  = Ofdm(fp, fn,fb)
    modulowany = ofdm.moduluj(dane)
    N = len(modulowany)

    plt.subplot(2,1,1)
    plt.plot(modulowany)

    plt.subplot(2,1,2)
    plt.plot(abs(fft.fft(modulowany[0:int(N/2)])))
    plt.show()

if __name__ == '__main__':
    main()