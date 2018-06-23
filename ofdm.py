import scipy.fftpack as fft
import utils
import matplotlib.pyplot as plt
import numpy as np
import math
from przetwornikSP import PrzetwornikSzeregowoRownolegly
from modulatorQpsk import Qpsk

class Ofdm:
    def __init__(self, fp, fb, ileStrumieni):
        self.__fp = fp
        self.__fb=fb
        self.__ileStrumieni = ileStrumieni

    def __wyliczCzestotliwosci(self):
        out=[]
        for i in range(self.__ileStrumieni):
            out.append((i+1)*10)
        return out


    def moduluj(self, dane):
        if(len(dane) % 2 != 0):
            raise Exception('Dlugosc danych powinna byc parzysta, jest {}'.format(str(len(dane))))
    

        przetwornik = PrzetwornikSzeregowoRownolegly(self.__ileStrumieni)
        strumienie = przetwornik.rozdziel(dane)
        czestotliwosci = self.__wyliczCzestotliwosci()

        out = []

        for s,c in zip(strumienie, czestotliwosci):
            q = Qpsk(self.__fp, c, self.__fb//self.__ileStrumieni)
            wynik = q.moduluj(s)
            
            if(len(out) == 0):
                out = wynik
            else:
                for i in range(len(out)):
                    out[i] += wynik[i]
        return out        

def main():
    dane = utils.generujDaneBinarne(30)
    fp = 200
    fb =5
    ofdm  = Ofdm(fp,fb, 3)
    modulowany = ofdm.moduluj(dane)

    plt.subplot(2,1,1)
    plt.plot(modulowany)

    plt.subplot(2,1,2)
    plt.plot(abs(fft.fft(modulowany)))
    
    plt.show()

if __name__ == '__main__':
    main()