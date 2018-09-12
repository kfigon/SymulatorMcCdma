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

import math

if __name__ =="__main__":
    def gamma(odebrane, zakodowane, uk=0, Luk=0, Lc=5):
        sumy = [x*y for x,y in zip(odebrane, zakodowane)]
        suma = sum(sumy)
        return math.exp(uk * Luk/2)*math.exp(Lc*suma/2)

    def alfa(a, g):
        '''poprzednie alfa i korespadujace z nim gamma'''
        return sum([x*y for x,y in zip(a, g)])
    def normuj(alfa, wszystkieAlfa):
        return alfa/sum(wszystkieAlfa)

    mapping = {
        '00':   [-1,-1],
        '02':   [1,1],
        '10':   [1,1],
        '12':   [-1,-1],
        '21':   [1,-1],
        '23':   [-1,1],
        '31':   [-1,1],
        '33':   [1,-1],
    }

    odebrane = [[0.3, 0.1], [-0.5, 0.2], [0.8, 0.5], [-0.5, 0.3]]
    Lc = 5
    Luk = 0 # prawdopodobienstwo Uk=1 -> 1/2
    uk = 123 # any, since Luk is 0
    g = [gamma(odebrane[0], mapping['00']), gamma(odebrane[0], mapping['02'])]
    print(g)

    a00n=alfa([1],[g[0]])
    a02n=alfa([1],[g[1]])
    
    a00 = normuj(a00n, [a00n, a02n])
    a02 = normuj(a02n,[a00n, a02n])

    print(a00, a02)

    g2 = [
        gamma(odebrane[1], mapping['00']),
        gamma(odebrane[1], mapping['02']),
        gamma(odebrane[1], mapping['21']),
        gamma(odebrane[1], mapping['23']),
        ]
    print(g2)

    a2n = [
        alfa([a00],[g2[0]]),
        alfa([a00],[g2[1]]),
        alfa([a02],[g2[2]]),
        alfa([a02],[g2[3]]),
    ]
    a2 = [normuj(i,a2n) for i in a2n]
    print(a2)
