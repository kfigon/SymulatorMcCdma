# odczepy - tablica indeksow:
# bity przesuwaja sie w kierunku rosnacych indeksow.
# Nowy bit wchodzi na[0]
# 0 1 2 - indeksy komorek rejestru
# | | | - odczepy -> [0,1,2]
# |   | - odczepy -> [0,2]
# dlugosc tutaj - 3 (2 na komorki i 1 na aktualny bit)
class RejestrPrzesuwny:
    def __init__(self, dlugosc, odczepy):
        self.__tab = [0]*dlugosc
        self.__odczepy = odczepy

    # bit 0 - te, ktory ostatnio wszedl.
    # wg teorii to nie stan, to wejsciowy bit
    def shift(self, bit):
        for i in range(len(self.__tab)-1, 0, -1):
            self.__tab[i] = self.__tab[i-1]
        self.__tab[0] = bit

    def licz(self):
        out = []
        for galazOdczepow in self.__odczepy:
            out.append(self.__liczGalaz(galazOdczepow))
        return tuple(out)

    def getDlugoscRejestru(self):
        return len(self.__tab)-1

    def getIleBitowWyjsciowych(self):
        return len(self.__odczepy)

    def reset(self):
        for i in range(len(self.__tab)):
            self.__tab[i]=0

    def __liczGalaz(self, odczepy):
        val = 0
        for idxRejestru in odczepy:
            val ^= self.__tab[idxRejestru]
        return val
    
    def __str__(self):
        out=""
        for i in range(len(self.__tab)):
            b = self.__tab[i]
            out += str(b)
        return out

    def __repr__(self):
        return str(self)
