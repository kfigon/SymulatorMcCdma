from rejestrPrzesuwny import RejestrPrzesuwny
class MaszynaStanow:
    def __init__(self, rejestr, ileNaRaz):
        self.__rej = rejestr
        self.__ileNaRaz=ileNaRaz
        self.__stany={}

        ileStanow = 2**self.__rej.getDlugoscRejestru()
        szablon = '0%db' % self.__rej.getDlugoscRejestru()
        for i in range(ileStanow):
            self.__rej.reset()
            liczba = format(i, szablon)
            inputs = liczba[0:ileNaRaz]
            stan = liczba[ileNaRaz:]
            for bitStanu in reversed(liczba):
                b = 0
                if(bitStanu == '1'):
                    b=1
                self.__rej.shift(b)

            stanNaWyjsciu = str(self.__rej)[ileNaRaz:]
            outcome = list(self.__rej.licz())

            daneStanu = {'outputBits':outcome, 'destState': stanNaWyjsciu}
            self.__stany[stan] = daneStanu
        print(self.__stany)
        print()
    # zwraca slownik
    # [in] = inptBits
    # [out] = output bits
    # [inState] = inputState
    # [outState] = outputState
    def checkState(self, sourceState, inputBits):
        st = self.__stany[sourceState]
        outputBits = st['outputBits']
        destState = st['destState']
        
        return {'in':inputBits, 'out':outputBits,
                'inState':sourceState, 'outState':destState}

    def getNumberOfStates(self):
        return len(self.__stany)
