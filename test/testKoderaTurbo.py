import unittest
from koderTurbo import KoderTurbo
from przeplot import Przeplatacz
from rejestrPrzesuwny import RejestrPrzesuwny

class TestKoderaTurbo(unittest.TestCase):
    def setUp(self):
        # jakby o jeden mniej niz w matlabie
        r1 = RejestrPrzesuwny(3, [[1,2], [0,2]])
        r2 = RejestrPrzesuwny(3, [[1,2], [0,2]])
        self.k = KoderTurbo(rejestr1 = r1, 
                            rejestr2 = r2,
                            przeplatacz=Przeplatacz())
    
    def test(self):
        # od skrajnego po lewej
        indata = [1,1,0,0,1]

        [d, c1, c2] = self.k.koduj(indata)
        self.assertEqual(indata, d)
        expC = [0,1,1,0,1]
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

    def testDecombine1(self):
        tab = [1,2,3,4,5,6]
        self.assertEqual([[1,2],[4,5]], KoderTurbo.decombine(tab,1))

    def testDecombine2(self):
        tab = [1,2,3,4,5,6]
        self.assertEqual([[1,3],[4,6]], KoderTurbo.decombine(tab,2))

    def testEndToEnd(self):
        # dane musza byc terminowane!
        indata = [1,1,0,0,0,0,0,0]
        zakodowane = self.k.koduj(indata)
        zakodowane = KoderTurbo.combine(zakodowane[0], zakodowane[1], zakodowane[2])
        zdekodowane = self.k.dekoduj(zakodowane)

        self.assertEqual(indata, zdekodowane)

if __name__ =='__main__':
    unittest.main()