# podzial na rowno
class PrzetwornikSzeregowoRownolegly:
    def __init__(self, ileStrumieni):
        self.__ileStrumieni = ileStrumieni

    def rozdziel(self, dane):
        if len(dane) < self.__ileStrumieni or len(dane) % self.__ileStrumieni != 0:
            raise Exception("Niepodzielna ilosc danych {} i strumieni{}".format(str(len(dane)), str(self.__ileStrumieni)))
 
        out = []
        ileBitowNaStrumien = len(dane)//self.__ileStrumieni
        for s in range(self.__ileStrumieni):
            strumien = []
            for i in range(s*ileBitowNaStrumien, (s+1)*ileBitowNaStrumien):
                strumien.append(dane[i])
            out.append(strumien)

        return out
