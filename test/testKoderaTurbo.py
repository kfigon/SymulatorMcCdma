import unittest
from koderTurbo import KoderTurbo
from przeplot import Przeplatacz
from rejestrPrzesuwny import RejestrPrzesuwny

class TestKoderaTurbo(unittest.TestCase):
    def setUp(self):
        r1 = RejestrPrzesuwny(4, [[0,2,3], [0,1]])
        r2 = RejestrPrzesuwny(4, [[0,2,3], [0,1]])
        self.k = KoderTurbo(rejestr1 = r1, 
                            rejestr2 = r2,
                            przeplatacz=Przeplatacz())
    
    def test(self):
        indata = [1,0,1,0,1,1,0,0,1]

        [d, c1, c2] = self.k.koduj(indata)
        self.assertEqual(indata, d)
        self.fail("todo")

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
            

if __name__ =='__main__':
    unittest.main()