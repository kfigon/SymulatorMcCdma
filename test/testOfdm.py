import unittest
from transmiterOfdm import addPadding,TransmiterOfdm


class TestOfdm(unittest.TestCase):

    def testPaddinguBasic(self):
        dane = [1,2,3,4]
        dopelnienie = 2

        wynik = addPadding(dane, dopelnienie)
        exp = [0,1,2,3,4,0,0,0]
        self.assertEqual(exp, wynik)
        self.assertEqual([1,2,3,4], dane) # stare dane niezmienne

    def testPaddinguComplex(self):
        dane = [complex(1,0),
                complex(1,1),
                complex(1,-1)]
        dopelnienie = 2
        wynik = addPadding(dane, dopelnienie)

        exp = [0,complex(1,0), complex(1,1), complex(1,-1), 0, 0]
        self.assertEqual(exp, wynik)
        self.assertEqual([complex(1,0),complex(1,1), complex(1,-1)], dane)


    def testE2E_jedenStrumienQpsk(self):
        dane = [complex(1,1), complex(-1,1), complex(1,-1), complex(-1,-1), complex(-1,1)]
        tr = TransmiterOfdm(10)
        zmodulowane = tr.modulujStrumien(dane)

        zdemodulowane = tr.demoduluj(zmodulowane)
        # todo: moze to przycyzna bledow?
        # expected = [i*50 for i in dane] # aplituda jest zmieniona, trzeba pomnozyc razy dlugosc i ilosc strumieni
        self.__testujComplexArray(dane, zdemodulowane)
    
    def testE2E_jedenStrumienBpsk(self):
        dane = [complex(1,0), complex(-1,0), complex(1,0), complex(-1,0), complex(-1,0)]
        tr = TransmiterOfdm(10)
        zmodulowane = tr.modulujStrumien(dane)

        zdemodulowane = tr.demoduluj(zmodulowane)
        # todo: moze to przycyzna bledow?
        #expected = [i*50 for i in dane] # aplituda jest zmieniona, trzeba pomnozyc razy dlugosc i ilosc strumieni
        self.__testujComplexArray(dane, zdemodulowane)

    def __testujComplexArray(self, first, second):
        self.assertEqual(len(first), len(second))
        for f,s in zip(first, second):
            self.assertAlmostEqual(f.real, s.real, places=3)
            self.assertAlmostEqual(f.imag, s.imag, places=3)

if __name__ == '__main__':
    unittest.main()