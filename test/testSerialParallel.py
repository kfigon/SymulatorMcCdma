import unittest
from przetwornikSP import PrzetwornikSzeregowoRownolegly

class TestSzeregowoRownolegly4(unittest.TestCase):
    def setUp(self):
        self.p = PrzetwornikSzeregowoRownolegly(4)
    
    def test1(self):
        dane = [0,1,1,0]
        exp = [[0],[1],[1],[0]]
        self.assertEqual(exp, self.p.rozdziel(dane))

    def test2(self):
        dane = [0,1,1,0,1,1,0,0]
        exp = [[0,1],[1,0],[1,1],[0,0]]
        self.assertEqual(exp, self.p.rozdziel(dane))

    def test3(self):
        dane = [0,1,1, 0,1,1, 0,0,0, 1,1,0]
        exp = [[0,1,1], [0,1,1], [0,0,0], [1,1,0]]
        self.assertEqual(exp, self.p.rozdziel(dane))


if __name__ == '__main__':
    unittest.main()