import unittest
from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow


class TestMaszynyStanow(unittest.TestCase):
    def setUp(self):
        odczepy = [[0,1,2], [1,2]]
        r = RejestrPrzesuwny(3, odczepy)
        self.m = MaszynaStanow(r)

    def test1(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()
