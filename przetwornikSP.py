class PrzetwornikSzeregowoRownolegly:
    def __init__(self, ileStrumieni):
        '''dzieli po rowno na ileStrumieni kanalow'''
        self.__ileStrumieni = ileStrumieni

    def rozdziel(self, dane):
        if len(dane) < self.__ileStrumieni or len(dane) % self.__ileStrumieni != 0:
            raise Exception("Niepodzielna ilosc danych {} i strumieni {}".format(str(len(dane)), str(self.__ileStrumieni)))
 
        out = []
        ileBitowNaStrumien = len(dane)//self.__ileStrumieni
        for i in range(self.__ileStrumieni):
            out.append(dane[i*ileBitowNaStrumien:(i+1)*ileBitowNaStrumien])

        return out