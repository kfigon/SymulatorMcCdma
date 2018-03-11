from maszynaStanow import MaszynaStanow
from utils import odlegloscHamminga

class Viterbi:
    def __init__(self, maszynaStanow):
        self.__maszyna = maszynaStanow
        self.__sciezki = []

    # dane do policzenia w trakcie kroku
    def liczPierwszy(self, dane):
        pocz = self.__maszyna.getStanPoczatkowy()
        mozliweStany = self.__maszyna.getMozliwePrzejscia(pocz)
        for s in mozliweStany:
            sciezka = Sciezka()
            sciezka.dodajStan(s, odlegloscHamminga(dane, s[MaszynaStanow.OUT]))
            self.__sciezki.append(sciezka)
        return self.__sciezki

    def liczSciezke(self, dane):
        doDodania=[]
        for sciezka in self.__sciezki:
            przejscia = self.__maszyna.getMozliwePrzejscia(sciezka.getOstatniStan()[MaszynaStanow.OUT_STATE])
            for i, p in enumerate(przejscia):
                hamming = odlegloscHamminga(p[MaszynaStanow.OUT], dane)
                if(i==0):
                    ob = {'sciezka': sciezka, 'krok': p, 'hamming': hamming, 'nowaSciezka':False}
                    doDodania.append(ob)
                else:
                    nowa = sciezka.kopiujSciezke()
                    ob = {'sciezka': nowa, 'krok': p, 'hamming': hamming, 'nowaSciezka':True}
                    doDodania.append(ob)

        # usuwanie konfliktow


        for d in doDodania:
            if(d['nowaSciezka'] == True):
                d['sciezka'].dodajStan(d['krok'], d['hamming'])
                self.__sciezki.append(d['sciezka'])
            else:
                d['sciezka'].dodajStan(d['krok'], d['hamming'])


        return self.__sciezki

    def getSciezkiDochodzaceDoStanu(self, stan):
        out=[]
        for sciezka in self.__sciezki:
            s = sciezka.getOstatniStan()[MaszynaStanow.OUT_STATE]
            if(self.__maszyna.czyPolaczone(s, stan)):
                out.append(sciezka)
        return out

class Sciezka:
    def __init__(self):
        self.__stany = []
        self.__zakumulowanyStan = 0

    def dodajStan(self, stan, hamming):
        self.__zakumulowanyStan += hamming
        self.__stany.append(stan)

    def getOstatniStan(self)    :
        return self.__stany[len(self.__stany) - 1]

    def getDlugoscSciezki(self):
        return len(self.__stany)

    def traceBack(self):
        out = []
        for s in self.__stany:
            out.extend(s[MaszynaStanow.IN])
        return out

    def getZakumulowanyHamming(self):
        return self.__zakumulowanyStan

    def kopiujSciezke(self):
        nowa = Sciezka()
        for i in range(len(self.__stany) - 1):
            nowa.dodajStan(self.__stany[i], 0)
        nowa.dodajStan(self.getOstatniStan(), self.getZakumulowanyHamming())
        return nowa
