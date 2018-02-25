from rejestrPrzesuwny import RejestrPrzesuwny
class MaszynaStanow:
    def __init__(self, rejestr, ileNaRaz):
        self.__rej = rejestr
        self.__ileNaRaz=ileNaRaz
        self.__stany={}

        # stan w srodku to
        # bityWej_StaNRej
        # 001 - stan 01, wejscie 0

        # lacznie z inputowymi 'komorkami',
        # wiec metoda getNumberOfStates()
        # nie moze byc
        permutacjeBinarne = self.__getPermutacje(self.__rej.getDlugoscRejestru())
        for liczba in permutacjeBinarne:
            self.__rej.reset()
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
        stateKey = self.__budujKluczStanu(sourceState, inputBits)
        
        st = self.__stany[stateKey]
        outputBits = st['outputBits']
        destState = st['destState']
        
        return {'in':inputBits, 'out':outputBits,
                'inState':sourceState, 'outState':destState}

    def __budujKluczStanu(self, state, inputBits):
        stateKey = ""
        for i in inputBits:
            stateKey += str(i)
        stateKey += state
        return stateKey
    
    def getMozliwePrzejscia(self, stan):
        out = []
        for klucz in self.__stany:
            source = klucz[self.__ileNaRaz:]
            inputs = str2List(klucz[:self.__ileNaRaz])
            st = self.checkState(source, inputs)
            if(st['inState']==stan):
                out.append(st)
        return out
    
    def getMozliweDojscia(self, stan):
        out = []
        for klucz in self.__stany:
            source = klucz[self.__ileNaRaz:]
            inputs = str2List(klucz[:self.__ileNaRaz])
            st = self.checkState(source, inputs)
            if(st['outState']==stan):
                out.append(st)
        return out
    
    def __getPermutacje(self, ileZmiennych):
        ileStanow = 2**ileZmiennych
        szablon = '0%db' % ileZmiennych
        out = [None] * ileStanow
        
        for i in range(ileStanow):
            out[i] = format(i, szablon)
        return out

    def getNumberOfStates(self):
        return 2**(self.__rej.getDlugoscRejestru()-self.__ileNaRaz)

    def getStanPoczatkowy(self):
        ile = self.__rej.getDlugoscRejestru() - self.__ileNaRaz
        szablon = '0%db' % ile
        return format(0, szablon)

def str2List(data):
    out = [0]*len(data)
    for i in range(len(data)):
        out[i]=int(data[i])
    return out


