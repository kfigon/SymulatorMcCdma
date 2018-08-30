import unittest
from przeplot import Przeplatacz

class TestPrzeplotu(unittest.TestCase):

    def testAligned(self):
        dane = [
            {'in':[1,2,3, 4,5,6, 7,8,9], 'exp':[1,4,7, 2,5,8, 3,6,9], 'szerokoscPrzeplotu': 3},
            {'in':[1,2,3,4 ,5,6,7,8], 'exp':[1,5, 2,6, 3,7, 4,8], 'szerokoscPrzeplotu': 4},
            {'in':[1,2,3,4,5 ,6,7,8,9,10, 11,12,13,14,15], 
                'exp':[1,6,11, 2,7,12, 3,8,13, 4,9,14, 5,10,15], 'szerokoscPrzeplotu': 5},
            ]

        for d in dane:
            nazwa = 'test z szerokoscia ' + str(d['szerokoscPrzeplotu'])
            p = Przeplatacz(d['szerokoscPrzeplotu'])
                
            with self.subTest(name=nazwa):
                przeplecione = p.przeplot(d['in'])
                self.assertEqual(d['exp'], przeplecione, 'przeplot failed')

                rozplecione = p.rozplot(przeplecione)
                self.assertEqual(d['in'], rozplecione, 'rozplot failed')
        

if __name__ == '__main__':
    unittest.main()