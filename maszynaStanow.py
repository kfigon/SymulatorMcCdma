from rejestrPrzesuwny import RejestrPrzesuwny
class MaszynaStanow:
    def __init__(self, rejestr, ileNaRaz):
        self.__rej = rejestr
        self.__ileNaRaz=ileNaRaz
        self.__stany={}

        ileStanow = 2**self.__rej.getDlugoscRejestru()
        szablon = '0%db' % ileZmiennych
        for i in range(ileStanow):
            self.__rej.reset()
            liczba = format(i, szablon)
            
            
return out
        
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
