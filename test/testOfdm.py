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
        self.assertEqual(dane, zdemodulowane)
    
    def testE2E_jedenStrumienBps(self):
        dane = [complex(1,0), complex(-1,0), complex(1,0), complex(-1,0), complex(-1,0)]
        tr = TransmiterOfdm(10)
        zmodulowane = tr.modulujStrumien(dane)

        zdemodulowane = tr.demoduluj(zmodulowane)
        self.assertEqual(dane, zdemodulowane)
if __name__ == '__main__':
    unittest.main()