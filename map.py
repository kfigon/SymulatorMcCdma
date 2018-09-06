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

    def gamma(self, stanPocz, stanKoncowy, dane, parzystosc, prawdopodo0=1/2, prawdopodo1=1/2):
        '''
        pojedyczna iteracja prawodobienstwa
        przejscia ze stanu s` do s
        s` = parametr stan
        zwraca gamma dla 0 i dla 1
        '''
        przejscie = self.__maszyna.getStan(stanPocz, stanKoncowy)
        out = mapujBit(przejscie['in'][0])
        
        g = self.__liczGammaInternal(prawdopodo0, prawdopodo1, dane, parzystosc, out)
        return g

    def __liczGammaInternal(self, prawdopodo0, prawdopodo1, dane, parzystosc, out):
        sumuj = lambda d, p, out:  d*out + p*out
        uk = 1
        return self.__ck*uk*math.exp(liczL(prawdopodo0,prawdopodo1)/2)*math.exp(self.__lc/2 *sumuj(dane,parzystosc, out))

    def alfa(self, alfa1, gamma1, alfa2, gamma2):
        '''poprzednie alfa i przejscie z niego do obecnego stanu
        dla obu sciezek'''
        return  alfa1*gamma1 + alfa2*gamma2

    def beta(self, beta1, gamma1, beta2, gamma2):
        return beta1*gamma1 + beta2*gamma2