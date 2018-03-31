from maszynaStanow import MaszynaStanow

class Sciezka:
    def __init__(self):
        self.__stany = []
        self.__zakumulowanyStan = 0
        self.czyJuzRozszerzona = False

    def dodajStan(self, stan, hamming):
        self.__zakumulowanyStan += hamming
        self.__stany.append(stan)

    def getOstatniStan(self):
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
        if(len(self.__stany)==0):
            return Sciezka()

        nowa = Sciezka()
        for i in range(len(self.__stany) - 1):
            nowa.dodajStan(self.__stany[i], 0)
        nowa.dodajStan(self.getOstatniStan(), self.getZakumulowanyHamming())
        return nowa

    def __str__(self):
        nap = ''
        for s in self.__stany:
            nap += s[MaszynaStanow.IN_STATE]+' -> '+s[MaszynaStanow.OUT_STATE]+', '
        nap += ' ham: ' + str(self.getZakumulowanyHamming())
        return nap