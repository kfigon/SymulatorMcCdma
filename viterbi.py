from maszynaStanow import MaszynaStanow
from utils import odlegloscHamminga

class Viterbi:
    def __init__(self, maszynaStanow):
        self.__maszyna = maszynaStanow
        self.__trellis = []

    # dane - podzielona paczka bitow
    def licz(self, dane):
        stany = self.__maszyna.getListaStanow()
        for st in stany:
            przejscia = self.__maszyna.getMozliwePrzejscia(st)

        pass

    def liczPierwszy(self, dane):
        stanPoczatkowy = self.__maszyna.getStanPoczatkowy()
        przejscia = self.__maszyna.getMozliwePrzejscia(stanPoczatkowy)
        krok = {'stany': []}
        for i in przejscia:
            hamming = odlegloscHamminga(dane, przejscia[MaszynaStanow.OUT])
            stan = {'stan': i, 'hamming': hamming}
            krok['stany'].append(stan)
        
        self.__trellis.append(krok)

    def traceback(self):
        out = []
        return out
