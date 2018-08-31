from koderSplotowy import KoderSplotowy
from przeplot import Przeplatacz

class KoderTurbo:
    def __init__(self, koder1, koder2, przeplatacz):
        self.__koder1 = koder1
        self.__koder2 = koder2
        self.__przeplatacz = przeplatacz

    def koduj(self, dane):
        zakodowane = self.__koder1.koduj(dane)
        przeplecione = self.__przeplatacz.przeplot(zakodowane)
        return self.__koder2.koduj(przeplecione)
