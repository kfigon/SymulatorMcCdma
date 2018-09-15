import unittest
from map import MapAlgorithm, gamma, alfa, normujAlfa, mapujP
from maszynaStanow import MaszynaStanow
from rejestrPrzesuwny import RejestrPrzesuwny

class TestMatematykiMap(unittest.TestCase):
  
    def testGamma(self):
        odebrane=[0.3, 0.1]
        Lc = 5
        Luk = 0
        zakodowane = [-1,-1]
        g = gamma(odebrane, zakodowane, Luk, Lc)

        self.assertAlmostEqual(0.3678, g, 3)

    def testGammaZApriori(self):
        odebrane=[0.3, 0.1]
        zakodowane = [-1, 1]
        Luk = -0.13
        Lc= 5
        result = gamma(odebrane, zakodowane, Luk, Lc)
        
        self.assertAlmostEqual(0.647, result, 3)

    def testAlfa(self):
        a=[1,2,3,4]
        g=[2,2,3,5]
        wynik = alfa(a,g)
        self.assertEqual(35, wynik)
    
    def testNormowaniaAlfa(self):
        a=50
        alfy=[1,2,3,4]
        self.assertEqual(5.0, normujAlfa(a, alfy))

    def testMapowaniaPrawodpodobienstwa(self):
        data = [
            # p0, p1, exp
            (1,2,0.693),
            (2,3,0.405),
            (0, 123, 10),
            (123, 0, -10)
            ]
        for d in data:
            nazwa = "ln{}/{} = {}".format(str(d[0]),str(d[1]),str(d[2]))
            with self.subTest(name=nazwa):
                p = [d[0], d[1]]
                result = mapujP(p)
                self.assertAlmostEqual(d[2], result, 2)

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

    # @unittest.skip # zaokraglenia i bug (?) z poczatkiem i koncem metryk
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
        
        # exp = [0.203, 1.214, 0.139, 0.177, 0.493, 0.068, 0.0, 0.306]
        exp = [0.02878,
                0.1699,
                0.1400,
                0.1776,
                0.4946,
                0.0691,
                0.0012,
                0.3074]
        self.assertEqual(len(exp), len(out))
        for e, o in zip(exp, out):
            self.assertAlmostEqual(e, o, 2)

    def testE2E(self):
        odebrane = [[0.3,0.1],[-0.5,0.2],[0.8,0.5],[-0.5,0.3],[0.1,-0.7],[1.5,-0.4]]
        res = self.m.dekoduj(odebrane)
        self.assertEqual([1,1,0,1,0,0], self.m.proguj(res))

if __name__ == '__main__':
    unittest.main()