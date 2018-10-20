import unittest
import json
from config import Konfiguracja, budujKonfiguracje
from modulator import Qpsk
from koderTurbo import KoderTurbo

class TestKonfiguracji(unittest.TestCase):
    def test(self):
        config = '''{
            "ileBitow": 99900,
            "ileStrumieni": 2,
            "tylkoPrzebiegiCzasowe": true
            }'''
        k = Konfiguracja(json.loads(config))
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
        config = '''[{
                "ileBitow": 99900,
                "ileStrumieni": 2,
                "tylkoPrzebiegiCzasowe": true
            }, {
                "ileBitow": 1234
            }]'''
        konfigi = budujKonfiguracje(config)
        self.assertEqual(64, konfigi[0].read('dlugoscKoduWalsha'))
        self.assertEqual(64, konfigi[1].read('dlugoscKoduWalsha'))

        self.assertEqual(99900, konfigi[0].read('ileBitow'))
        self.assertEqual(1234, konfigi[1].read('ileBitow'))

    def testWieluKonfiguracjiDefault(self):
        konfigi = budujKonfiguracje()
        self.assertEqual(1, len(konfigi))
        self.assertEqual(64, konfigi[0].read('dlugoscKoduWalsha'))

    def testOdczepowKodera(self):
        k = Konfiguracja()
        self.assertEqual(3, k.read('koder1')['ileKomorekRejestru'])
        self.assertEqual([[0,2]], k.read('koder1')['odczepy'])
        self.assertEqual([1,2], k.read('koder1')['odczepySprzezenia'])

    def testKonfiguracjiKodera(self):
        config = '''[
            {
                "koder1" :{
                    "ileKomorekRejestru": 123,
                    "odczepy": [[56,456,123]]
                },
                "koder2": {
                    "ileKomorekRejestru":567
                }
            }
        ]'''
        konfigi = budujKonfiguracje(config)
        self.assertEqual(1, len(konfigi))
        self.assertEqual(64, konfigi[0].read('dlugoscKoduWalsha'))
        self.assertEqual(123, konfigi[0].read('koder1')['ileKomorekRejestru'])
        self.assertEqual([[56,456,123]], konfigi[0].read('koder1')['odczepy'])
        self.assertEqual(567, konfigi[0].read('koder2')['ileKomorekRejestru'])
    
    def testBudowaniaModulatora(self):
        k = Konfiguracja()
        m = k.stworzModulator()
        self.assertEqual(Qpsk, type(m))

    def testBudowaniaKodera(self):
        k = Konfiguracja()
        m = k.budujKoder()
        self.assertEqual(KoderTurbo, type(m))

if __name__ == '__main__':
    unittest.main()