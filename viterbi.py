from maszynaStanow import MaszynaStanow
from utils import odlegloscHamminga

class Viterbi:
    def __init__(self, maszynaStanow):
        self.__maszyna = maszynaStanow
        self.__trellis = []

    # stanDocelowy - str
    def __znajdzPoprzedniePrzejscie(self, stanDocelowy):
        poprzedniKrok = self.__trellis[len(self.__trellis)-1]
        for p in poprzedniKrok['przejscia']:
            if(p['usunac'] == False and p['danePrzejscia'][MaszynaStanow.OUT_STATE] == stanDocelowy):
                return p
        return None

    # dane - podzielona paczka bitow
    def licz(self, dane):
        assert(len(self.__trellis) > 0)

        stany = self.__maszyna.getListaStanow()
        krok = {'przejscia': []}
        for st in stany:
            przejscia = self.__maszyna.getMozliwePrzejscia(st)
            for p in przejscia:
                poprzedniePrzejscie = self.__znajdzPoprzedniePrzejscie(p[MaszynaStanow.IN_STATE])
                if(poprzedniePrzejscie is None):
                    continue

                hamming = odlegloscHamminga(dane, p[MaszynaStanow.OUT])
                przejscie = {'danePrzejscia': p, 'hamming': hamming+poprzedniePrzejscie['hamming'], 'usunac': False}
                krok['przejscia'].append(przejscie)
        
        self.__rozwiazKonflikty(krok)
        self.__trellis.append(krok)

    # dane - podzielona paczka bitow
    def liczPierwszy(self, dane):
        stanPoczatkowy = self.__maszyna.getStanPoczatkowy()
        przejscia = self.__maszyna.getMozliwePrzejscia(stanPoczatkowy)        
        krok = {'przejscia': []}

        for p in przejscia:
            hamming = odlegloscHamminga(dane, p[MaszynaStanow.OUT])
            przejscie = {'danePrzejscia': p, 'hamming': hamming, 'usunac': False}
            krok['przejscia'].append(przejscie)

        self.__trellis.append(krok)

    def traceback(self):
        out = []

        # przejscie z minimalnym hammingiem
        przejscie=None 
        ostatniKrok = self.__trellis[len(self.__trellis)-1]
        for p in ostatniKrok['przejscia']:
            if(p['usunac']==True):
                continue
            ham = p['hamming']
            if(przejscie is None):
                przejscie = p
            elif(ham < przejscie['hamming']):
                przejscie = p
        
        if(przejscie is None):
            raise RuntimeError('nie znaleziono najlepszej sciezki')

        for i in range(len(self.__trellis)-2, -1, -1):
            krok = self.__trellis[i]
            for p in krok['przejscia']:
                if(p['usunac']==True):
                    continue
                if(p['danePrzejscia'][MaszynaStanow.OUT_STATE] == 
                    przejscie['danePrzejscia'][MaszynaStanow.IN_STATE]):
                    out.extend(przejscie['danePrzejscia'][MaszynaStanow.IN])
                    przejscie = p
                    break

        out.extend(przejscie['danePrzejscia'][MaszynaStanow.IN])

        return list(reversed(out))

    def pisz(self):
        for i,krok in enumerate(self.__trellis):
            print('\n'+str(i))
            for p in krok['przejscia']:
                if(p['usunac'] == True):
                    continue
                d = p['danePrzejscia']
                przejscieStr = str(d[MaszynaStanow.IN_STATE]) + "->" + str(d[MaszynaStanow.OUT_STATE]) 
                print(przejscieStr + ", ham: " + str(p['hamming']))

    def __rozwiazKonflikty(self, krok):
        for i,p in enumerate(krok['przejscia']):
            if(p['usunac']==True):
                continue

            for j in range(len(krok['przejscia'])):
                if(i==j):
                    continue

                px = krok['przejscia'][j]
                if(p['danePrzejscia'][MaszynaStanow.OUT_STATE] == px['danePrzejscia'][MaszynaStanow.OUT_STATE]):

                    # pStr = str(p['danePrzejscia'][MaszynaStanow.IN_STATE]) + "->" + str(p['danePrzejscia'][MaszynaStanow.OUT_STATE]) 
                    # pxStr = str(px['danePrzejscia'][MaszynaStanow.IN_STATE]) + "->" + str(px['danePrzejscia'][MaszynaStanow.OUT_STATE]) 
                    # print('konflikt: ' + pStr + ", " + pxStr)
                    if(px['hamming'] >= p['hamming']):
                        px['usunac'] = True
                        p['usunac'] = False
                        # print('usuwam '+pxStr)
                    else:
                        p['usunac'] = True
                        px['usunac'] = False
                        # print('usuwam '+pStr)