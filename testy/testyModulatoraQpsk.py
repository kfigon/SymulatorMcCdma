import unittest
from modulatorQpsk import Qpsk
import utils

class TestModulatoraQpsk(unittest.TestCase):
    def setUp(self):
        self.q = Qpsk(10, 2,1)

    def testSzeregowoRownoleglego(self):
        dane = [1,0,1,0,0,1]
        self.assertEqual([1,1,0], list(self.q.getI(dane)))
        self.assertEqual([0,0,1], list(self.q.getQ(dane)))

    def testWalidacjiDlugosci(self):
        dane = utils.generujDaneBinarne(10)
        self.q.walidujDlugosci(dane)

    def testMod(self):
        zmodulowany = self.q.moduluj(utils.generujDaneBinarne(10))
        self.assertEqual(100, len(zmodulowany))

if __name__ == '__main__':
    unittest.main()
