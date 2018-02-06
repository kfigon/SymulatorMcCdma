import unittest
from rejestrPrzesuwny import RejestrPrzesuwny

class KoderSplotowy:
    def __init__(self, rejestrPrzesuwny):
        self.__rejestr = rejestrPrzesuwny
        
    def koduj(self, daneBinarne):
        pass

class TestKoderaSplotowego(unittest.TestCase):
    def setUp(self):
        r = RejestrPrzesuwny()
        self.k = KoderSplotowy(r)

    def test1(self):
        self.fail()
        
if __name__ == '__main__':
    unittest.main()
