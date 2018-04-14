import utils
import math

class Qpsk:
    def __init__(self, fp, fc, ampl=1):
        '''
        :param fp: cz. probkowania
        :param fc: cz. nosnej
        :param ampl:
        '''
        self.__fp = fp
        self.__fc = fc
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
            yield self.__ampl * math.cos(2 * math.pi * self.__fc * t + faza)

    def __getQI(self, dane, czyI):
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