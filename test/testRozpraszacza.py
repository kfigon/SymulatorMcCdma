import unittest
from rozpraszaczWidma import RozpraszaczWidma, RozpraszaczBipolarny, IterateHelper


class TestRozpraszacza(unittest.TestCase):
    def testOk(self):
        r = RozpraszaczWidma(3) #3 chipy na bit
        bity = [1,0,0,1]
        ciagRozpraszajacy = [1,1,1,0,0,1,0,0,1,0,0,0]
        exp=[0,0,0, 0,0,1, 0,0,1, 1,1,1]
        self.assertEqual(exp, list(r.rozpraszaj(bity, ciagRozpraszajacy)))

    def testKrotszeDane(self):
        r = RozpraszaczWidma(3)
        bity = [1,0]
        ciagRozpraszajacy = [1,1,1,0,0,1,0,0,1,0,0]
        exp = [0,0,0, 0,0,1]
        self.assertEqual(exp, list(r.rozpraszaj(bity, ciagRozpraszajacy)))

    def testDluzszeDane(self):
        r = RozpraszaczWidma(3)
        bity = [1,0,1]
        ciagRozpraszajacy = [1,1,1,0,0,1]
        exp = [0,0,0, 0,0,1, 0,0,0]
        self.assertEqual(exp, list(r.rozpraszaj(bity, ciagRozpraszajacy)))
    
    def testNotAligned(self):
        r = RozpraszaczWidma(3)
        bity = [1,0,1]
        ciagRozpraszajacy = [1,1,1,0,0,1,0]
        exp = [0,0,0, 0,0,1, 1,0,0]
        self.assertEqual(exp, list(r.rozpraszaj(bity, ciagRozpraszajacy)))

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

if __name__ == '__main__':
    unittest.main()