from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow
from utils import podziel
from viterbi import Viterbi

class KoderSplotowy:
    def __init__(self, rejestrPrzesuwny, ileBitowNaRaz):
        self.__rejestr = rejestrPrzesuwny
        self.__ileBitowNaRaz = ileBitowNaRaz

    def koduj(self, daneBinarne):
        assert(len(daneBinarne) % self.__ileBitowNaRaz == 0)

        dl = self.__rejestr.getIleBitowWyjsciowych()*len(daneBinarne)//self.__ileBitowNaRaz
        out = [0]*dl
        krok = self.__ileBitowNaRaz
        idxOut=0
        for i in range(0, len(daneBinarne), krok):
            podCiag = daneBinarne[i:i+krok]
            # wchodza wszystkie na raz!
            for obrot in reversed(range(krok)):
                b = podCiag[obrot]
                self.__rejestr.shift(b)
            wynikObrotu = self.__rejestr.licz()

            for b in wynikObrotu:
                out[idxOut] = b
                idxOut += 1
        return out

    def getNKM(self):
        return (self.__rejestr.getIleBitowWyjsciowych(),
                self.__ileBitowNaRaz, self.__rejestr.getDlugoscRejestru())

    def reset(self):
        self.__rejestr.reset()

    def dekoduj(self, daneBinarne):
        maszyna = MaszynaStanow(self.__rejestr, self.__ileBitowNaRaz)
        v = Viterbi(maszyna)
        podzielone = podziel(daneBinarne, self.__rejestr.getIleBitowWyjsciowych())

        for i, paczka in enumerate(podzielone):
            if(i==0):
                v.liczPierwszy(paczka)
            else:
                v.liczSciezke(paczka)

        for i in v.getSciezki():
            print(i)

        # todo: pominiecie sciezek, ktore nawet nie dotarly do konca
        # (dlugosc sciezki)
        return self.__traceBackNajlepszejSciezki(v.getSciezki())

    def __traceBackNajlepszejSciezki(self, sciezki):
        najlepszaSciezka = sciezki[0]
        for s in sciezki:
            if(s.getZakumulowanyHamming() < najlepszaSciezka.getZakumulowanyHamming()):
                najlepszaSciezka = s

        return najlepszaSciezka.traceBack()


