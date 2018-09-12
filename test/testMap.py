import unittest
from map import MapAlgorithm, liczL, decyzja, gamma, alfa, normujAlfa
from maszynaStanow import MaszynaStanow
from rejestrPrzesuwny import RejestrPrzesuwny

class TestMatematykiMap(unittest.TestCase):
    def testL(self):
        x = liczL(1/2, 1/2)
        self.assertEqual(0, x)

    def testDecyzji(self):
        self.assertEqual(1, decyzja(0))
        self.assertEqual(-1, decyzja(-1))
        self.assertEqual(1, decyzja(12))

    def testGamma(self):
        odebrane=[0.3, 0.1]
        Lc = 5
        Luk = 0
        uk = 123 # any, since Luk=0
        zakodowane = [-1,-1]
        g = gamma(odebrane, zakodowane, uk, Luk, Lc)

        self.assertAlmostEqual(0.3678, g, 3)

    def testAlfa(self):
        a=[1,2,3,4]
        g=[2,2,3,5]
        wynik = alfa(a,g)
        self.assertEqual(35, wynik)
    
    def testNormowaniaAlfa(self):
        a=50
        alfy=[1,2,3,4]
        self.assertEqual(5.0, normujAlfa(a, alfy))

class TestMap(unittest.TestCase):
    def setUp(self):
        odczepy = [[0,1,2],[0,2]]
        rej = RejestrPrzesuwny(3, odczepy)
        maszyna = MaszynaStanow(rej, 1)
        self.m = MapAlgorithm(maszyna)

    def test(self):
        odebrane = [[0.3,0.1],[-0.5,0.2],[0.8,0.5],[-0.5,0.3],[0.1,-0.7],[1.5,-0.4]]
        wynik = self.m.licz(odebrane)
        self.assertEqual([], wynik)
        
if __name__ == '__main__':
    unittest.main()