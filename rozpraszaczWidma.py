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
    