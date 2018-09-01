class Przeplatacz:
    def __init__(self, szerokoscPrzeplotu = 1):
        ''' przeplot realizowany na zasadzie transpozycji macierzy '''
        if szerokoscPrzeplotu == 0:
            raise Exception("krok przeplotu nie moze byc 0!")

        self.__szerokoscPrzeplotu = szerokoscPrzeplotu

    def przeplot(self, dane):
        indeksyPrzeplotu = self.__generujIndeksyPrzeplotu(dane)
        return list(map(lambda x: dane[x], indeksyPrzeplotu))

    def __generujIndeksyPrzeplotu(self, dane):
        dl = len(dane)
        krok = self.__szerokoscPrzeplotu
        for i in range(krok):
            j = i
            while(j < dl):
                yield j
                j += krok


    def rozplot(self, dane):
        out = [0 for i in range(len(dane))]
        indeksyPrzeplotu = self.__generujIndeksyPrzeplotu(dane)
        
        for i, v in enumerate(indeksyPrzeplotu):
            out[v] = dane[i]

        return out