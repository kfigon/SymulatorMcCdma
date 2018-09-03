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

        res = KoderTurbo.combine(tab1, tab2)
        exp = [1,4,2,5,3,6]
        self.assertEqual(exp, res)

    def testCombineNotEven(self):
        tab1=[1,2,3]
        tab2=[4,5,6,3]
        self.assertRaises(Exception, KoderTurbo.combine, tab1, tab2)

    def testEndToEnd(self):
        indata = [1,1,0,0,1]

        [d, c1, c2] = self.k.koduj(indata)
        self.fail("todo")

if __name__ =='__main__':
    unittest.main()