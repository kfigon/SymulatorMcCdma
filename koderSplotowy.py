from rejestrPrzesuwny import RejestrPrzesuwny
import math
class KoderSplotowy:
    def __init__(self, rejestrPrzesuwny, ileBitowNaRaz):
        self.__rejestr = rejestrPrzesuwny
        self.__ileBitowNaRaz = ileBitowNaRaz

    # todo - tryb krokowy
    def koduj(self, daneBinarne):
        dl = self.__rejestr.getIleBitowWyjsciowych()*len(daneBinarne)//self.__ileBitowNaRaz
        out = [0]*dl
        krok=self.__ileBitowNaRaz
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
