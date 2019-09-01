from utils import bipolar, binar

class Modulator:
    def mapuj(self, bity):
        raise Exception('not implemented')

    def demapuj(self, symbole):
        raise Exception('not implemented')
        
class Qpsk(Modulator):
    def mapuj(self, bity):
        if len(bity) % 2 == 1:
            raise Exception("dlugosc bitow musi byc parzysta, jest {}".format(str(len(bity))))
        
        out = []
        for i in range(0, len(bity),2):
            bitI = bipolar(bity[i])
            bitQ = bipolar(bity[i+1])
            out.append(complex(bitI, bitQ)) 
        return out

    def demapuj(self, symbole):
        '''zwraca symbole bipolarne'''
        out = []
        for s in symbole:
            out.append(s.real)
            out.append(s.imag)
        return out

class Bpsk(Modulator):
    def mapuj(self, bity):
        return [complex(bipolar(b),0) for b in bity]    

    def demapuj(self, symbole):
        return [s.real for s in symbole]
