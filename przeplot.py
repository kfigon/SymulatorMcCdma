import math

class Przeplatacz:
    def __init__(self, iloscKolumn):
        ''' przeplot realizowany na zasadzie transpozycji macierzy '''
        self.__iloscKolumn = iloscKolumn

    def przeplot(self, dane):
        out = []
        dl = len(dane)
        for i in range(self.__iloscKolumn):
            j = i
            while(j < dl):
                out.append(dane[j])
                j += self.__iloscKolumn

        return out

    def rozplot(self, dane):
        return self.przeplot(dane)