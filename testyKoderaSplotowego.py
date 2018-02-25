import unittest
from rejestrPrzesuwny import RejestrPrzesuwny
from koderSplotowy import KoderSplotowy
from koderSplotowy import odlegloscHamminga
from koderSplotowy import podziel

class TestKoderaSplotowego(unittest.TestCase):
    def setUp(self):
        odczepy = [[1,4,6,8],
                   [0,2,4],
                   [2,3,5,7],
                   [1,5,6,8]]
        r = RejestrPrzesuwny(9, odczepy)
        self.k = KoderSplotowy(r,3)

    def test1(self):
        wejscie=[1,1,1, 0,0,1, 0,1,1, 1,0,1]
        exp=[1,0,1,1,  1,0,1,1,  1,1,1,0,  0,1,0,0]
        self.assertEqual(exp, self.k.koduj(wejscie))

    def test2(self):
        self.assertEqual([1,0,1,1], self.k.koduj([1,1,1]))

    def testHamminga(self):
        self.assertEqual(0, odlegloscHamminga([1,1,1,0],[1,1,1,0]))
        self.assertEqual(1, odlegloscHamminga([1,1,1,0],[1,1,1,1]))                        
        self.assertEqual(2, odlegloscHamminga([1,0,1,0],[0,1,1,0]))

    def testDzielenia1(self):
        wej = [1,0, 1,0, 1,1, 0,0]
        exp = [[1,0],[1,0],[1,1],[0,0]]
        self.assertEqual(exp, podziel(wej,2))

    def testDzielenia2(self):
        wej = [1,0, 1,0, 1,1, 0,0,1]
        exp = [[1,0,1], [0,1,1], [0,0,1]]
        self.assertEqual(exp, podziel(wej,3))

class TestViterbiego(unittest.TestCase):
    def setUp(self):
        odczepy = [[0,1,2], [0,2]]
        r = RejestrPrzesuwny(3, odczepy)
        self.k = KoderSplotowy(r,1)

    def testBezBledu(self):
        nadany = [1, 0, 1, 1, 0, 0]
        expZakodowany = [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1]
        zakodowany = self.k.koduj(nadany)
        self.assertEqual(expZakodowany, zakodowany)
        self.assertEqual(nadany, self.k.dekoduj(zakodowany))

    def testZBledem(self):
        expNadany = [1,0,1,1,0,0]
        otrzymany = [1,0, 1,0, 0,0, 0,0, 0,1, 1,1]
        self.assertEqual(expNadany, self.k.dekoduj(otrzymany))

if __name__ == '__main__':
    unittest.main()
