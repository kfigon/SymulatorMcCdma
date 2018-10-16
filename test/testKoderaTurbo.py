import unittest
from koderTurbo import KoderTurbo
from przeplot import Przeplatacz
from rejestrPrzesuwny import RejestrSystematyczny, RejestrPrzesuwny
import random

class TestKoderaTurbo(unittest.TestCase):
    def setUp(self):
        r1 = RejestrSystematyczny(3, [[0,2]], [1,2])
        r2 = RejestrSystematyczny(3, [[0,2]], [1,2])
        self.k = KoderTurbo(rejestr1 = r1, 
                            rejestr2 = r2,
                            przeplatacz=Przeplatacz())
    
    def test(self):
        # od skrajnego po lewej
        indata = [1,1,0,0,1]

        [d, c1, c2] = self.k.koduj(indata)
        self.assertEqual(indata, d)
        expC = [1,0,0,1,0]
        # to samo bo przeplot przezroczysty
        self.assertEqual(expC, c1, "pierwszy koder zle!")
        self.assertEqual(expC, c2, "koder po przeplocie zle!")


    def testCombine(self):
        tab1=[1,2,3]
        tab2=[4,5,6]
        tab3 = [7,8,9]
        res = KoderTurbo.combine(tab1, tab2, tab3)
        exp = [1,4,7,2,5,8,3,6,9]
        self.assertEqual(exp, res)

    def testCombineNotEven(self):
        tab1=[1,2,3]
        tab2=[4,5,6,3]
        tab3=[1,2,3]
        self.assertRaises(Exception, KoderTurbo.combine, tab1, tab2, tab3)

    def testDecombine(self):
        tab = [1,4,7,2,5,8,3,6,9]

        [a,b,c] = KoderTurbo.decombine(tab)
        self.assertEqual([1,2,3],a)
        self.assertEqual([4,5,6],b)
        self.assertEqual([7,8,9],c)

    def testCombDecomb(self):
        combined = KoderTurbo.combine([1,2,3],[4,5,6],[7,8,9])
        res = KoderTurbo.decombine(combined)
        self.assertEqual([1,2,3],res[0])
        self.assertEqual([4,5,6],res[1])
        self.assertEqual([7,8,9],res[2])

    def testEndToEndSame0(self):
        indata = [0 for _ in range(20)]
        self.end2end(indata)

    def end2end(self, indata):
        zakodowane = self.k.koduj(indata)
        zakodowane = KoderTurbo.combine(zakodowane[0], zakodowane[1], zakodowane[2])

        zdekodowane = self.k.dekoduj(zakodowane, ileItracji=20)

        self.assertEqual(indata, zdekodowane)

    def testEndToEndSame1(self):
        # dane musza byc terminowane!
        indata = [1 for _ in range(20)]
        for _ in range(5):
            indata.append(0)
        self.end2end(indata)

    def testEndToEnd(self):
        indata = [1,0,1,1,0,0,1,0,0,0,0,0]
        self.end2end(indata)

class TestDekoderaTurboZPrzeplotem(unittest.TestCase):
    def setUp(self):
        r1 = RejestrPrzesuwny(3, [[1,2], [0,2]])
        r2 = RejestrPrzesuwny(3, [[1,2], [0,2]])
        self.k = KoderTurbo(rejestr1 = r1, 
                            rejestr2 = r2,
                            przeplatacz=Przeplatacz(3))
    def testEndToEnd(self):
        # dane musza byc terminowane!
        indata = [1,1,0,1,1,1,0,0,0,0,0,0]
        self.end2end(indata)
        
    def end2end(self, indata):
        zakodowane = self.k.koduj(indata)
        zakodowane = KoderTurbo.combine(zakodowane[0], zakodowane[1], zakodowane[2])
        
        zdekodowane = self.k.dekoduj(zakodowane, ileItracji=5)

        self.assertEqual(indata, zdekodowane)

    def testStres(self):
        indata = [random.randint(0,1) for _ in range(995)]
        for _ in range(5):
            indata.append(0)
        zakodowane = self.k.koduj(indata)
        zakodowane = KoderTurbo.combine(zakodowane[0], zakodowane[1], zakodowane[2])
        zdekodowane = self.k.dekoduj(zakodowane, ileItracji=5)

        self.assertEqual(indata, zdekodowane)

if __name__ =='__main__':
    unittest.main()