import unittest
from map import MapAlgorithm, liczL, decyzja
from maszynaStanow import MaszynaStanow
from rejestrPrzesuwny import RejestrPrzesuwny

class Test(unittest.TestCase):
    def setUp(self):
        odczepy = [[0,1,2],[0,2]]
        rej = RejestrPrzesuwny(3, odczepy)
        maszyna = MaszynaStanow(rej, 1)
        self.m = MapAlgorithm(maszyna)

    def testL(self):
        x = liczL(1/2, 1/2)
        self.assertEqual(0, x)

    def testDecyzji(self):
        self.assertEqual(1, decyzja(0))
        self.assertEqual(-1, decyzja(-1))
        self.assertEqual(1, decyzja(12))

    def testGamma(self):
        stan='00'
        odebranaDana=0.3
        odebranaParzystosc=0.1

        g = self.m.gamma(stan, odebranaDana, odebranaParzystosc)
        self.assertAlmostEqual(0.368, g[0], 3)
        self.assertAlmostEqual(2.718, g[1], 3)
        
if __name__ == '__main__':
    unittest.main()