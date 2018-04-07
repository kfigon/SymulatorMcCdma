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
            if(p['danePrzejscia'][MaszynaStanow.OUT_STATE] == stanDocelowy):
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
                przejscie = {'danePrzejscia': p, 'hamming': hamming+poprzedniePrzejscie['hamming']}
                krok['przejscia'].append(przejscie)
        self.__trellis.append(krok)

    # dane - podzielona paczka bitow
    def liczPierwszy(self, dane):
        stanPoczatkowy = self.__maszyna.getStanPoczatkowy()
        przejscia = self.__maszyna.getMozliwePrzejscia(stanPoczatkowy)        
        krok = {'przejscia': []}

        for p in przejscia:
            hamming = odlegloscHamminga(dane, p[MaszynaStanow.OUT])
            przejscie = {'danePrzejscia': p, 'hamming': hamming}
            krok['przejscia'].append(przejscie)

        self.__trellis.append(krok)

    def traceback(self):
        out = []
        minimalnyHamming = -1

        for krok in self.__trellis:
            for p in krok['przejscia']:
                ham = p['hamming']
                if(minimalnyHamming == -1):
                    minimalnyHamming = ham
                elif(ham < minimalnyHamming):
                    minimalnyHamming = ham
        
        for krok in self.__trellis:
             for p in krok['przejscia']:
                if(p['hamming'] == minimalnyHamming):
                    out.extend(p['danePrzejscia'][MaszynaStanow.IN])

        return out
