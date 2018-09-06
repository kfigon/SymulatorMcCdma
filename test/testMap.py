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

    def testGamma0(self):
        stan='00'
        stanKoncowy = '00'
        odebranaDana=0.3
        odebranaParzystosc=0.1

        g = self.m.gamma(stan, stanKoncowy, odebranaDana, odebranaParzystosc)
        self.assertAlmostEqual(0.368, g, 3)
    
    def testGamma1(self):
        stan='00'
        stanKoncowy = '10'
        odebranaDana=0.3
        odebranaParzystosc=0.1

        g = self.m.gamma(stan, stanKoncowy, odebranaDana, odebranaParzystosc)
        self.assertAlmostEqual(2.718, g, 3)

    def testAlfa(self):
        gamma1 = 0.5
        poprzednieAlfa1 = 0.4
        gamma2 = 0.1
        poprzednieAlfa2 = 0.2

        exp = 0.22
        self.assertAlmostEqual(exp, self.m.alfa(poprzednieAlfa1, gamma1, poprzednieAlfa2, gamma2))
    def testBeta(self):
        gamma1 = 0.5
        beta1 = 0.4
        gamma2 = 0.1
        beta2 = 0.2

        exp = 0.22
        self.assertAlmostEqual(exp, self.m.beta(beta1, gamma1, beta2, gamma2))

if __name__ == '__main__':
    unittest.main()