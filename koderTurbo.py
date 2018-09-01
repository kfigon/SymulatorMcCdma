from koderSplotowy import KoderSplotowy
from przeplot import Przeplatacz
from rejestrPrzesuwny import RejestrPrzesuwny

class KoderTurbo:
    def __init__(self, koder1, koder2, przeplatacz = Przeplatacz()):
        self.__koder1 = koder1
        self.__koder2 = koder2
        self.__przeplatacz = przeplatacz

    def koduj(self, dane):
        zakodowane = self.__koder1.koduj(dane)
        przeplecione = self.__przeplatacz.przeplot(zakodowane)
        return self.__koder2.koduj(przeplecione)


# k1 = KoderSplotowy(RejestrPrzesuwny(3, [0,1,2]))
# k2 = KoderSplotowy(RejestrPrzesuwny(3,[0,1]))
# p = Przeplatacz()
# k = KoderTurbo(koder1 = k1, koder2 = k2, przeplatacz = p)


# out = k.koduj()
# print(out)