from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow
from utils import podziel, flat
from viterbi import Viterbi

class KoderSplotowy:
    def __init__(self, rejestrPrzesuwny, ileBitowNaRaz = 1):
        self.__ileBitowNaRaz = ileBitowNaRaz
        self.__maszyna = MaszynaStanow(rejestrPrzesuwny, self.__ileBitowNaRaz)

        self.__nkm = (
                rejestrPrzesuwny.getIleBitowWyjsciowych(),
                self.__ileBitowNaRaz, 
                rejestrPrzesuwny.getDlugoscRejestru())

    def kodujBezMultipleksowania(self, daneBinarne):
        assert(len(daneBinarne) % self.__ileBitowNaRaz == 0)
        
        krok = self.__ileBitowNaRaz
        stan = self.__maszyna.getStanPoczatkowy()

        for i in range(0, len(daneBinarne), krok):
            podCiag = daneBinarne[i:i+krok]
            daneStanu = self.__maszyna.checkState(stan, podCiag)
            stan = daneStanu['outState']
            yield daneStanu['out']

    def koduj(self, daneBinarne):
        out = self.kodujBezMultipleksowania(daneBinarne)
        # multipleksowanie (p/s)
        return flat(out)

    def getNKM(self):
        return self.__nkm

    def dekoduj(self, daneBinarne):
        v = Viterbi(self.__maszyna)

        # todo: potencjalne miejsce do optymalizacji, 
        # nie tworzyc nowej tablicy, uzyc indeksow
        podzielone = podziel(daneBinarne, self.getNKM()[0])

        for i, paczka in enumerate(podzielone):
            if(i==0):
                v.liczPierwszy(paczka)
            else:
                v.licz(paczka)

        # v.pisz()
        return v.traceback()


