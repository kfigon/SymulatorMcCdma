import unittest
from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow


class TestMaszynyStanow(unittest.TestCase):
    def setUp(self):
        odczepy = [[0,1,2], [1,2]]
        r = RejestrPrzesuwny(3, odczepy)
        self.m = MaszynaStanow(r,1)

    def testDlugosc(self):
        self.assertEqual(4, self.m.getNumberOfStates())

    def testStan00_0(self):
        stan = self.m.checkState("00", [0])
        self.assertEqual([0], stan['in'])
        self.assertEqual([0,0], stan['out'])
        self.assertEqual("00", stan['inState'])
        self.assertEqual("00", stan['outState'])

    def testStan00_1(self):
        stan = self.m.checkState("00", [1])
        self.assertEqual([1], stan['in'])
        self.assertEqual([1,0], stan['out'])
        self.assertEqual("00", stan['inState'])
        self.assertEqual("10", stan['outState'])

    def testStan01_0(self):
        stan = self.m.checkState("01", [0])
        self.assertEqual([0], stan['in'])
        self.assertEqual([1,1], stan['out'])
        self.assertEqual("01", stan['inState'])
        self.assertEqual("00", stan['outState'])

    def testStan01_1(self):
        stan = self.m.checkState("01", [1])
        self.assertEqual([1], stan['in'])
        self.assertEqual([0,1], stan['out'])
        self.assertEqual("01", stan['inState'])
        self.assertEqual("10", stan['outState'])

    def testStan10_0(self):
        stan = self.m.checkState("10", [0])
        self.assertEqual([0], stan['in'])
        self.assertEqual([1,1], stan['out'])
        self.assertEqual("10", stan['inState'])
        self.assertEqual("01", stan['outState'])

    def testStan10_1(self):
        stan = self.m.checkState("10", [1])
        self.assertEqual([1], stan['in'])
        self.assertEqual([0,1], stan['out'])
        self.assertEqual("10", stan['inState'])
        self.assertEqual("11", stan['outState'])
        
    def testStan11_0(self):
        stan = self.m.checkState("11", [0])
        self.assertEqual([0], stan['in'])
        self.assertEqual([0,0], stan['out'])
        self.assertEqual("11", stan['inState'])
        self.assertEqual("01", stan['outState'])

    def testStan11_1(self):
        stan = self.m.checkState("11", [1])
        self.assertEqual([1], stan['in'])
        self.assertEqual([1,0], stan['out'])
        self.assertEqual("11", stan['inState'])
        self.assertEqual("11", stan['outState'])
        
class TestMaszynyStanow2(unittest.TestCase):
    def setUp(self):
        #inne odczepy
        odczepy = [[0,1,2], [1,2]]
        r = RejestrPrzesuwny(3, odczepy)
        self.m = MaszynaStanow(r,1)

    def test1(self):
        self.fail()

class TestMaszynyStanow3(unittest.TestCase):
    def setUp(self):
        # wiele inputow
        odczepy = [[0,1,2], [1,2]]
        r = RejestrPrzesuwny(3, odczepy)
        self.m = MaszynaStanow(r,3)

    def test1(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()
