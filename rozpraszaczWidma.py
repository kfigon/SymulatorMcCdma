class RozpraszaczWidma:
    def __init__(self, ileChipowNaBit):
        self.__ileChipowNaBit = ileChipowNaBit
    
    def rozpraszaj(self, dane, ciagRozpraszajacy):
        i = 0
        for d in dane:
            for _ in range(self.__ileChipowNaBit):
                yield d ^ ciagRozpraszajacy[i]
                i += 1
                if i >= len(ciagRozpraszajacy):
                    i = 0


class RozpraszaczBipolarny:
    def rozpraszajBipolarne(self, probki, ciag):
        j = 0
        out = []
        for i in range(len(probki)):
            if j >= len(ciag):
                j = 0
            out.append(probki[i] * ciag[j])
            j+=1
        return out

    def skupBipolarne(self, probki, ciag):
        return self.rozpraszajBipolarne(probki, ciag)