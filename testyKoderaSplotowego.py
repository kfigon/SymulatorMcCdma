import unittest
from rejestrPrzesuwny import RejestrPrzesuwny
from koderSplotowy import KoderSplotowy
from utils import generujDaneBinarne

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

class TestyDekodowania(unittest.TestCase):
    def setUp(self):
        odczepy = [[0,1,2], [0,2]]
        r = RejestrPrzesuwny(3, odczepy)
        self.k = KoderSplotowy(r,1)

    def testBezBledu(self):
        nadany = [1, 0, 1, 1, 0, 0]
        expZakodowany = [1,1, 1,0, 0,0, 0,1, 0,1, 1,1]
        self.fullSprawdzenie(nadany, expZakodowany)

    def testZBledem(self):
        nadany = [1,0,1,1,0,0]
        expZakodowany = [1,1, 1,0, 0,0, 0,1, 0,1, 1,1]
        otrzymany =     [1,1, 1,0, 1,0, 0,1, 0,1, 0,1]
        zakodowany = self.k.koduj(nadany)
        self.assertEqual(expZakodowany, zakodowany, 'blad zakodowanych')
        self.assertEqual(nadany, self.k.dekoduj(otrzymany), 'blad dekodowania')

    def fullSprawdzenie(self, nadany, expZakodowany):
        zakodowany = self.k.koduj(nadany)
        self.assertEqual(expZakodowany, zakodowany, 'blad zakodowanych')
        self.assertEqual(nadany, self.k.dekoduj(zakodowany), 'blad dekodowania')

    def test1Bit(self):
        nadany=[1]
        expZakodowany=[1,1]
        self.fullSprawdzenie(nadany, expZakodowany)

    def test2Bity(self):
        nadany=[1,0]
        expZakodowany=[1,1,1,0]
        self.fullSprawdzenie(nadany, expZakodowany)

    def test3Bity(self):
        nadany=[1,0,0]
        expZakodowany = [1, 1, 1, 0, 1, 1]
        self.fullSprawdzenie(nadany, expZakodowany)

    def test3Bity2(self):
        nadany=[1,0,1]
        expZakodowany=[1,1,1,0,0,0]
        self.fullSprawdzenie(nadany, expZakodowany)

    def test10Bitow(self):
        nadany=[0,1,1,0,1,0,1,0,1,1]
        expZakodowany=[0,0, 1,1, 0,1, 0,1, 0,0, 1,0, 0,0, 1,0, 0,0, 0,1]
        self.fullSprawdzenie(nadany, expZakodowany)

# poprawic dane
@unittest.SkipTest
class StresTestKodera(unittest.TestCase):
    def setUp(self):
        odczepy = [[1,4,6,8],
                   [0,2,4],
                   [2,3,5,7],
                   [1,5,6,8]]
        r = RejestrPrzesuwny(9, odczepy)
        self.k = KoderSplotowy(r,3)

    def test1(self):
        wejscie=[1,1,1, 0,0,1, 0,1,1, 1,0,1]
        zakodowany = self.k.koduj(wejscie)
        zdekodowane = self.k.dekoduj(zakodowany)
        self.assertEqual(wejscie, zdekodowane)

    def testStres(self):
        dane = generujDaneBinarne(33)
        zakodowany = self.k.koduj(dane)
        zdekodowane = self.k.dekoduj(zakodowany)
        self.assertEqual(dane, zdekodowane)

if __name__ == '__main__':
    unittest.main()
