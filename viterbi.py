from maszynaStanow import MaszynaStanow
from utils import odlegloscHamminga
from sciezka import Sciezka

class Viterbi:
    def __init__(self, maszynaStanow):
        self.__maszyna = maszynaStanow
        self.__sciezki = []

    # dane - podzielona paczka bitow
    def liczPierwszy(self, dane):
        pocz = self.__maszyna.getStanPoczatkowy()
        mozliweStany = self.__maszyna.getMozliwePrzejscia(pocz)
        for s in mozliweStany:
            sciezka = Sciezka()
            sciezka.dodajStan(s, odlegloscHamminga(dane, s[MaszynaStanow.OUT]))
            self.__sciezki.append(sciezka)
        return self.__sciezki

    def __oznaczKonflikty(self, doDodania):
        getHam = lambda el: el['hamming'] + el['sciezka'].getZakumulowanyHamming()
        getEndState = lambda el: el['krok'][MaszynaStanow.OUT_STATE]

        for i,el1 in enumerate(doDodania):
            if (el1['czyUsunac']):
                continue
            for j,el2 in enumerate(doDodania):
                if (i == j):
                    continue
                if (el2['czyUsunac']):
                    continue

                if (getEndState(el1) == getEndState(el2)):
                    if (getHam(el1) <= getHam(el2)):
                        el2['czyUsunac'] = True
                    else:
                        el1['czyUsunac'] = True

    def liczSciezke(self, dane):
        doDodania=[]
        for sciezka in self.__sciezki:
            sciezka.czyJuzRozszerzona = False
            przejscia = self.__maszyna.getMozliwePrzejscia(sciezka.getOstatniStan()[MaszynaStanow.OUT_STATE])
            for i, p in enumerate(przejscia):
                hamming = odlegloscHamminga(p[MaszynaStanow.OUT], dane)
                ob = {'sciezka': sciezka,
                      'krok': p,
                      'hamming': hamming,
                      'czyUsunac': False}
                doDodania.append(ob)

        self.__oznaczKonflikty(doDodania)
        outTab = list(filter(lambda x: not x['czyUsunac'], doDodania))

        for d in outTab:
            if(d['sciezka'].czyJuzRozszerzona == True):
                nowa = Sciezka.kopiujSciezke(d['sciezka'])
                nowa.dodajStan(d['krok'], d['hamming'])
                nowa.czyJuzRozszerzona = False
                self.__sciezki.append(d['sciezka'])
            else:
                d['sciezka'].dodajStan(d['krok'], d['hamming'])
                d['sciezka'].czyJuzRozszerzona = True
        return self.__sciezki

    def getSciezkiDochodzaceDoStanu(self, stan):
        out=[]
        for sciezka in self.__sciezki:
            s = sciezka.getOstatniStan()[MaszynaStanow.OUT_STATE]
            if(self.__maszyna.czyPolaczone(s, stan)):
                out.append(sciezka)
        return out

    def getSciezki(self):
        return self.__sciezki