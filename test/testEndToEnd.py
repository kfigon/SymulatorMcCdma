import unittest
from kontroler import liczBer
from config import Konfiguracja

class TestEndToEnd(unittest.TestCase):
    def testE2E(self):
        ber,berProcent = liczBer(Konfiguracja(), 0)
        self.assertEqual(ber, 0)
