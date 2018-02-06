# odczepy - tablica indeksow:
# bity przesuwaja sie w kierunku rosnacych indeksow.
# Nowy bit wchodzi na[0]
# 0 1 2 - indeksy komorek rejestru
# | | | - odczepy -> [0,1,2]
# |   | - odczepy -> [0,2]
class RejestrPrzesuwny:
    def __init__(self, dlugosc, odczepy):
        self.__tab = [0]*dlugosc
        self.__odczepy = odczepy

    # przesuwa, potem liczy
    def shift(self, bit):
        for i in range(len(self.__tab)-1, 0, -1):
            self.__tab[i] = self.__tab[i-1]
        self.__tab[0] = bit
  
        return self.__licz()

    def __liczGalaz(self, odczepy):
        val = 0
        for idxRejestru in odczepy:
            val ^= self.__tab[idxRejestru]
        return val
    
    def __licz(self):
        out = []
        for galazOdczepow in self.__odczepy:         
            out.append(self.__liczGalaz(galazOdczepow))
        return tuple(out)
    
    def __str__(self):
        out=""
        # stan zawsze dlugoscRejestru - 1
        for i in range(len(self.__tab)-1):
            b = self.__tab[i]
            out += str(b)
        return out

    def __repr__(self):
        return str(self)
