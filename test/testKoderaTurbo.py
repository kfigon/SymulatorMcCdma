import unittest
from koderTurbo import KoderTurbo
from unittest.mock import MagicMock
from przeplot import Przeplatacz

class TestKoderaTurbo(unittest.TestCase):
    def setUp(self):
        self.k1 = MagicMock()
        self.k2 = MagicMock()
        self.k=KoderTurbo(koder1=self.k1, koder2=self.k2, przeplatacz=Przeplatacz())

    def test(self):
        k1output = [1,2,3,4]
        k2output = [5, 6, 7, 8, 9]
        self.k1.koduj = MagicMock(return_value=k1output)
        self.k2.koduj = MagicMock(return_value=k2output)
        indata = [1,2]

        wynik = self.k.koduj(indata)

        self.assertEqual(k2output, wynik)
        self.k1.koduj.assert_called_with(indata)
        self.k2.koduj.assert_called_with(k1output)


if __name__ =='__main__':
    unittest.main()