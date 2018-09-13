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

    def testMetryk(self):
        odebrane = [[0.3,0.1],[-0.5,0.2],[0.8,0.5],[-0.5,0.3],[0.1,-0.7],[1.5,-0.4]]
        (alfy, bety, gammy) = self.m.liczMetryki(odebrane)

        self.assertAlmostEqual(0.37, gammy[0][0][0],2)
        self.assertAlmostEqual(25.79, gammy[2][1][0],2)
        self.assertAlmostEqual(4.48, gammy[4][0][0],2)
        self.assertAlmostEqual(15.64, gammy[5][1][0],2)

        self.assertAlmostEqual(1, alfy[0][0],2)
        self.assertAlmostEqual(0.105, alfy[3][1],2)
        self.assertAlmostEqual(0.45, alfy[3][3],2)

        self.assertAlmostEqual(1, bety[6][0],2)
        self.assertAlmostEqual(0.98, bety[4][2],2)
        self.assertAlmostEqual(0.67, bety[2][1],2)

    @unittest.skip # zaokraglenia i bug (?) z poczatkiem i koncem metryk
    def testPrawodopodobienstw(self):
        odebrane = [[0.3,0.1],[-0.5,0.2],[0.8,0.5],[-0.5,0.3],[0.1,-0.7],[1.5,-0.4]]
        (alfy, bety, gammy) = self.m.liczMetryki(odebrane)

        out = []
        out.append(self.m.liczPrawdopodobienstwa(odebrane[0], 0, alfy, bety, gammy, [0]))
        out.append(self.m.liczPrawdopodobienstwa(odebrane[0], 0, alfy, bety, gammy, [1]))

        out.append(self.m.liczPrawdopodobienstwa(odebrane[1], 1, alfy, bety, gammy, [0]))
        out.append(self.m.liczPrawdopodobienstwa(odebrane[1], 1, alfy, bety, gammy, [1]))
        
        out.append(self.m.liczPrawdopodobienstwa(odebrane[2], 2, alfy, bety, gammy, [0]))
        out.append(self.m.liczPrawdopodobienstwa(odebrane[2], 2, alfy, bety, gammy, [1]))
        
        out.append(self.m.liczPrawdopodobienstwa(odebrane[3], 3, alfy, bety, gammy, [0]))
        out.append(self.m.liczPrawdopodobienstwa(odebrane[3], 3, alfy, bety, gammy, [1]))
        
        exp = [0.203, 1.214, 0.139, 0.177, 0.493, 0.068, 0.0, 0.306]
        self.assertEqual(exp, out)

    def testE2E(self):
        odebrane = [[0.3,0.1],[-0.5,0.2],[0.8,0.5],[-0.5,0.3],[0.1,-0.7],[1.5,-0.4]]
        res = self.m.dekoduj(odebrane)
        self.assertEqual([1,1,0,1,0,0], self.m.proguj(res))

if __name__ == '__main__':
    unittest.main()