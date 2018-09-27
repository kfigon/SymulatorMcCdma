from przeplot import Przeplatacz
from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow
from utils import flat
from map import MapAlgorithm, mapujBit
import math

def budujDomyslnyKoder():
    r1 = RejestrPrzesuwny(3, [[1,2], [0,2]])
    r2 = RejestrPrzesuwny(3, [[1,2], [0,2]])
    return KoderTurbo(rejestr1 = r1, 
                            rejestr2 = r2,
                            przeplatacz=Przeplatacz(10))


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
        
        dane = list(map(mapujBit, dane))

        [systematyczne, par1, par2] = self.decombine(dane)
        przeplecioneSystematyczne = self.__przeplatacz.przeplot(systematyczne)
        
        podzielone1 = self.__rozdziel(systematyczne, par1)
        podzielone2 = self.__rozdziel(przeplecioneSystematyczne, par2)
        
        lu = [0 for _ in range(len(dane)//3)]
        wynikDekodera2 = None
        for _ in range(ileItracji):
            extr1 = map1.dekoduj(podzielone1, lu)
            przeplecioneExtr1 = self.__przeplatacz.przeplot(extr1)
            
            extr2 = map2.dekoduj(podzielone2, przeplecioneExtr1)
            wynikDekodera2 = extr2
            lu = self.__przeplatacz.rozplot(extr2)
            
        i=0
        for sys in systematyczne:
           wynikDekodera2[i] += lc*sys
           i+=1 
        return MapAlgorithm.proguj(wynikDekodera2)

