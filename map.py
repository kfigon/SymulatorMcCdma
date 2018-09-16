import math
from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow

def mapujBit(val):
    return -1 if val == 0 else 1

def gamma(odebrane, zakodowane, Luk, Lc):
    iloczyny = [x*y for x,y in zip(odebrane, zakodowane)]
    suma = sum(iloczyny)
    uk = 1 if Luk >=0 else -1
    return math.exp(uk * Luk/2)*math.exp(Lc*suma/2)

def alfa(a, g):
    '''poprzednie alfa i korespondujace z nim gamma'''
    return sum([x*y for x,y in zip(a, g)])

def normujAlfa(alfa, wszystkieAlfa):
    return alfa/sum(wszystkieAlfa)

def mapujP(p):
    if p[1] == 0:
        return -10
    elif p[0] == 0:
        return 10
    else:
        return math.log(p[1]/p[0])

class MapAlgorithm:
    def __init__(self, maszyna, Lc=5):
        '''
        algorytm MAP
        '''
        self.__maszyna = maszyna
        self.__lc=Lc # miara jakosci kanalu

    def liczMetryki(self, odebrane, lu=[]):
        '''liczy iteracje map
        odebrane w formie 2 wymiarowej tablicy - [ [symbol1], [symbol2] ]'''
        
        # wyliczyc wszystkie gamma
        # wyliczyc wszystkie alfa (+ normowanie)
        # beta
        # wyliczyc L, decyzja przy ostatniej iteracji.

        ileStanow = self.__maszyna.getNumberOfStates()
        ileOdebranychSymboli = len(odebrane)
        
        alfy = [[0 for _ in range(ileStanow)] for _ in range(ileOdebranychSymboli+1)]
        bety = [[0 for _ in range(ileStanow)] for _ in range(ileOdebranychSymboli+1)]
        gammy = [ [[0 for _ in range(ileStanow)] for _ in range(ileStanow)] for _ in range(ileOdebranychSymboli) ]

        # pewne stany
        alfy[0][0] = 1
        bety[ileOdebranychSymboli][0]=1
    
        if len(lu) == 0:
            lu = [0 for _ in range(len(odebrane))]

        i=0
        for o,luk in zip(odebrane, lu):
            self.__liczGammaDlaSymbolu(gammy, i,o, luk)
            self.__liczAlfaDlaSymbolu(alfy, gammy, i, o)
            i+=1

        for i,o in enumerate(reversed(odebrane)):
            self.__liczBetaDlaSymbolu(bety, gammy, len(odebrane)-i-1, o)

        return (alfy, bety, gammy)

    def dekoduj(self, odebrane, lu=[]):
        (alfy, bety, gammy) = self.liczMetryki(odebrane, lu)
        prawdopodobienstwa = []
        for i in range(len(odebrane)):
            p0 = self.liczPrawdopodobienstwa(i, alfy, bety, gammy, [0])
            p1 = self.liczPrawdopodobienstwa(i, alfy, bety, gammy, [1])
            prawdopodobienstwa.append([p0,p1])
        
        # print(prawdopodobienstwa)
        # normowanie
        sumy = list(map(lambda ps: sum(ps), prawdopodobienstwa))
        
        i=0
        for ps, s in zip(prawdopodobienstwa, sumy):
            prawdopodobienstwa[i][0] = ps[0]/s
            prawdopodobienstwa[i][1] = ps[1]/s
            i+=1

        out = list(map(mapujP, prawdopodobienstwa))
        return out

    @staticmethod
    def proguj(prawdopodobienstwa):
        out = []
        for p in prawdopodobienstwa:
            out.append(1 if p >=0 else 0)
        
        return out        

    def liczPrawdopodobienstwa(self, i, alfy, bety,gammy, spodziewanyNadanyBit):
        stany = self.__maszyna.getListaStanow()
        prawdopodobienstwa = 0.0
        for s in stany:
            przejscia = self.__maszyna.getMozliwePrzejscia(s)
            for p in przejscia:
                bitNadany = p['in']
                if bitNadany != spodziewanyNadanyBit:
                    continue

                stanPocz = p['inState']
                stanKoncowy = p['outState']
                sk = int(stanKoncowy, 2)
                sp = int(stanPocz, 2)
                
                prawdopodobienstwa += alfy[i][sp]*gammy[i][sp][sk]*bety[i+1][sk]
        return prawdopodobienstwa

    def __liczBetaDlaSymbolu(self, bety, gammy, i, o):
        stany = self.__maszyna.getListaStanow()
        for s in stany:
            dojscia = self.__maszyna.getMozliweDojscia(s)
            for d in dojscia:
                stanPoczatkowy = d['inState']     
                stanKoncowy = d['outState']                
                sk = int(stanKoncowy, 2)
                sp = int(stanPoczatkowy, 2)

                zwykleB = bety[i+1][sk] * gammy[i][sp][sk]
                bety[i][sp] += zwykleB

        sumaBet = sum(bety[i])

        for j,b in enumerate(bety[i]):
            bety[i][j] = b/sumaBet
            # print("b[{}][{}] = {}".format(str(i),str(j),str(bety[i][j])))
        # print()


    def __liczAlfaDlaSymbolu(self, alfy, gammy, i, o):
        stany = self.__maszyna.getListaStanow()
        for s in stany:
            dojscia = self.__maszyna.getMozliweDojscia(s)
            for d in dojscia:
                stanPoczatkowy = d['inState']     
                stanKoncowy = d['outState']                
                sk = int(stanKoncowy, 2)
                sp = int(stanPoczatkowy, 2)

                zwykleA = alfy[i][sp] * gammy[i][sp][sk]
                alfy[i+1][sk] += zwykleA

        sumaAlf = sum(alfy[i+1])

        # todo: na koncu normuje tez nieistniejace przejscia.
        # nie wiem czy to blad, ale inaczej niz w przykladach
        # todo: dla beta tez tak jest
        for j,a in enumerate(alfy[i+1]):
            alfy[i+1][j] = a/sumaAlf
            # print("a[{}][{}] = {}".format(str(i+1),str(j),str(alfy[i+1][j])))
        # print()

    def __liczGammaDlaSymbolu(self, gammy, i,o, luk):
        stany = self.__maszyna.getListaStanow()
        for s in stany:
            przejscia = self.__maszyna.getMozliwePrzejscia(s)
            for p in przejscia:
                stanPocz = p['inState']
                stanKoncowy = p['outState']
                codedBits = list(map(mapujBit, p['out']))

                g = gamma(odebrane=o,
                    zakodowane = codedBits,
                    Luk = luk,
                    Lc = self.__lc)

                gs = int(stanPocz, 2)
                gk = int(stanKoncowy, 2)
                gammy[i][gs][gk] = g
                # print("g[{}][{}][{}] = {}".format(str(i),str(gs),str(gk), str(g))) 
        # print()


def main():
    #todo remove imports
    odczepy = [[0,1,2],[0,2]]
    rej = RejestrPrzesuwny(3, odczepy)
    maszyna = MaszynaStanow(rej, 1)
    m = MapAlgorithm(maszyna)

    odebrane = [[0.3,0.1],[-0.5,0.2],[0.8,0.5],[-0.5,0.3],[0.1,-0.7],[1.5,-0.4]]
    apriori = [-12, -5, -1, 1, 1, 1]

    res1 = m.dekoduj(odebrane)
    res2 = m.dekoduj(odebrane, apriori)

    print()
    print(res1)
    print(res2)

# main()