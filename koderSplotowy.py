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
                    sciezka = Sciezka()
                    sciezka.dodajStan(s, odlegloscHamminga(porcja, s[MaszynaStanow.OUT]))
                    sciezki.append(sciezka)
            else:
                doDodania =[]
                wszystkieStany = m.getListaStanow()
                for potencjalnyKolejnyStan in wszystkieStany:
                    for sciezka in sciezki:
                        s = sciezka.getOstatniStan()[MaszynaStanow.OUT_STATE]
                        if (m.czyPolaczone(s, potencjalnyKolejnyStan)):
                            # dodac stan do sciezki - trzeba wydlubac obiekt
                            kolejnyKrokSciezki = m.getStan(s, potencjalnyKolejnyStan)
                            hamming = odlegloscHamminga(kolejnyKrokSciezki[MaszynaStanow.OUT], porcja)
                            ob = {'sciezka': sciezka, 'krok':kolejnyKrokSciezki, 'hamming': hamming}
                            if(len(doDodania) == 0):
                                doDodania.append(ob)
                                break
                            docelowyStanOb = kolejnyKrokSciezki[MaszynaStanow.OUT_STATE]
                            # wykrywanie konfliktow, wybor najlepszej sciezki
                            for naLiscie in doDodania:
                                docelowyStanL = naLiscie['krok'][MaszynaStanow.OUT_STATE]
                                if(docelowyStanOb == docelowyStanL):
                                    if(naLiscie['hamming'] > hamming):
                                        doDodania.remove(naLiscie)
                                        doDodania.append(ob)
                                else:
                                    doDodania.append(ob)

                juzRozszerzoneSciezki=[]
                for el in doDodania:
                    sciezka = el['sciezka']
                    if(sciezka in juzRozszerzoneSciezki):
                        nowa = sciezka.kopiujSciezke()
                        nowa.dodajStan(el['krok'], el['hamming'])
                        sciezki.append(nowa)
                    else:
                        sciezka.dodajStan(el['krok'], el['hamming'])
                        juzRozszerzoneSciezki.append(sciezka)

        return self.__traceBackNajlepszejSciezki(sciezki)
    
    def __traceBackNajlepszejSciezki(self, sciezki):
        najlepszaSciezka = sciezki[0]
        for s in sciezki:
            if(s.getZakumulowanyHamming() < najlepszaSciezka.getZakumulowanyHamming()):
                najlepszaSciezka = s

        return najlepszaSciezka.traceBack()

class Sciezka:
    def __init__(self):
        self.__stany = []
        self.__zakumulowanyStan = 0
        
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

    def kopiujSciezke(self):
        nowa = Sciezka()
        for i in range(len(self.__stany)-1):
            nowa.dodajStan(i,0)
        nowa.dodajStan(self.getOstatniStan(), self.getZakumulowanyHamming())
        return nowa

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
