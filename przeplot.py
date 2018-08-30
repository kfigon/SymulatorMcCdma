import math

class Przeplatacz:
    def __init__(self, szerokoscPrzeplotu):
        ''' przeplot realizowany na zasadzie transpozycji macierzy '''
        self.szerokoscPrzeplotu = szerokoscPrzeplotu

    def przeplot(self, dane):
        if len(dane) % self.szerokoscPrzeplotu != 0:
            raise Exception('Ilosc danych {} powinna byc podzielna przez krok przeplotu {}'
            .format(str(len(dane),str(self.szerokoscPrzeplotu))))

        return self._przeplotInternal(dane, self.szerokoscPrzeplotu)

    def _przeplotInternal(self, dane, krok):
        out = []
        dl = len(dane)
        for i in range(krok):
            j = i
            while(j < dl):
                out.append(dane[j])
                j += krok

        return out

    def rozplot(self, dane):
        krok = math.ceil(len(dane)/self.szerokoscPrzeplotu)
        return self._przeplotInternal(dane, krok)