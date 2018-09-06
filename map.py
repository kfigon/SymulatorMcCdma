import math

def liczL(prawodobienstwo1, prawodopobienstwo0):
    return math.log(prawodobienstwo1/prawodopobienstwo0)

def decyzja(val):
    return 1 if val >=0 else -1
    
def mapujBit(val):
    return -1 if val == 0 else 1

class MapAlgorithm:
    def __init__(self, maszyna, Ck=1, Lc=5):
        '''
        algorytm MAP
        '''
        self.__maszyna = maszyna
        self.__ck = Ck
        self.__lc=Lc

    def gamma(self, stan, dane, parzystosc, prawdopodo0=1/2, prawdopodo1=1/2):
        '''
        pojedyczna iteracja prawodobienstwa
        przejscia ze stanu s` do s
        '''
        outPrzy0Bin = self.__maszyna.checkState(stan, [0])['out']
        outPrzy1Bin = self.__maszyna.checkState(stan, [1])['out']

        outPrzy0 = list(map(mapujBit, outPrzy0Bin))
        outPrzy1 = list(map(mapujBit, outPrzy1Bin))
        
        a = self.__liczGammaInternal(prawdopodo0, prawdopodo1, dane, parzystosc, outPrzy0)
        b = self.__liczGammaInternal(prawdopodo0, prawdopodo1, dane, parzystosc, outPrzy1)
        return (a,b)

    def __liczGammaInternal(self, prawdopodo0, prawdopodo1, dane, parzystosc, out):
        sumuj = lambda d, p, out:  d*out[0]+p*out[1]
        uk = 1
        return self.__ck*uk*math.exp(liczL(prawdopodo0,prawdopodo1)/2)*math.exp(self.__lc/2 *sumuj(dane,parzystosc, out))