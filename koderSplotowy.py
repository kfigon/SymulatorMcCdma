from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow
from utils import podziel, flat
from viterbi import Viterbi

class KoderSplotowy:
    def __init__(self, rejestrPrzesuwny, ileBitowNaRaz = 1):
        self.__rejestr = rejestrPrzesuwny
        self.__ileBitowNaRaz = ileBitowNaRaz

    def kodujBezMultipleksowania(self, daneBinarne):
        assert(len(daneBinarne) % self.__ileBitowNaRaz == 0)

        self.reset()
        maszyna = MaszynaStanow(self.__rejestr, self.__ileBitowNaRaz)
        
        krok = self.__ileBitowNaRaz
        stan = maszyna.getStanPoczatkowy()

        for i in range(0, len(daneBinarne), krok):
            podCiag = daneBinarne[i:i+krok]
            daneStanu = maszyna.checkState(stan, podCiag)
            stan = daneStanu['outState']
            yield daneStanu['out']

    def koduj(self, daneBinarne):
        out = self.kodujBezMultipleksowania(daneBinarne)
        # multipleksowanie (p/s)
        return flat(out)

    def getNKM(self):
        return (self.__rejestr.getIleBitowWyjsciowych(),
                self.__ileBitowNaRaz, self.__rejestr.getDlugoscRejestru())

    def reset(self):
        self.__rejestr.reset()

    def dekoduj(self, daneBinarne):
        self.reset()
        maszyna = MaszynaStanow(self.__rejestr, self.__ileBitowNaRaz)
        v = Viterbi(maszyna)

        # todo: potencjalne miejsce do optymalizacji, 
        # nie tworzyc nowej tablicy, uzyc indeksow
        podzielone = podziel(daneBinarne, self.__rejestr.getIleBitowWyjsciowych())

        for i, paczka in enumerate(podzielone):
            if(i==0):
                v.liczPierwszy(paczka)
            else:
                v.licz(paczka)

        # v.pisz()
        return v.traceback()


