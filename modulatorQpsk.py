import math
import utils

class Qpsk:
    def __init__(self, fp, fn, ampl=1):
        '''
        :param fp: cz. probkowania
        :param fn: cz. nosnej
        :param ampl:
        '''
        self.__fp = fp
        self.__fn = fn
        self.__ampl = ampl

    def generujCzas(self, czasTrwania):
        for i in range(0, czasTrwania * self.__fp):
            yield (i / self.__fp)

    def generujNosna(self, czas, faza=0):
        '''
        :param czas: wynik z generatora czasu
        :param faza: faza cosinusa w radianach
        :return:
        '''
        for t in czas:
            yield self.__ampl * math.cos(2 * math.pi * self.__fn * t + faza)

    def __getQI(self, dane, czyI):
        if(len(dane) % 2 != 0):
            raise Exception('Dlugosc powinna byc parzysta')

        modulo = 1
        if(czyI):
            modulo = 0
        for i in range(len(dane)):
            if(i%2==modulo):
                yield dane[i]

    def getQ(self, dane):
        return self.__getQI(dane, False)

    def getI(self, dane):
        return self.__getQI(dane, True)

    def moduluj(self, dane):
        pass

    def getCzasTransmisji(self, ileBitow, fb):
        return int(ileBitow/fb)

    def mapBipolar(self, bit):
        if(bit == 0):
            return 1
        return -1

    def symbol2Faza(self, i, q):
        if(i == 0 and q == 0):
            return math.pi/4
        elif(i == 0 and q == 1):
            return 3*math.pi / 4
        elif (i == 1 and q == 0):
            return 5*math.pi / 4
        elif (i == 1 and q == 1):
            return 7*math.pi / 4
        raise Exception('Blad I{}, Q{}'.format(str(i), str(q)))

import matplotlib.pyplot as plt
def main():
    dane = utils.generujDaneBinarneGen(10)
    fp = 10
    fn=2
    fb = 1
    probki = utils.probkuj(dane, fp,fn)
    qpsk = Qpsk(fp, fn)

    q = qpsk.getQ(dane)
    i = qpsk.getI(dane)

    modulowany = []
    czas
    while(True):
        try:
            qi = next(q)
            ii = next(i)
            faza = qpsk.symbol2Faza(ii, qi)
            nosnaSymbolu = qpsk.generujNosna()
        except:
            break

    #  todo: przejscie na kanaly IQ
    # 'spowalnia' bitrate o 2.
    #  dane 10Hz, I 5, Q 5
    plt.subplot(2,1,1)
    plt.stem(dane)
    plt.subplot(2, 1, 2)
    plt.stem(modulowany)
    plt.show()

main()
