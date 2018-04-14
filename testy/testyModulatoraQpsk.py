import unittest
from modulatorQpsk import Qpsk

class TestModulatoraQpsk(unittest.TestCase):
    def setUp(self):
        self.q = Qpsk(12, 1)

    def testGenerowaniaNosnej(self):
        exp = [1.0, 0.8660254037844387, 0.5000000000000001, 6.123233995736766e-17, -0.4999999999999998, -0.8660254037844387,
         -1.0, -0.8660254037844386, -0.5000000000000004, -1.8369701987210297e-16, 0.5000000000000001,
         0.8660254037844384, 1.0, 0.866025403784439, 0.4999999999999997, 3.061616997868383e-16, -0.4999999999999992,
         -0.8660254037844388, -1.0, -0.8660254037844392, -0.49999999999999983, -4.286263797015736e-16,
         0.4999999999999991, 0.8660254037844387, 1.0, 0.8660254037844383, 0.5000000000000014, 5.51091059616309e-16,
         -0.5000000000000006, -0.8660254037844377, -1.0, -0.8660254037844393, -0.5000000000000016,
         -2.4499125789312946e-15, 0.5000000000000004, 0.8660254037844386]
        czas = self.q.generujCzas(3)
        self.assertAlmostEqual(exp, list(self.q.generujNosna(czas)))

    def testSzeregowoRownoleglego(self):
        dane = [1,0,1,0,0,1]
        self.assertEqual([1,1,0], list(self.q.getI(dane)))
        self.assertEqual([0,0,1], list(self.q.getQ(dane)))

    def testMod(self):
        dane = [1,0,1,0,0]
        self.fail('todo')


if __name__ == '__main__':
    unittest.main()
