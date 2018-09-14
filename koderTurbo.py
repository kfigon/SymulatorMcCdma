from przeplot import Przeplatacz
from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow
from utils import flat
from map import MapAlgorithm

class KoderTurbo:
    def __init__(self, rejestr1, rejestr2, przeplatacz = Przeplatacz()):
        if rejestr1.getIleBitowWyjsciowych() != 2 or rejestr2.getIleBitowWyjsciowych() != 2:
            raise Exception('rejestry kodera turbo musza miec 2 gazie do odczepow!')

        self.__rej1 = rejestr1
        self.__rej2 = rejestr2
        self.__przeplatacz = przeplatacz

    def __koduj(self, rejestr, dane):
        rejestr.reset()
        for b in dane:
            wynik = rejestr.licz()
            wejscie = b ^ wynik[0]
            rejestr.shift(wejscie)

            yield wynik[1]

    def koduj(self, dane):
        # todo: uncomment termination, fix test
        out1 = list(self.__koduj(self.__rej1, dane)) + self.__rej1.terminate()
        # terminacja tylko pierwszego? literatura tak sugeruje
        przeplecione = self.__przeplatacz.przeplot(dane)
        out2 = list(self.__koduj(self.__rej2, przeplecione)) + self.__rej2.terminate()

        return [dane, out1, out2]
    
    @staticmethod
    def combine(tab1, tab2, tab3):
        if len(tab1) != len(tab2) or len(tab2) != len(tab3) or len(tab1) != len(tab3):
            raise Exception("kombinator musi dostac rowne tablice")

        out = []
        for a,b,c in zip(tab1, tab2,tab3):
            out.append(a)
            out.append(b)
            out.append(c)
        return out
    
    @staticmethod
    def decombine(tab, skok):
        out = []
        for i in range(0, len(tab),3):
            out.append(tab[i])
            out.append(tab[i+skok])

        return out

    def dekoduj(self, dane, ileItracji = 5):
        maszyna1 = MaszynaStanow(self.__rej1)
        map1 = MapAlgorithm(maszyna1)
        podzielone1 = KoderTurbo.decombine(dane, 1)
        
        prawdopodobienstwa1 = map1.dekoduj(podzielone1)

