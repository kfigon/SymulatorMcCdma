import unittest
from modulatorQpsk import Qpsk
import utils

class TestModulatoraQpsk(unittest.TestCase):
    def setUp(self):
        self.q = Qpsk(30, 10,5)

    def testSzeregowoRownoleglego(self):
        dane = [1,0,1,0,0,1]
        self.assertEqual([1,1,0], list(self.q.getI(dane)))
        self.assertEqual([0,0,1], list(self.q.getQ(dane)))

    def testWalidacjiDlugosci(self):
        dane = utils.generujDaneBinarne(10)
        self.q.walidujDlugosci(dane)

    def testMod(self):
        zmodulowany = self.q.moduluj(utils.generujDaneBinarne(30))
        self.assertEqual(180, len(zmodulowany))

    def testDemod(self):
        dane = utils.generujDaneBinarne(30)
        zmodulowany = self.q.moduluj(dane)
        self.assertEqual(180, len(zmodulowany))
        self.assertEqual(dane, self.q.demodulacja(zmodulowany))

if __name__ == '__main__':
    unittest.main()
