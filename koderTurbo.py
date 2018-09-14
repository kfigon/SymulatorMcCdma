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
        out1 = list(self.__koduj(self.__rej1, dane))
        przeplecione = self.__przeplatacz.przeplot(dane)
        out2 = list(self.__koduj(self.__rej2, przeplecione))

        return [dane, out1, out2]
    
    @staticmethod
    def combine(tab1, tab2, tab3):
        dl1 = len(tab1)
        dl2 = len(tab2)
        dl3 = len(tab3)
        if dl1 != dl2 or dl2 != dl3 or dl1 != dl3:
            raise Exception("kombinator musi dostac rowne tablice: {},{},{}".format(str(dl1),str(dl2),str(dl3)))

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
            out.append([tab[i], tab[i+skok]])

        return out

    def dekoduj(self, dane, ileItracji = 5):
        maszyna1 = MaszynaStanow(self.__rej1)
        map1 = MapAlgorithm(maszyna1)
        podzielone1 = KoderTurbo.decombine(dane, 1)
        
        prawdopodobienstwa1 = map1.dekoduj(podzielone1)

