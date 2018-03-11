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

    def testPierwszyKrok(self):
        sciezki = self.v.liczPierwszy([1,1])

        self.assertEqual(2, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '00', 2)
        self.sprawdzStanSciezki(sciezki[1], '00', '10', 0)

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

    def testDrugiegoKroku(self):
        self.v.liczPierwszy([1,1])
        sciezki = self.v.liczSciezke([1,0])

        self.assertEqual(4, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '00', 3)
        self.sprawdzStanSciezki(sciezki[2], '00', '10', 3)
        self.sprawdzStanSciezki(sciezki[1], '10', '01', 0)
        self.sprawdzStanSciezki(sciezki[3], '10', '11', 2)

if __name__ == '__main__':
    unittest.main()
