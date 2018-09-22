import unittest
from utils import *

class TestyUtilsow(unittest.TestCase):
    def testHamminga(self):
        self.assertEqual(0, odlegloscHamminga([1,1,1,0],[1,1,1,0]))
        self.assertEqual(1, odlegloscHamminga([1,1,1,0],[1,1,1,1]))
        self.assertEqual(2, odlegloscHamminga([1,0,1,0],[0,1,1,0]))

    def testDzielenia1(self):
        wej = [1,0, 1,0, 1,1, 0,0]
        exp = [[1,0],[1,0],[1,1],[0,0]]
        self.assertEqual(exp, podziel(wej,2))

    def testDzielenia2(self):
        wej = [1,0, 1,0, 1,1, 0,0,1]
        exp = [[1,0,1], [0,1,1], [0,0,1]]
        self.assertEqual(exp, podziel(wej,3))

    def testGeneratoraBinarnego(self):
        dane = generujDaneBinarne(1000)
        self.assertEqual(1000, len(dane))
        for i in dane:
            if(i != 0 and i != 1):
                self.fail('element %d nie jest binarny!' % i)

    def testProbkowaniaBinarnego1(self):
        dane = [1,0,1,1]
        exp = [1,1,1, 0,0,0, 1,1,1, 1,1,1]
        self.assertEqual(exp, probkuj(dane, 3, 1))

    def testProbkowaniaBinarnego2(self):
        dane = [1,0,1,1]
        exp = [1,1,1, 0,0,0, 1,1,1, 1,1,1]
        self.assertEqual(exp, probkuj(dane, 6, 2))

    def testProbkowaniaBinarnego3(self):
        dane = [1,0,1,1]
        exp = [1,1,1,1, 0,0,0,0, 1,1,1,1, 1,1,1,1]
        self.assertEqual(exp, probkuj(dane, 4, 1))

    def testCzasuTrwania(self):
        self.assertEqual(10, getCzasTransmisji(10,1))
        self.assertEqual(10, getCzasTransmisji(5, 0.5))
        self.assertEqual(5, getCzasTransmisji(10, 2))

    def testBipolar(self):
        dane = [1,0,1,1,0]
        exp = [-1, 1, -1, -1, 1]
        tab = [bipolar(i) for i in dane]
        self.assertEqual(exp, tab)

    def testDzieleniaNaKanaly(self):

        dane = [
            { 'tab': [0,1,1,1,0,0,1,0,1,0], 'poIle': 2, 'exp': [[0,1,0,1,1], [1,1,0,0,0]] },
            { 'tab': [0,1,1,1,0,0,1,0,1], 'poIle': 3, 'exp': [[0,1,1], [1,0,0], [1,0,1]] },
            
        ]

        for d in dane:
            with self.subTest(name='po '+ str(d['poIle'])):

                result = podzielDaneNaKanaly(d['tab'], ileKanalow=d['poIle'])

                self.assertEqual(len(d['exp']), len(result))
                for r,e in zip(result, d['exp']):
                    self.assertEqual(e, r)
    def testFlat1(self):
        dane = [[1,2,3], [4,5],[6],[7,8,9]]
        flatted = flat(dane)
        self.assertEqual([1,2,3,4,5,6,7,8,9], flatted)
    
    def testFlat2(self):
        dane = [[1,2,3], [], [4,5],[6],[7,8,9]]
        flatted = flat(dane)
        self.assertEqual([1,2,3,4,5,6,7,8,9], flatted)

    def testGenerujSzum(self):
        res = generujSzum(ile=500)
        self.assertEqual(500, len(res))

        for i in res:
            self.assertLessEqual(i, 5)
            self.assertGreaterEqual(i, -5)

    def testModulatoraQpsk(self):
        dane = [1,0,1,1,0,0]
        qpsk = generujQpskZBitow(dane)
        exp = [complex(-1,1),complex(-1,-1),complex(1,1)]
        self.assertEqual(exp, qpsk)

    def testDemodulatoraQpsk(self):
        qpsk = [complex(-1,1),complex(-1,-1),complex(1,1)]
        dane = demodulujQpsk(qpsk)
        exp = [1,0,1,1,0,0]
        self.assertEqual(exp, dane)

if __name__ == '__main__':
    unittest.main()
