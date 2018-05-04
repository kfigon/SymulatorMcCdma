import unittest
from generatorKoduWalsha import GeneratorKoduWalsha

class TestGeneratora(unittest.TestCase):
    def setUp(self):
        self.g = GeneratorKoduWalsha(5)

    def test(self):
        self.fail('todo')
    
    # def test0(self):
    #     expected = [[1]]
    #     self.assertEqual(expected, self.g.generuj(0))

    # def testMatrix1(self):
    #     expected = [
    #         [1,1],
    #         [1,-1]
    #     ]
    

    # def test2(self):
    #     expected = [
    #         [1,  1,  1,  1],
    #         [1, -1,  1, -1],
    #         [1,  1, -1, -1],
    #         [1, -1, -1,  1]]
    

    # def test3(self):
    #     expected = [
    #         [1,  1,  1,  1,  1,  1,  1,  1],
    #         [1, -1,  1, -1,  1, -1,  1, -1],
    #         [1,  1, -1, -1,  1,  1, -1, -1],
    #         [1, -1, -1,  1,  1, -1, -1,  1],
    #         [1,  1,  1,  1, -1, -1, -1, -1],
    #         [1, -1,  1, -1, -1,  1, -1,  1],
    #         [1,  1, -1, -1, -1, -1,  1,  1],
    #         [1, -1, -1,  1, -1,  1,  1, -1]]

    
    
if __name__ == '__main__':
    unittest.main()