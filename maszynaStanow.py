from rejestrPrzesuwny import RejestrPrzesuwny
class MaszynaStanow:
    def __init__(self, rejestr, ileNaRaz):
        self.__rej = rejestr
        self.__ileNaRaz=ileNaRaz
        self.__stany={}

        # lacznie z inputowymi 'komorkami',
        # wiec metoda getNumberOfStates()
        # nie moze byc
        ileStanow = 2**self.__rej.getDlugoscRejestru()
        szablon = '0%db' % self.__rej.getDlugoscRejestru()
        for i in range(ileStanow):
            self.__rej.reset()
            liczba = format(i, szablon)
 
            for bitStanu in reversed(liczba):
                b = 0
                if(bitStanu == '1'):
                    b=1
                self.__rej.shift(b)

            # kolejny stan to tak naprawde to, co bedzie
            # gdy zrobimy kolejnego shifta o ileNaRaz
            stanNaWyjsciu = str(self.__rej)[0:-ileNaRaz]
            outcome = list(self.__rej.licz())

            daneStanu = {'outputBits': outcome,
                         'destState': stanNaWyjsciu}
            self.__stany[liczba] = daneStanu  
        
    # zwraca slownik
    # [in] = inptBits
    # [out] = output bits
    # [inState] = inputState
    # [outState] = outputState
    def checkState(self, sourceState, inputBits):
        stateKey = ""
        for i in inputBits:
            stateKey += str(i)
        stateKey += sourceState
        
        st = self.__stany[stateKey]
        outputBits = st['outputBits']
        destState = st['destState']
        
        return {'in':inputBits, 'out':outputBits,
                'inState':sourceState, 'outState':destState}

    def getNumberOfStates(self):
        return 2**(self.__rej.getDlugoscRejestru()-self.__ileNaRaz)
