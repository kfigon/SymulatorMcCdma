import math
from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow

def mapujBit(val):
    return -1 if val == 0 else 1

def gamma(odebrane, zakodowane, Lc):
    suma = zakodowane[1]*odebrane[1]
    return math.exp(Lc*suma/2)

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
        self.__wyliczoneMetryki = None # cache, nie ma potrzeby wyliczac od nowa co iteracje

    def liczMetryki(self, odebrane):
        '''liczy iteracje map
        odebrane w formie 2 wymiarowej tablicy - [ [symbol1], [symbol2] ]'''
        if self.__wyliczoneMetryki is not None:
            return self.__wyliczoneMetryki

        ileStanow = self.__maszyna.getNumberOfStates()
        ileOdebranychSymboli = len(odebrane)
        
        alfy = [[0 for _ in range(ileStanow)] for _ in range(ileOdebranychSymboli+1)]
        bety = [[0 for _ in range(ileStanow)] for _ in range(ileOdebranychSymboli+1)]
        gammy = [ [[0 for _ in range(ileStanow)] for _ in range(ileStanow)] for _ in range(ileOdebranychSymboli) ]

        # pewne stany
        alfy[0][0] = 1
        for i in range(len(bety[ileOdebranychSymboli])):
            bety[ileOdebranychSymboli][i]=1/ileStanow


        for i,o in enumerate(odebrane):
            self.__liczGammaDlaSymbolu(gammy, i,o)
            self.__liczAlfaDlaSymbolu(alfy, gammy, i, o)

        for i,o in enumerate(reversed(odebrane)):
            self.__liczBetaDlaSymbolu(bety, gammy, len(odebrane)-i-1, o)

        self.__wyliczoneMetryki = (alfy, bety, gammy)
        return self.__wyliczoneMetryki

    def dekoduj(self, odebrane):
        (alfy, bety, gammy) = self.liczMetryki(odebrane)
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
        for j,a in enumerate(alfy[i+1]):
            alfy[i+1][j] = a/sumaAlf
            # print("a[{}][{}] = {}".format(str(i+1),str(j),str(alfy[i+1][j])))
        # print()

    def __liczGammaDlaSymbolu(self, gammy, i,o):
        stany = self.__maszyna.getListaStanow()
        for s in stany:
            przejscia = self.__maszyna.getMozliwePrzejscia(s)
            for p in przejscia:
                stanPocz = p['inState']
                stanKoncowy = p['outState']
                codedBits = list(map(mapujBit, p['out']))

                g = gamma(odebrane=o,
                    zakodowane = codedBits,
                    Lc = self.__lc)

                gs = int(stanPocz, 2)
                gk = int(stanKoncowy, 2)
                gammy[i][gs][gk] = g
                # print("g[{}][{}][{}] = {}".format(str(i),str(gs),str(gk), str(g))) 
        # print()
