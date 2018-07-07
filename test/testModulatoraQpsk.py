import unittest
from modulatorQpsk import Qpsk
from modulatorQpsk import WalidatorPredkosciSygnalow
import utils


class TestWalidatoraPredkosci(unittest.TestCase):
    def testBitowaZleZNosna(self):
        self.assertFalse(WalidatorPredkosciSygnalow.waliduj(10,3,50))

    def testBitowaZleZNosna2(self):
        self.assertFalse(WalidatorPredkosciSygnalow.waliduj(10,11,50))

    def testProbkowaniaZla(self):
        self.assertFalse(WalidatorPredkosciSygnalow.waliduj(10,2,15))

    def testProbkowaniaZla2(self):
        self.assertFalse(WalidatorPredkosciSygnalow.waliduj(10,2,19))

    def testAllOk(self):
        self.assertTrue(WalidatorPredkosciSygnalow.waliduj(10,5,20))

    def testProbkowanieZle3(self):
        self.assertFalse(WalidatorPredkosciSygnalow.waliduj(10,5,21))
    
    def testAllOk2(self):
        self.assertTrue(WalidatorPredkosciSygnalow.waliduj(10,2,20))
    
    def testAllOk3(self):
        self.assertTrue(WalidatorPredkosciSygnalow.waliduj(15,5,30))


class TestModulatoraQpsk(unittest.TestCase):
    def setUp(self):
        self.q = Qpsk(30, 10,5)

    def testMapowaniaSymboli(self):
        dane = [1,0,1,0,0,1]
        symbole = list(self.q.mapujSymbole(dane))

        self.assertEqual([1,1,0], list(map(lambda v: v.real, symbole)))
        self.assertEqual([0,0,1], list(map(lambda v: v.imag, symbole)))

    def testMod(self):
        zmodulowany = self.q.moduluj(utils.generujDaneBinarne(30))
        self.assertEqual(90, len(zmodulowany))

    def testDemod(self):
        dane = utils.generujDaneBinarne(30)
        zmodulowany = self.q.moduluj(dane)
        self.assertEqual(90, len(zmodulowany))
        self.assertEqual(dane, self.q.demodulacja(zmodulowany))

if __name__ == '__main__':
    unittest.main()
