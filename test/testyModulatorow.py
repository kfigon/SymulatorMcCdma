import unittest
from modulator import Modulator,Qpsk, Bpsk

class TestBaseMod(unittest.TestCase):
    def setUp(self):
        self.m=Modulator()

    def test(self):
        self.assertRaises(Exception, self.m.mapuj, [])
        self.assertRaises(Exception, self.m.demapuj, [])

class TestQpsk(unittest.TestCase):
    def setUp(self):
        self.m=Qpsk()

    def testModulatoraQpsk(self):
        dane = [1,0,1,1,0,0]
        qpsk = self.m.mapuj(dane)
        exp = [complex(-1,1),complex(-1,-1),complex(1,1)]
        self.assertEqual(exp, qpsk)

    def testDemodulatoraQpsk(self):
        qpsk = [complex(-14,0.5),complex(-1.4,-4),complex(1,1)]
        dane = self.m.demapuj(qpsk)
        exp = [-14,0.5,-1.4,-4,1,1]
        self.assertEqual(exp, dane)

class TestBpsk(unittest.TestCase):
    def setUp(self):
        self.m=Bpsk()

    def testModulatoraBpsk(self):
        dane = [1,0,1]
        bpsk = self.m.mapuj(dane)
        exp = [complex(-1,0),complex(1,0),complex(-1,0)]
        self.assertEqual(exp, bpsk)

    def testDemodulatoraBpsk(self):
        bpsk = [complex(-1.54,0),complex(14,0),complex(-1,0)]
        dane = self.m.demapuj(bpsk)
        exp = [1,0,1]
        self.assertEqual(exp, dane)

if __name__ == '__main__':
    unittest.main()