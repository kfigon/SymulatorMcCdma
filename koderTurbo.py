from przeplot import Przeplatacz
from rejestrPrzesuwny import RejestrPrzesuwny, RejestrSystematyczny
from maszynaStanow import MaszynaStanow
from utils import flat, binar
from map import MapAlgorithm, mapujBit
import math

def budujDomyslnyKoder():
    r1 = RejestrSystematyczny(3, [[0,2]], [1,2])
    r2 = RejestrSystematyczny(3, [[0,2]], [1,2])
    return KoderTurbo(rejestr1 = r1, 
                            rejestr2 = r2,
                            przeplatacz=Przeplatacz(10))

class Koder:
    def kodujE2E(self, dane):
        return dane

    def dekoduj(self, dane, ileItracji = 5, lc=5):
        return list(map(binar, dane))
    

class KoderTurbo(Koder):
    def __init__(self, rejestr1, rejestr2, przeplatacz = Przeplatacz()):
        if rejestr1.getIleBitowWyjsciowych() != 2 or rejestr2.getIleBitowWyjsciowych() != 2:
            raise Exception('rejestry kodera turbo musza miec 2 gazie do odczepow!')

        self.__rej1 = rejestr1
        self.__rej2 = rejestr2
        self.__przeplatacz = przeplatacz

    def __koduj(self, rejestr, dane):
        rejestr.reset()
        for b in dane:
            rejestr.shift(b)
            wynik = rejestr.licz()
            yield wynik[1]

    def koduj(self, dane):
        out1 = list(self.__koduj(self.__rej1, dane))
        przeplecione = self.__przeplatacz.przeplot(dane)
        out2 = list(self.__koduj(self.__rej2, przeplecione))

        return [dane, out1, out2]

    def kodujE2E(self, dane):
        [a,b,c] = self.koduj(dane)
        return self.combine(a,b,c)

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
    def decombine(tab):
        a=[]
        b=[]
        c=[]

        for i in range(0,len(tab)-2, 3):
            a.append(tab[i])
            b.append(tab[i+1])
            c.append(tab[i+2])

        return [a,b,c]

    def __rozdziel(self, sys, par):
        podzielone = []
        for s,p in zip(sys, par):
            podzielone.append([s,p])
        return podzielone

    def dekoduj(self, dane, ileItracji = 5, lc=5):
        '''wchodza bity, wychodza bity. Maping bipolarny juz sie zadzieje sam'''
        map1 = MapAlgorithm(MaszynaStanow(self.__rej1), lc)
        map2 = MapAlgorithm(MaszynaStanow(self.__rej2), lc) 
        
        dane = list(map(lambda x: x*(-1), dane))

        [systematyczne, par1, par2] = self.decombine(dane)
        przeplecioneSystematyczne = self.__przeplatacz.przeplot(systematyczne)
        
        podzielone1 = self.__rozdziel(systematyczne, par1)
        podzielone2 = self.__rozdziel(przeplecioneSystematyczne, par2)
        
        wynikDekodera2 = None
        intr = None
        for _ in range(ileItracji):
            extr1 = map1.dekoduj(podzielone1)
            przeplecioneExtr1 = self.__przeplatacz.przeplot(extr1)
            intr = przeplecioneExtr1

            extr2 = map2.dekoduj(podzielone2)
            wynikDekodera2 = extr2

        out=[]
        for sys,l,d in zip(przeplecioneSystematyczne, intr, wynikDekodera2):
            w = d+ lc*sys + l
            out.append(w)
        out = self.__przeplatacz.rozplot(out)  
        return MapAlgorithm.proguj(out)

