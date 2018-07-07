import math
import utils
import numpy as np

class WalidatorPredkosciSygnalow:
    @staticmethod
    def waliduj(fn, fb, fp):
        if fn < fb:
            return False
        # nosna >= bity
        # probkowanie podzielne przez bity
        # nosna podzielna przez bity
        # nyquist
        return (fp % fn == 0) and (fn % fb == 0) and (fn <= fp/2)

class Qpsk:
    def __init__(self, fp, fn, fb, ampl=1):
        '''
        :param fp: cz. probkowania
        :param fn: cz. nosnej
        :param fb: cz. bitow (2 razy wieksza niz symboli)
        :param ampl:
        '''
        self.__fp = fp
        self.__fn = fn
        self.__fb = fb
        self.__ampl = ampl

    def mapujSymbole(self, dane):
        for i in range(0, len(dane)-1, 2):
            yield complex(dane[i], dane[i+1])

    def __ileProbekNaSymbol(self):
        return self.__fp//self.__fb

    def moduluj(self, dane):
        if(len(dane) % 2 != 0):
            raise Exception('Dlugosc danych powinna byc parzysta, jest {}'.format(str(len(dane))))
        
        symbole = self.mapujSymbole(dane)
        ileProbekNaSymbol = self.__ileProbekNaSymbol()

        out = []
        t = 0
        timeStep = 1/self.__fp

        for s in symbole:
            i = s.real
            q = s.imag
            faza = self.__symbol2Faza(i,q)
            for _ in range(ileProbekNaSymbol):
                x = self.__ampl*math.cos(faza)*math.cos(2*math.pi*self.__fn*t)
                y = self.__ampl*math.sin(faza)*math.sin(2*math.pi*self.__fn*t)
                t += timeStep
                out.append(x-y)
        
        return out

    def __symbol2Faza(self, i, q):
        if(i == 0 and q == 0):
            return math.pi/4
        elif(i == 0 and q == 1):
            return 3*math.pi / 4
        elif (i == 1 and q == 0):
            return 5*math.pi / 4
        elif (i == 1 and q == 1):
            return 7*math.pi / 4
        raise Exception('Blad, nie ma fazy dla: I{}, Q{}'.format(str(i), str(q)))
    
    def __decyzjaBitowa(self, calkaI, calkaQ):
            if(calkaI >= 0 and calkaQ >= 0):
                return [0,0]
            elif(calkaI < 0 and calkaQ >= 0):
                return [0,1]
            elif(calkaI < 0 and calkaQ < 0):
                return [1,0]
            else:
                return [1,1]

    def demodulacja(self, odebrany):
        ileProbekNaSymbol = self.__ileProbekNaSymbol()

        out = []
        calkaI = 0
        calkaQ = 0
        t = 0
        timeStep = 1/self.__fp

        licznikProbekDoCalki = 0
        for o in odebrany:
            nosnaI = self.__ampl*math.cos(2*math.pi*self.__fn*t)
            nosnaQ = (-1) * self.__ampl*math.sin(2*math.pi*self.__fn*t)
            t += timeStep

            calkaI += nosnaI*o
            calkaQ += nosnaQ*o
            
            licznikProbekDoCalki += 1
            if licznikProbekDoCalki >= ileProbekNaSymbol:
                out.extend(self.__decyzjaBitowa(calkaI, calkaQ))
                calkaI = 0
                calkaQ = 0
                licznikProbekDoCalki=0
        
        # jesli zostaly resztki - nie powinny
        if(calkaI != 0 and calkaQ != 0):
            print("Zostaly resztki z calki %d, %d" % (calkaI, calkaQ))
            out.extend(self.__decyzjaBitowa(calkaI, calkaQ))

        return out