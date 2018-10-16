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
        self._tab = [0]*dlugosc
        self.__odczepy = odczepy

    def shift(self, bit):
        '''
        metoda wprowadzajaca bit i przesuwajaca
        bit[0] = ten, ktory wszedl ostatnio. Wg teorii to nie stan - to bit wejsciowy
        '''
        for i in range(len(self._tab)-1, 0, -1):
            self._tab[i] = self._tab[i-1]
        self._tab[0] = bit

    def licz(self):
        '''wyliczenie wartosci ze stanu'''
        out = []
        for galazOdczepow in self.__odczepy:
            out.append(self._liczGalaz(galazOdczepow))
        return out

    def getDlugoscRejestru(self):
        return len(self._tab)-1

    def getIleBitowWyjsciowych(self):
        '''ile bitow na wyjsciu (ile galezi jest multipleksowanych)'''
        return len(self.__odczepy)

    def reset(self):
        for i in range(len(self._tab)):
            self._tab[i]=0

    def _liczGalaz(self, odczepy):
        val = 0
        for idxRejestru in odczepy:
            val ^= self._tab[idxRejestru]
        return val
    
    def __str__(self):
        '''
        skrajny lewy - bit wejsciowy
        skrajny prawy - bit do wypadniecia
        '''
        out=""
        for i in range(len(self._tab)):
            b = self._tab[i]
            out += str(b)
        return out

    def __repr__(self):
        return str(self)

    def injectState(self, state, inputBit):
        for i in range(len(state)):
            self._tab[i+1] = int(state[i])
        self._tab[0] = inputBit
    
    def getState(self):
        out = ""
        for i in range(1, len(self._tab)):
            out += str(self._tab[i])
        return out
    
    def getStateAfterShift(self):
        out = ""
        for i in range(len(self._tab)-1):
            out += str(self._tab[i])
        return out

    def getNumberOfStates(self):
        return (len(self._tab)-1)**2

class RejestrSystematyczny(RejestrPrzesuwny):
    def __init__(self, dlugosc, odczepy, odczepySprzezenia):
        '''dlugosc rejestru, 
           odczepy do wyjscia,
           odczepySprzezenia - odczepy ktorych wynik jest podawany na wejscie, lista pojedyncza. pomijamy jednosci'''
        super().__init__(dlugosc, odczepy)
        self.__odczepySprzezenia = odczepySprzezenia
        self.__bitWejsciowy = 0

    def getIleBitowWyjsciowych(self):
        return super().getIleBitowWyjsciowych() + 1

    def shift(self, bit):
        self.__bitWejsciowy = bit

        for i in range(len(self._tab)-1, 0, -1):
            self._tab[i] = self._tab[i-1]
        
        wyliczonyWejsciowy = self._liczGalaz(self.__odczepySprzezenia)
        self._tab[0] = wyliczonyWejsciowy ^ bit
    
    def reset(self):
        super().reset()
        self.__bitWejsciowy = 0

    def licz(self):
        wynik = super().licz()
        return [self.__bitWejsciowy] + wynik
    
    def getStateAfterShift(self):
        out = ""
        for i in range(len(self._tab)-1):
            out += str(self._tab[i])
        return out

    def injectState(self, state, inputBit):
        for i in range(len(state)):
            self._tab[i+1] = int(state[i])
        self.__bitWejsciowy = inputBit
        self._tab[0] = self.__bitWejsciowy ^ self._liczGalaz(self.__odczepySprzezenia)
