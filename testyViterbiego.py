import unittest
from maszynaStanow import MaszynaStanow
from rejestrPrzesuwny import RejestrPrzesuwny
from viterbi import Viterbi
from viterbi import Sciezka

class TestyViterbiego(unittest.TestCase):
    def setUp(self):
        odczepy = [[0, 1, 2], [0, 2]]
        r = RejestrPrzesuwny(3, odczepy)
        m = MaszynaStanow(r, 1)
        self.v = Viterbi(m)

    def sprawdzStanSciezki(self, sciezka, expInState, expOutState, expHamming):
        stan = sciezka.getOstatniStan()
        self.assertEqual(expInState, stan['inState'], 'blad! Stan wejsciowy')
        self.assertEqual(expOutState, stan['outState'], 'blad! Stan wyjsciowy')
        self.assertEqual(expHamming, sciezka.getZakumulowanyHamming(), 'blad! hamming')

    def testSciezkiDochodzaceDoStanu_2Krok_00(self):
        self.v.liczPierwszy([1, 1])
        sciezki = self.v.getSciezkiDochodzaceDoStanu('00')

        self.assertEqual(1, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '00', 2)

    def testSciezkiDochodzaceDoStanu_2Krok_01(self):
        self.v.liczPierwszy([1, 1])
        sciezki = self.v.getSciezkiDochodzaceDoStanu('01')
        self.assertEqual(1, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '10', 0)

    def testSciezkiDochodzaceDoStanu_2Krok_10(self):
        self.v.liczPierwszy([1, 1])
        sciezki = self.v.getSciezkiDochodzaceDoStanu('10')
        self.assertEqual(1, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '00', 2)

    def testSciezkiDochodzaceDoStanu_2Krok_11(self):
        self.v.liczPierwszy([1, 1])
        sciezki = self.v.getSciezkiDochodzaceDoStanu('11')
        self.assertEqual(1, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '10', 0)

if __name__ == '__main__':
    unittest.main()
