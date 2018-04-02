from maszynaStanow import MaszynaStanow

class Sciezka:
    def __init__(self):
        self.stany = []
        self.__zakumulowanyStan = 0

    def dodajStan(self, stan, hamming):
        self.__zakumulowanyStan += hamming
        self.stany.append(stan)

    def getOstatniStan(self):
        return self.stany[len(self.stany) - 1]

    def getDlugoscSciezki(self):
        return len(self.stany)

    def traceBack(self):
        out = []
        for s in self.stany:
            out.extend(s[MaszynaStanow.IN])
        return out

    def getZakumulowanyHamming(self):
        return self.__zakumulowanyStan

    def kopiujSciezke(self):
        if(len(self.stany)==0):
            return Sciezka()

        nowa = Sciezka()
        for i in range(len(self.stany) - 1):
            nowa.dodajStan(self.stany[i], 0)
        nowa.dodajStan(self.getOstatniStan(), self.getZakumulowanyHamming())
        return nowa

    def __str__(self):
        nap = ''
        for s in self.stany:
            nap += s[MaszynaStanow.IN_STATE]+' -> '+s[MaszynaStanow.OUT_STATE]+', '
        nap += ' ham: ' + str(self.getZakumulowanyHamming())
        return nap

    def __eq__(self, other):
        if(other.getDlugoscSciezki() != self.getDlugoscSciezki()):
            return False

        for i in range(self.getDlugoscSciezki()):
            x = self.stany[i]
            y = other.stany[i]
            if(x[MaszynaStanow.IN_STATE] != y[MaszynaStanow.IN_STATE] or
            y[MaszynaStanow.OUT_STATE] != x[MaszynaStanow.OUT_STATE]):
                return False
        return True