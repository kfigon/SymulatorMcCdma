import unittest
from maszynaStanow import MaszynaStanow
from rejestrPrzesuwny import RejestrPrzesuwny
from viterbi import Viterbi

class TestyViterbiego(unittest.TestCase):
    def setUp(self):
        odczepy = [[0, 1, 2], [0, 2]]
        r = RejestrPrzesuwny(3, odczepy)
        m = MaszynaStanow(r, 1)
        self.v = Viterbi(m)
    
    def testPierwszego1(self):
        self.v.liczPierwszy([0,0])
        wynik = self.v.traceback()
        self.assertEqual([0], wynik)
    
    def testPierwszego2(self):
        self.v.liczPierwszy([1,1])
        wynik = self.v.traceback()
        self.assertEqual([1], wynik)

if __name__ == '__main__':
    unittest.main()
