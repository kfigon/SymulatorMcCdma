import unittest
from generatorKoduWalsha import GeneratorKoduWalsha

class TestGeneratora64(unittest.TestCase):
    def setUp(self):
        self.g = GeneratorKoduWalsha(64)

    def test0(self):
        exp = [0 for i in range(64)]
        self.assertEqual(exp, self.g.generuj(0))

    def test1(self):
        exp = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        self.assertEqual(exp, self.g.generuj(1))

    def test2(self):
        exp = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1,
 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1,
 0, 0, 1, 1, 0, 0, 1, 1]
        self.assertEqual(exp, self.g.generuj(2))

    def test3(self):
        exp = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0,
  0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
        self.assertEqual(exp, self.g.generuj(3))

    def test4(self):
        exp = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1,
  0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
        self.assertEqual(exp, self.g.generuj(4))

    def test5(self):
        exp = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0,
  0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
        self.assertEqual(exp, self.g.generuj(5))

    def test6(self):
        exp = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
        self.assertEqual(exp, self.g.generuj(6))

    def test7(self):
        exp =[0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1,
 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
        self.assertEqual(exp, self.g.generuj(7))


    def test8(self):
        exp = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(exp, self.g.generuj(8))

    def test9(self):
        exp = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0,
  0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0]
        self.assertEqual(exp, self.g.generuj(9))


    def test32(self):
        exp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(exp, self.g.generuj(32))

class TestWalshaRozneDlugosc(unittest.TestCase):
    def test2(self):
        g = GeneratorKoduWalsha(2)
        self.assertEqual([0,0], g.generuj(0))
        self.assertEqual([0, 1], g.generuj(1))

    def test4(self):
        g = GeneratorKoduWalsha(4)
        self.assertEqual([0,0,0,0], g.generuj(0))
        self.assertEqual([0, 1,0,1], g.generuj(1))
        self.assertEqual([0,0,1,1], g.generuj(2))
        self.assertEqual([0,1,1,0], g.generuj(3))

    def test8(self):
        g = GeneratorKoduWalsha(8)
        self.assertEqual([0,0,0,0,0,0,0,0], g.generuj(0))
        self.assertEqual([0,1,0,1,0,1,0,1], g.generuj(1))
        self.assertEqual([0,0,1,1,0,0,1,1], g.generuj(2))
        self.assertEqual([0,1,1,0,0,1,1,0], g.generuj(3))

        self.assertEqual([0, 0, 0, 0, 1,1,1,1], g.generuj(4))
        self.assertEqual([0,1,0,1,1,0,1,0], g.generuj(5))
        self.assertEqual([0,0,1,1,1,1,0,0], g.generuj(6))
        self.assertEqual([0,1,1,0,1,0,0,1], g.generuj(7))


    
if __name__ == '__main__':
    unittest.main()