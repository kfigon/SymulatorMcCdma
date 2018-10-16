from rejestrPrzesuwny import RejestrPrzesuwny
from utils import str2List

class MaszynaStanow:
    IN = 'in'
    OUT = 'out'
    IN_STATE = 'inState'
    OUT_STATE = 'outState'

    def __init__(self, rejestr, ileNaRaz=1):
        self.__rej = rejestr
        self.__ileNaRaz=ileNaRaz
        self.__stany={}

        # stan w srodku to
        # bityWej_StaNRej
        # 001 - stan 01, wejscie 0
        permutacjeWejsc = self.__getPermutacje(ileNaRaz)
        permutacjeStanow = self.__getPermutacje(self.__rej.getDlugoscRejestru())
        for stan in permutacjeStanow:
            for wejscie in permutacjeWejsc:
                self.__rej.reset()            
                self.__rej.injectState(stan, int(wejscie))

                stanNaWyjsciu = self.__rej.getStateAfterShift()
                outcome = list(self.__rej.licz())

                daneStanu = {'outputBits': outcome,
                            'destState': stanNaWyjsciu}
                klucz = wejscie + stan
                self.__stany[klucz] = daneStanu  

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

    # zwraca slownik
    # input - str stanu np. '00'
    def getMozliwePrzejscia(self, stan):
        out = []
        for klucz in self.__stany:
            source = klucz[self.__ileNaRaz:]
            inputs = str2List(klucz[:self.__ileNaRaz])
            st = self.checkState(source, inputs)
            if(st['inState']==stan):
                out.append(st)
        return out

    # zwraca slownik
    # input - str stanu np. '00'
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
        return 2**(self.__rej.getDlugoscRejestru())

    # zwraca oznaczenie stanu (str)
    def getStanPoczatkowy(self):
        ile = self.__rej.getDlugoscRejestru()
        szablon = '0%db' % ile
        return format(0, szablon)

    # zwraca oznaczenia stanow (str)
    def getListaStanow(self):
        return self.__getPermutacje(self.__rej.getDlugoscRejestru())

    # przyjmuje oznaczenia stanow (str)
    def czyPolaczone(self, stan1, stan2):
        dojscia = self.getMozliweDojscia(stan2)
        for d in dojscia:
            if(stan1 == d[MaszynaStanow.IN_STATE]):
                return True
        return False

    # zwraca obiekt na podstawie dwoch stringow.
    # MUSI byc polaczenie!
    def getStan(self, stanPocz, stanKonc):
        przejscia = self.getMozliwePrzejscia(stanPocz)
        for p in przejscia:
            if(p[MaszynaStanow.OUT_STATE] == stanKonc):
                return p
        return None
