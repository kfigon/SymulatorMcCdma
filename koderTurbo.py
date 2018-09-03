from przeplot import Przeplatacz
from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow
from utils import flat

class KoderTurbo:
    def __init__(self, rejestr1, rejestr2, przeplatacz = Przeplatacz()):
        if rejestr1.getIleBitowWyjsciowych() != 2 or rejestr2.getIleBitowWyjsciowych() != 2:
            raise Exception('rejestry kodera turbo musza miec 2 gazie do odczepow!')

        self.__rej1 = rejestr1
        self.__rej2 = rejestr2
        self.__przeplatacz = przeplatacz

    def __koduj(self, rejestr, dane):
        rejestr.reset()
        for b in dane:
            wynik = rejestr.licz()
            wejscie = b ^ wynik[0]
            rejestr.shift(wejscie)

            yield wynik[1]

    def koduj(self, dane):
        # todo: uncomment termination, fix test
        out1 = list(self.__koduj(self.__rej1, dane))# + self.__rej1.terminate()
        # terminacja tylko pierwszego? literatura tak sugeruje
        przeplecione = self.__przeplatacz.przeplot(dane)
        out2 = list(self.__koduj(self.__rej2, przeplecione)) #+ self.__rej2.terminate()

        return [dane, out1, out2]
        
    @staticmethod
    def combine(tab1, tab2):
        if len(tab1) != len(tab2):
            raise Exception("kombinator musi dostac rowne tablice")

        out = []
        for a,b in zip(tab1, tab2):
            out.append(a)
            out.append(b)
        return out
    
    def dekoduj(self, dane):
        pass

