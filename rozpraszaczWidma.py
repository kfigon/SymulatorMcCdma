class IterateHelper:
    def __init__(self, dlugoscCiagu):
        self.j=0
        self.len = dlugoscCiagu

    def get(self):
        if self.j >= self.len:
            self.j=0
        
        toRet = self.j
        self.j += 1
        return toRet

class RozpraszaczBipolarny:
    def rozpraszajBipolarne(self, probki, ciag):
        ''' probki - symbole complex'''
        out = []
        it = IterateHelper(len(ciag))

        for p in probki:
            re = ciag[it.get()]
            im = ciag[it.get()]
            toAdd = complex(p.real*re, p.imag*im)
            out.append(toAdd)

        return out

    def skupBipolarne(self, probki, ciag):
        return self.rozpraszajBipolarne(probki, ciag)