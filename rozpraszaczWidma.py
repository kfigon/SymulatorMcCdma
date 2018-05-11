class RozpraszaczWidma:
    def __init__(self, ileChipowNaBit):
        self.__ileChipowNaBit = ileChipowNaBit
    
    def __rozpraszaj(self,dane, ciag):
        i = 0
        for d in dane:
            for _ in range(self.__ileChipowNaBit):
                yield d ^ ciag[i]
                i +=1

    def rozpraszaj(self, dane, ciagRozpraszajacy):
        if (len(dane)*self.__ileChipowNaBit) != len(ciagRozpraszajacy):
            raise Exception('Nieprawidlowe dlugosci ciagow. Dane {}, ciag {}, ileChipowNaBit {}'.format(str(len(dane)), str(len(ciagRozpraszajacy)), str(self.__ileChipowNaBit)))

        return self.__rozpraszaj(dane, ciagRozpraszajacy)
    