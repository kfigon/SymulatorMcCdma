import math

# algorytm z ksiazki o cdma2000
class GeneratorKoduWalsha:
    def __init__(self, dlugoscCiagu):
        self.__ileZmiennych = math.log2(dlugoscCiagu)

    def generuj(self, nrUzytkownika):
        szablon = '0%db' % self.__ileZmiennych
        liczba = format(nrUzytkownika, szablon)
        out = [0]
        for b in reversed(liczba):
            self.__dopisz(out, b == '1')
        return out

    def __dopisz(self, tab, czyOdwrocic):
        dl = len(tab)
        for i in range(dl):
            b = int(tab[i])
            if czyOdwrocic:
                b ^= 1
            tab.append(b)