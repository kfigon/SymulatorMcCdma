from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow
from utils import podziel
from utils import odlegloscHamminga

class KoderSplotowy:
    def __init__(self, rejestrPrzesuwny, ileBitowNaRaz):
        self.__rejestr = rejestrPrzesuwny
        self.__ileBitowNaRaz = ileBitowNaRaz

    def koduj(self, daneBinarne):
        assert(len(daneBinarne) % self.__ileBitowNaRaz == 0)

        dl = self.__rejestr.getIleBitowWyjsciowych()*len(daneBinarne)//self.__ileBitowNaRaz
        out = [0]*dl
        krok = self.__ileBitowNaRaz
        idxOut=0
        for i in range(0, len(daneBinarne), krok):
            podCiag = daneBinarne[i:i+krok]
            # wchodza wszystkie na raz!
            for obrot in reversed(range(krok)):
                b = podCiag[obrot]
                self.__rejestr.shift(b)
            wynikObrotu = self.__rejestr.licz()

            for b in wynikObrotu:
                out[idxOut] = b
                idxOut += 1
        return out

    def getNKM(self):
        return (self.__rejestr.getIleBitowWyjsciowych(),
                self.__ileBitowNaRaz, self.__rejestr.getDlugoscRejestru())

    def reset(self):
        self.__rejestr.reset()

    def dekoduj(self, daneBinarne):
        pass
        # self.reset()
        # m = MaszynaStanow(self.__rejestr, self.__ileBitowNaRaz)
        # podzielone = podziel(daneBinarne, self.__rejestr.getIleBitowWyjsciowych())
        #
        # sciezki = []
        # for i, porcja in enumerate(podzielone):
        #     if(i == 0):
        #         pocz = m.getStanPoczatkowy()
        #         mozliweStany = m.getMozliwePrzejscia(pocz)
        #         for s in mozliweStany:
        #             sciezka = Sciezka()
        #             sciezka.dodajStan(s, odlegloscHamminga(porcja, s[MaszynaStanow.OUT]))
        #             sciezki.append(sciezka)
        #     else:
        #         doDodania =[]
        #         wszystkieStany = m.getListaStanow()
        #         for potencjalnyKolejnyStan in wszystkieStany:
        #             for sciezka in sciezki:
        #                 s = sciezka.getOstatniStan()[MaszynaStanow.OUT_STATE]
        #                 if (m.czyPolaczone(s, potencjalnyKolejnyStan)):
        #                     # dodac stan do sciezki - trzeba wydlubac obiekt
        #                     kolejnyKrokSciezki = m.getStan(s, potencjalnyKolejnyStan)
        #                     hamming = odlegloscHamminga(kolejnyKrokSciezki[MaszynaStanow.OUT], porcja)
        #                     ob = {'sciezka': sciezka, 'krok':kolejnyKrokSciezki, 'hamming': hamming}
        #                     doDodania.append(ob)
        #
        #         self.__usunKonflikty(doDodania)
        #
        #         juzRozszerzoneSciezki=[]
        #         for el in doDodania:
        #             sciezka = el['sciezka']
        #             if(sciezka in juzRozszerzoneSciezki):
        #                 nowa = sciezka.kopiujSciezke()
        #                 nowa.dodajStan(el['krok'], el['hamming'])
        #                 sciezki.append(nowa)
        #             else:
        #                 sciezka.dodajStan(el['krok'], el['hamming'])
        #                 juzRozszerzoneSciezki.append(sciezka)
        #
        # # sciezki ktore zostaly usuniete w ostatniej iteracji
        # for s in sciezki:
        #     if(s.getDlugoscSciezki() != len(podzielone)):
        #         sciezki.remove(s)
        #
        # return self.__traceBackNajlepszejSciezki(sciezki)

    # def __usunKonflikty(self, lista):
    #     for pierwszy in lista:
    #         for drugi in lista:
    #             outSt1 = pierwszy['krok'][MaszynaStanow.OUT_STATE]
    #             outSt2 = drugi['krok'][MaszynaStanow.OUT_STATE]
    #             ham1 = pierwszy['hamming'] + pierwszy['sciezka'].getZakumulowanyHamming()
    #             ham2 = drugi['hamming'] + drugi['sciezka'].getZakumulowanyHamming()
    #
    #             if (drugi != pierwszy and outSt1 == outSt2 and ham1 > ham2):
    #                 lista.remove(pierwszy)
    #
    #
    # def __traceBackNajlepszejSciezki(self, sciezki):
    #     najlepszaSciezka = sciezki[0]
    #     for s in sciezki:
    #         if(s.getZakumulowanyHamming() < najlepszaSciezka.getZakumulowanyHamming()):
    #             najlepszaSciezka = s
    #
    #     return najlepszaSciezka.traceBack()


