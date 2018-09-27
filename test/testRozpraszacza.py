import unittest
from rozpraszaczWidma import RozpraszaczBipolarny, IterateHelper


class TestRozpraszaczaBipolarnego(unittest.TestCase):
    def setUp(self):
        self.r = RozpraszaczBipolarny()

    def testRozpraszaniaBipolarnego(self):
        probki = [complex(-1, 1),complex(-1, 1),complex(-1, 1)]
        ciag =   [        -1,-1,       -1,-1,            1,-1]

        wynik = self.r.rozpraszajBipolarne(probki, ciag)
        exp = [complex(1,-1),complex(1,-1),complex(-1,-1)]
        self.assertEqual(exp, wynik)

    def testNotAligned(self):
        probki = [complex(-1, 1),complex(-1,1),complex(-1,1)]
        ciag =   [-1,-1, 1]

        wynik = self.r.rozpraszajBipolarne(probki, ciag)
        exp = [complex(1,-1),complex(-1,-1),complex(1,1)]
        self.assertEqual(exp, wynik)

    def testNotAligned2(self):
        probki = [complex(-1, 1),complex(-1, 1),  complex(-1,1) ,complex(1,-1),  
                complex(-1,-1)]
        ciag =   [-1,-1, 1,-1]

        wynik = self.r.rozpraszajBipolarne(probki, ciag)
        exp = [complex(1,-1),complex(-1,-1),complex(1,-1),complex(1,1),complex(1,1)]
        self.assertEqual(exp, wynik)

    def testSingleChip(self):
        probki = [complex(-1, 1),complex(-1,1),complex(-1,1)]
        ciag =   [-1]

        wynik = self.r.rozpraszajBipolarne(probki, ciag)
        exp = [complex(1,-1),complex(1,-1),complex(1,-1)]
        self.assertEqual(exp, wynik)

    def testSkupianieSingleChip(self):
        probki = [complex(-1, 1),complex(-1,1),complex(-1,1)]
        ciag =   [-1]

        wynik = self.r.skupBipolarne(probki, ciag)
        exp = [complex(1,-1),complex(1,-1),complex(1,-1)]
        self.assertEqual(exp, wynik)

    def testE2E(self):
        probki = [complex(-1, 1),complex(-1,1),complex(-1,1)]
        ciag =   [-1]
        rozproszone = self.r.rozpraszajBipolarne(probki, ciag)
        
        wynik = self.r.skupBipolarne(rozproszone, ciag)
        self.assertEqual(probki, wynik)


class TestIterateHelper(unittest.TestCase):
    def test1(self):
        it = IterateHelper(3)
        self.assertEqual(0, it.get())
        self.assertEqual(1, it.get())
        self.assertEqual(2, it.get())

        self.assertEqual(0, it.get())
        self.assertEqual(1, it.get())
        self.assertEqual(2, it.get())

        self.assertEqual(0, it.get())
        self.assertEqual(1, it.get())
        self.assertEqual(2, it.get())

if __name__ == '__main__':
    unittest.main()