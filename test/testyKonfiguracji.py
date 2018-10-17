import unittest
from config import Konfiguracja

class TestKonfiguracji(unittest.TestCase):
    def test(self):
        config = '''{
            "ileBitow": 99900,
            "ileStrumieni": 2,
            "tylkoPrzebiegiCzasowe": true
            }'''
        k = Konfiguracja(config)
        self.assertEqual(99900, k.read('ileBitow'))
        self.assertEqual(2, k.read('ileStrumieni'))
        self.assertEqual(True, k.read('tylkoPrzebiegiCzasowe'))
    
    def testDefault(self):
        k = Konfiguracja()
        self.assertEqual(100, k.read('ileBitow'))
        self.assertEqual(5, k.read('ileStrumieni'))
        self.assertEqual(2, k.read('numerKoduWalsha'))
        self.assertEqual(False, k.read('tylkoPrzebiegiCzasowe'))
        
    def testWieluKonfiguracji(self):
        self.fail("to impl")
        # tablica konfigow, defauly, tytuly

    def testOdczepowKodera(self):
        k = Konfiguracja()
        self.assertEqual(4, k.read('ileKomorekRejestru'))
        self.assertEqual([[0,1,3],[0,1]], k.read('odczepy'))
        self.assertEqual([2,4], k.read('odczepySprzezenia'))

if __name__ == '__main__':
    unittest.main()