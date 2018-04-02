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

    def __rozgaleziajSciezki(self, doDodania):
        # poszukac duplikatow - te same sciezki
        # pierwsza z nich nowaSciezka:False
        # reszta nowaSciezka:True i kopie + podmianka ['sciezka']
        ktoreJuzByly = []
        for i in doDodania:
            if (i['sciezka'] in ktoreJuzByly):
                continue
            duplikaty = list(filter(lambda el: el['sciezka'] == i['sciezka'], doDodania))
            for d in range(len(duplikaty)):
                if(d == 0):
                    duplikaty[0]['nowaSciezka'] = False
                    ktoreJuzByly.append(duplikaty[0]['sciezka'])
                else:
                    nowa = Sciezka.kopiujSciezke(duplikaty[d]['sciezka'])
                    duplikaty[d]['sciezka'] = nowa
                    duplikaty[d]['nowaSciezka'] = True

    def liczSciezke(self, dane):
        doDodania=[]
        for sciezka in self.__sciezki:
            przejscia = self.__maszyna.getMozliwePrzejscia(sciezka.getOstatniStan()[MaszynaStanow.OUT_STATE])
            for i, p in enumerate(przejscia):
                hamming = odlegloscHamminga(p[MaszynaStanow.OUT], dane)
                ob = {'sciezka': sciezka, 'krok': p,
                      'hamming': hamming, 'czyUsunac': False,
                      'nowaSciezka': False}
                doDodania.append(ob)

        self.__oznaczKonflikty(doDodania)
        outTab = list(filter(lambda x: not x['czyUsunac'], doDodania))
        self.__rozgaleziajSciezki(outTab)

        for d in outTab:
            d['sciezka'].dodajStan(d['krok'], d['hamming'])
            if (d['nowaSciezka'] == True):
                self.__sciezki.append(d['sciezka'])

        return self.__sciezki

    def wyfiltrujSciezkiKtoreNieSkonczyly(self, dlugoscPodzielonychDanych):
        self.__sciezki = list(filter(
            lambda s: s.getDlugoscSciezki() == dlugoscPodzielonychDanych,
            self.__sciezki))

    def getSciezkiDochodzaceDoStanu(self, stan):
        out=[]
        for sciezka in self.__sciezki:
            s = sciezka.getOstatniStan()[MaszynaStanow.OUT_STATE]
            if(self.__maszyna.czyPolaczone(s, stan)):
                out.append(sciezka)
        return out

    def getSciezki(self):
        return self.__sciezki