import unittest
from rejestrPrzesuwny import RejestrPrzesuwny

class TestyRejestruPrzesuwnego1(unittest.TestCase):
    def setUp(self):
        self.r = RejestrPrzesuwny(3, [[0,1,2], [0,2]])
        self.assertEqual("00", str(self.r))
        
    def test1(self):
        self.assertEqual((1,1), self.r.shift(1))
        self.assertEqual("10", str(self.r))

        self.assertEqual((1,0), self.r.shift(0))
        self.assertEqual("01", str(self.r))

        self.assertEqual((1,1), self.r.shift(0))
        self.assertEqual("00", str(self.r))

        self.assertEqual((1,1), self.r.shift(1))
        self.assertEqual("10", str(self.r))

        self.assertEqual((0,1), self.r.shift(1))
        self.assertEqual("11", str(self.r))

    def test2(self):
        self.assertEqual((0,0), self.r.shift(0))
        self.assertEqual((1,1), self.r.shift(1))
        self.assertEqual((0,1), self.r.shift(1))
        self.assertEqual((0,1), self.r.shift(0))

class TestyRejestruPrzesuwnego2(unittest.TestCase):
    def setUp(self):
        self.r = RejestrPrzesuwny(3, [[0],[0,2],[0,1,2]])
        self.assertEqual("00", str(self.r))

    def test(self):
        self.assertEqual((1,1,1), self.r.shift(1))
        self.assertEqual((0,0,1), self.r.shift(0))
        self.assertEqual((0,1,1), self.r.shift(0))
        self.assertEqual((1,1,1), self.r.shift(1))
        self.assertEqual((1,1,0), self.r.shift(1))
        self.assertEqual((0,1,0), self.r.shift(0))
        self.assertEqual((1,0,0), self.r.shift(1))

class TestyRejestruPrzesuwnego3(unittest.TestCase):
    def setUp(self):
        self.r = RejestrPrzesuwny(4, [[0,2,3],[0,1,3],[0,2]])
        self.assertEqual("000", str(self.r))

    def test(self):
        self.assertEqual((1,1,1), self.r.shift(1))
        self.assertEqual((0,1,0), self.r.shift(0))
        self.assertEqual((1,0,1), self.r.shift(0))
        self.assertEqual((0,0,1), self.r.shift(1))
        self.assertEqual((1,0,1), self.r.shift(1))
        self.assertEqual((1,1,1), self.r.shift(0))
        self.assertEqual((1,0,0), self.r.shift(1))
     
if __name__ == '__main__':
    unittest.main()

