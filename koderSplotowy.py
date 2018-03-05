from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow
import math

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
        self.reset()
        m = MaszynaStanow(self.__rejestr, self.__ileBitowNaRaz)
        podzielone = podziel(daneBinarne, self.__rejestr.getIleBitowWyjsciowych())

        sciezki = []
        for i, porcja in enumerate(podzielone):
            if(i == 0):
                pocz = m.getStanPoczatkowy()
                mozliweStany = m.getMozliwePrzejscia(pocz)
                for s in mozliweStany:
                    sciezka = Sciezka(m)
                    sciezka.dodajStan(s, odlegloscHamminga(porcja, s[MaszynaStanow.OUT]))
                    sciezki.append(sciezka)
            else:
                wszystkieStany = m.getListStanow()
                for potencjalnyKolejnyStan in wszystkieStany:
                    potencjalneSciezki =
                        self.__getPotencjalneSciezkiMogaceTraficDoStanu(potencjalnyKolejnyStan, sciezki, m)
                                
                        
            # else:
            #     wszystkieStany = m.getListaStanow()
            #     for potencjalnyStan in wszystkieStany:
            #         sciezkiDojsciaDoStanu = []
            #         for sciezka in sciezki:
            #             ostatniStan = sciezka.getOstatniStan()
            # nie tak. outState to stan wejsciowy dla nowego stanu ;<
            #             if(ostatniStan[MaszynaStanow.OUT_STATE] == potencjalnyStan):

        return self.__traceBackNajlepszejSciezki(sciezki)
    
    def __traceBackNajlepszejSciezki(self, sciezki):
        najlepszaSciezka = sciezki[0]
        for s in sciezki:
            if(s.getZakumulowanyHamming() < najlepszaSciezka.getZakumulowanyHamming()):
                najlepszaSciezka = s

        return najlepszaSciezka.traceBack()
    
class Sciezka:
    def __init__(self, maszynaStanow):
        self.__stany = []
        self.__zakumulowanyStan = 0
        self.__maszynaStanow = maszynaStanow
        
    def dodajStan(self, stan, hamming):
        self.__zakumulowanyStan += hamming
        self.__stany.append(stan)

    def getOstatniStan(self):
        return self.__stany[len(self.__stany)-1]

    def traceBack(self):
        out = []
        for s in self.__stany:
            out.extend(s[MaszynaStanow.IN])
        return out

    def getZakumulowanyHamming(self):
        return self.__zakumulowanyStan

    # czy z ostatniego stanu sciezki mozna dosc do stanu x
    def czyJestDojscie(self, stan):
        # moze 'stan' 'stan2' i w wywolaniu getOstatniStan? latwiej testowac
        # albo przeniesc do maszynyStanow to, chyba najlepiej
        ostatniStan = self.getOstatniStan()
        
        pass

# utils
def odlegloscHamminga(daneA, daneB):
    assert (len(daneA) == len(daneB))
    roznica = 0
    for i in range(len(daneA)):
        if (daneA[i] != daneB[i]):
            roznica += 1
    return roznica

# utils
def podziel(dane, ileNaRaz):
    assert (len(dane) % ileNaRaz == 0)
    out=[None]* (len(dane)//ileNaRaz)
    for i in range(len(out)):
        out[i] = dane[i*ileNaRaz: ((i+1)*ileNaRaz)]

    return out
