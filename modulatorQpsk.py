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

    def __symbol2Faza(self, i, q):
        if(i == 0 and q == 0):
            return math.pi/4
        elif(i == 0 and q == 1):
            return 3*math.pi / 4
        elif (i == 1 and q == 0):
            return 5*math.pi / 4
        elif (i == 1 and q == 1):
            return 7*math.pi / 4
        raise Exception('Blad I{}, Q{}'.format(str(i), str(q)))

# import matplotlib.pyplot as plt
def main():
    dane = utils.generujDaneBinarneGen(20)
    fp = 10
    fn=1
    probki = utils.probkuj(dane, fp,fn)
    q = Qpsk(fp, fn)
    # plt.stem(dane)
    # plt.show()

main()
