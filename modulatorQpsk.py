import math
import utils

class Qpsk:
    def __init__(self, fp, fn, fb, ampl=1):
        '''
        :param fp: cz. probkowania
        :param fn: cz. nosnej
        :param fb: cz. bitow (2 razy wieksza niz symboli)
        :param ampl:
        '''
        self.__fp = fp
        self.__fn = fn
        self.__fb = fb
        self.__ampl = ampl

    def generujCzas(self, czasTrwania):
        for i in range(czasTrwania * self.__fp):
            yield (i / self.__fp)

    def __getQI(self, dane, czyI):
        if(len(dane) % 2 != 0):
            raise Exception('Dlugosc danych powinna byc parzysta, jest {}'.format(str(len(dane))))

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
        if(len(dane) % 2 != 0):
            raise Exception('Dlugosc danych powinna byc parzysta, jest {}'.format(str(len(dane))))
        
        czasTrwania = utils.getCzasTransmisji(len(dane), self.__fb) 
        czas = self.generujCzas(czasTrwania)

        qbity = self.getQ(dane)
        ibity = self.getI(dane)

        probkiQ = utils.probkujGen(qbity, self.__fp, self.__fb/2)
        probkiI = utils.probkujGen(ibity, self.__fp, self.__fb/2)
        
        out = []
        for t, q, i in zip(czas, probkiQ, probkiI):
            faza = self.__symbol2Faza(i,q)
            x = self.__ampl*math.cos(faza)*math.cos(2*math.pi*self.__fn*t)
            y = self.__ampl*math.sin(faza)*math.sin(2*math.pi*self.__fn*t)
            out.append(x-y)
        return out

    def walidujDlugosci(self, dane):
        qbity = self.getQ(dane)
        ibity = self.getI(dane)
        probkiQ = list(utils.probkujGen(qbity, self.__fp, self.__fb/2))
        probkiI = list(utils.probkujGen(ibity, self.__fp, self.__fb/2))
        czasTrwania = utils.getCzasTransmisji(len(dane), self.__fb) 
        czas = list(self.generujCzas(czasTrwania))        

        dlCzas = len(czas)
        dI = len(probkiI)
        dQ = len(probkiQ)
        if(dlCzas != dI and dlCzas != dQ and dI != dQ):
            raise Exception('dlugosc czasu: {}, dlugosc I {}, dlugosc Q {}'.format(
                        str(dlCzas), 
                        str(dI),
                        str(dQ)))

    def __symbol2Faza(self, i, q):
        if(i == 0 and q == 0):
            return math.pi/4
        elif(i == 0 and q == 1):
            return 3*math.pi / 4
        elif (i == 1 and q == 0):
            return 5*math.pi / 4
        elif (i == 1 and q == 1):
            return 7*math.pi / 4
        raise Exception('Blad, nie ma fazy dla: I{}, Q{}'.format(str(i), str(q)))



# todo: odkomentowac dla testu

# import matplotlib.pyplot as plt
# def wykresQpsk():
#     dane = utils.generujDaneBinarne(20)
#     fp = 50
#     fn=2
#     fb = 1
#     qpsk = Qpsk(fp, fn,fb)
#     modulowany = qpsk.moduluj(dane)

#     plt.subplot(2,1,1)
#     plt.stem(dane)
#     plt.subplot(2, 1, 2)
#     plt.plot(modulowany)
#     plt.show()

# wykresQps()
