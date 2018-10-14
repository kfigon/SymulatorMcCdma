from utils import flat

class RejestrPrzesuwny:
    def __init__(self, dlugosc, odczepy):
        '''
        odczepy - tablica indeksow:
        bity przesuwaja sie w kierunku rosnacych indeksow.
        Nowy bit wchodzi na[0]
        0 1 2 - indeksy komorek rejestru. Potegi wielomianu
        | | | - odczepy -> [0,1,2]
        |   | - odczepy -> [0,2]
        dlugosc tutaj - 3 (2 na komorki i 1 na aktualny bit)
        '''
        self.__tab = [0]*dlugosc
        self.__odczepy = odczepy

    def shift(self, bit):
        '''
        metoda wprowadzajaca bit i przesuwajaca
        bit[0] = ten, ktory wszedl ostatnio. Wg teorii to nie stan - to bit wejsciowy
        '''
        for i in range(len(self.__tab)-1, 0, -1):
            self.__tab[i] = self.__tab[i-1]
        self.__tab[0] = bit

    def licz(self):
        '''wyliczenie wartosci ze stanu'''
        out = []
        for galazOdczepow in self.__odczepy:
            out.append(self.__liczGalaz(galazOdczepow))
        return out

    def terminate(self):
        ''' wypluwa z siebie stan na zewnatrz'''
        out = []
        for _ in range(self.getDlugoscRejestru()-1):
            self.shift(0)
            out.append(self.licz())
        return flat(out)

    def getDlugoscRejestru(self):
        return len(self.__tab)

    def getIleBitowWyjsciowych(self):
        '''ile bitow na wyjsciu (ile galezi jest multipleksowanych)'''
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
        '''
        skrajny lewy - bit wejsciowy
        skrajny prawy - bit do wypadniecia
        '''
        out=""
        for i in range(len(self.__tab)):
            b = self.__tab[i]
            out += str(b)
        return out

    def __repr__(self):
        return str(self)

class RejestrSystematyczny(RejestrPrzesuwny):
    def __init__(self, dlugosc, odczepy, odczepySprzezenia):
        '''dlugosc rejestru, 
           odczepy do wyjscia,
           odczepySprzezenia - odczepy ktorych wynik jest podawany na wejscie, lista pojedyncza'''
        super().__init__(dlugosc, odczepy)
        self.__odczepySprzezenia = odczepySprzezenia

    def getIleBitowWyjsciowych(self):
        return super().getDlugoscRejestru() + 1
