import unittest
from rejestrPrzesuwny import RejestrPrzesuwny
from koderSplotowy import KoderSplotowy
from koderSplotowy import odlegloscHamminga
from koderSplotowy import podziel
from koderSplotowy import Sciezka

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
        self.assertEqual(expZakodowany, zakodowany, "kodowanie sie nie udalo")
        self.assertEqual(nadany, self.k.dekoduj(zakodowany), "dekodowanie sie nie udalo")

    def testZBledem(self):
        expNadany = [1,0,1,1,0,0]
        otrzymany = [1,0, 1,0, 0,0, 0,0, 0,1, 1,1]
        self.assertEqual(expNadany, self.k.dekoduj(otrzymany))

    def test1Bit(self):
        nadany=[1]
        expZakodowany=[1,1]
        zakodowany = self.k.koduj(nadany)
        self.assertEqual(expZakodowany, zakodowany)
        self.assertEqual(nadany, self.k.dekoduj(zakodowany))

    def test2Bity(self):
        nadany=[1,0]
        expZakodowany=[1,1,1,0]
        zakodowany = self.k.koduj(nadany)
        self.assertEqual(expZakodowany, zakodowany)
        self.assertEqual(nadany, self.k.dekoduj(zakodowany))

class TestySciezki(unittest.TestCase):
    def setUp(self):
        odczepy = [[0,1,2], [0,2]]
        ileBitowNaRaz= 3
        r = RejestrPrzesuwny(ileBitowNaRaz, odczepy)
        m = MaszynaStanow(r, ileBitowNaRaz)
        self.sciezka = Sciezka(m)

    def przygotujStan(self, inBit, inState, outBits, outState):
        return {'in':inBit, 'out':outBits, 'inState':inState, 'outState':outState}

    # outState w s to nie to samo co stan tutaj!!!
    # false/true?
    def testDojscie1(self):
        s = self.przygotujStan('00', [1], [1,1], '10')
        self.sciezka.dodajStan(s, 0)
        self.assertTrue(self.sciezka.czyJestDojscie('01'))
    
if __name__ == '__main__':
    unittest.main()
