import math

def liczL(prawodobienstwo1, prawodopobienstwo0):
    return math.log(prawodobienstwo1/prawodopobienstwo0)

def decyzja(val):
    return 1 if val >=0 else -1

def mapujBit(val):
    return -1 if val == 0 else 1

def gamma(odebrane, zakodowane, uk, Luk, Lc):
    iloczyny = [x*y for x,y in zip(odebrane, zakodowane)]
    suma = sum(iloczyny)
    return math.exp(uk * Luk/2)*math.exp(Lc*suma/2)

def alfa(a, g):
    '''poprzednie alfa i korespadujace z nim gamma'''
    return sum([x*y for x,y in zip(a, g)])

def normujAlfa(alfa, wszystkieAlfa):
    return alfa/sum(wszystkieAlfa)


class MapAlgorithm:
    def __init__(self, maszyna, uk=0, Luk=0, Lc=5):
        '''
        algorytm MAP
        '''
        self.__maszyna = maszyna
        self.__uk=uk # ?
        self.__luk=Luk # prawdopodobienstwo zajscia uk
        self.__lc=Lc # miara jakosci kanalu

    def licz(self, odebrane, apriori=[]):
        '''liczy iteracje map
        odebrane w formie 2 wymiarowej tablicy - [ [symbol1], [symbol2] ]'''
        
        # wyliczyc wszystkie gamma
        # wyliczyc wszystkie alfa (+ normowanie)
        # beta
        # wyliczyc L, decyzja przy ostatniej iteracji.
        if len(apriori) == 0:
            pass # todo: zainicjalizowac zerami jesli nie podano. jesli podano to wyrzkosyatc

        ileStanow = self.__maszyna.getNumberOfStates()
        ileOdebranychSymboli = len(odebrane)
        
        alfy = [[0 for _ in range(ileStanow)] for _ in range(ileOdebranychSymboli)]
        bety = [[0 for _ in range(ileStanow)] for _ in range(ileOdebranychSymboli)]
        gammy = [ [[0 for _ in range(ileStanow)] for _ in range(ileStanow)] for _ in range(ileOdebranychSymboli) ]

        # pewne stany
        alfy[0][0] = 1
        bety[ileOdebranychSymboli-1][0]=1

        # gammas
    
        for i,o in enumerate(odebrane):
        # o = odebrane[0]
            self.__liczGammaGammaDlaSymbolu(gammy, i,o)


        return [1,2,3]
    def __liczGammaGammaDlaSymbolu(self, gammy, i,o):
        stany = self.__maszyna.getListaStanow()
        for s in stany:
            przejscia = self.__maszyna.getMozliwePrzejscia(s)
            for p in przejscia:
                stanPocz = p['inState']
                stanKoncowy = p['outState']
                codedBits = list(map(mapujBit, p['out']))

                g = gamma(odebrane=o,
                    zakodowane = codedBits,
                    uk = self.__uk,
                    Luk = self.__luk,
                    Lc = self.__lc)

                gs = int(stanPocz, 2)
                gk = int(stanKoncowy, 2)
                gammy[i][gs][gk] = g
                # print("g[{}][{}][{}] = {}".format(str(i),str(gs),str(gk), str(g))) 
    
# if __name__ =="__main__":

    # mapping = {
    #     '00':   [-1,-1],
    #     '02':   [1,1],
    #     '10':   [1,1],
    #     '12':   [-1,-1],
    #     '21':   [1,-1],
    #     '23':   [-1,1],
    #     '31':   [-1,1],
    #     '33':   [1,-1],
    # }

    # odebrane = [[0.3, 0.1], [-0.5, 0.2], [0.8, 0.5], [-0.5, 0.3]]
    # Lc = 5
    # Luk = 0 # prawdopodobienstwo Uk=1 -> 1/2
    # uk = 123 # any, since Luk is 0
    # g = [gamma(odebrane[0], mapping['00']), gamma(odebrane[0], mapping['02'])]
    # print(g)

    # a00n=alfa([1],[g[0]])
    # a02n=alfa([1],[g[1]])
    
    # a00 = normuj(a00n, [a00n, a02n])
    # a02 = normuj(a02n,[a00n, a02n])

    # print(a00, a02)

    # g2 = [
    #     gamma(odebrane[1], mapping['00']),
    #     gamma(odebrane[1], mapping['02']),
    #     gamma(odebrane[1], mapping['21']),
    #     gamma(odebrane[1], mapping['23']),
    #     ]
    # print(g2)

    # a2n = [
    #     alfa([a00],[g2[0]]),
    #     alfa([a00],[g2[1]]),
    #     alfa([a02],[g2[2]]),
    #     alfa([a02],[g2[3]]),
    # ]
    # a2 = [normuj(i,a2n) for i in a2n]
    # print(a2)
