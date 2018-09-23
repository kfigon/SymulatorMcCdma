import unittest
from config import Konfiguracja

class TestKonfiguracji(unittest.TestCase):
    def test(self):
        config = '''{
            "ileBitow": 100,
            "ileStrumieni": 2,
            "tylkoPrzebiegiCzasowe": true
            }'''
        k = Konfiguracja(config)
        self.assertEqual(100, k.read('ileBitow'))
        self.assertEqual(2, k.read('ileStrumieni'))
        self.assertEqual(1, k.read('ileIteracji'))
        self.assertEqual(True, k.read('tylkoPrzebiegiCzasowe'))
    
    def testDefault(self):
        k = Konfiguracja()
        self.assertEqual(90, k.read('ileBitow'))
        self.assertEqual(5, k.read('ileStrumieni'))
        self.assertEqual(2, k.read('numerKoduWalsha'))
        self.assertEqual(1, k.read('ileIteracji'))
        self.assertEqual(False, k.read('tylkoPrzebiegiCzasowe'))

if __name__ == '__main__':
    unittest.main()