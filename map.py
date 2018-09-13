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

    def liczMetryki(self, odebrane):
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
    
        # print()
        for i,o in enumerate(odebrane):
            self.__liczGammaDlaSymbolu(gammy, i,o)
            self.__liczAlfaDlaSymbolu(alfy, gammy, i, o)
        
        # print()
        for i,o in enumerate(reversed(odebrane)):
            self.__liczBetaDlaSymbolu(bety, gammy, len(odebrane)-i-1, o)

        return (alfy, bety, gammy)

    def dekoduj(self, odebrane):
        (alfy, bety, gammy) = self.liczMetryki(odebrane)
        prawdopodobienstwa = []
        for i,o in enumerate(odebrane):
            p0 = self.liczPrawdopodobienstwa(o, i, alfy, bety, gammy, [0])
            p1 = self.liczPrawdopodobienstwa(o, i, alfy, bety, gammy, [1])
            prawdopodobienstwa.append([p0,p1])

        # normowanie
        for i,p in enumerate(prawdopodobienstwa):
            suma = sum(p)
            for j,px in enumerate(p):
                prawdopodobienstwa[i][j] = px/suma
        
        return prawdopodobienstwa

    def proguj(self, prawdopodobienstwa):
        out = []
        for p in prawdopodobienstwa:
            p0 = p[0]
            p1= p[1]
            
            l = 0
            if p1 == 0:
                out.append(0)
                continue
            elif p0 == 0:
                l = p1
            else:
                l = math.log(p1/p0)

            out.append(1 if l >=0 else 0)

        return out        

    def liczPrawdopodobienstwa(self, o, i, alfy, bety,gammy, spodziewanyNadanyBit):
        stany = self.__maszyna.getListaStanow()
        prawdopodobienstwa = 0.0
        for s in stany:
            przejscia = self.__maszyna.getMozliwePrzejscia(s)
            for p in przejscia:
                stanPocz = p['inState']
                stanKoncowy = p['outState']
                sk = int(stanKoncowy, 2)
                sp = int(stanPocz, 2)
                bitNadany = p['in']

                if bitNadany == spodziewanyNadanyBit:
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
                    uk = self.__uk,
                    Luk = self.__luk,
                    Lc = self.__lc)

                gs = int(stanPocz, 2)
                gk = int(stanKoncowy, 2)
                gammy[i][gs][gk] = g
                # print("g[{}][{}][{}] = {}".format(str(i),str(gs),str(gk), str(g))) 
        # print()