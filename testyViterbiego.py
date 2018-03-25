import unittest
from maszynaStanow import MaszynaStanow
from rejestrPrzesuwny import RejestrPrzesuwny
from viterbi import Viterbi
from viterbi import Sciezka

class TestyViterbiego(unittest.TestCase):
    def setUp(self):
        odczepy = [[0, 1, 2], [0, 2]]
        r = RejestrPrzesuwny(3, odczepy)
        m = MaszynaStanow(r, 1)
        self.v = Viterbi(m)

    def sprawdzStanSciezki(self, sciezka, expInState, expOutState, expHamming):
        stan = sciezka.getOstatniStan()
        self.assertEqual(expInState, stan['inState'], 'blad! Stan wejsciowy')
        self.assertEqual(expOutState, stan['outState'], 'blad! Stan wyjsciowy')
        self.assertEqual(expHamming, sciezka.getZakumulowanyHamming(), 'blad! hamming')

    def testPierwszyKrok(self):
        sciezki = self.v.liczPierwszy([1,1])

        self.assertEqual(2, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '00', 2)
        self.sprawdzStanSciezki(sciezki[1], '00', '10', 0)

    def testSciezkiDochodzaceDoStanu_2Krok_00(self):
        self.v.liczPierwszy([1, 1])
        sciezki = self.v.getSciezkiDochodzaceDoStanu('00')

        self.assertEqual(1, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '00', 2)

    def testSciezkiDochodzaceDoStanu_2Krok_01(self):
        self.v.liczPierwszy([1, 1])
        sciezki = self.v.getSciezkiDochodzaceDoStanu('01')
        self.assertEqual(1, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '10', 0)

    def testSciezkiDochodzaceDoStanu_2Krok_10(self):
        self.v.liczPierwszy([1, 1])
        sciezki = self.v.getSciezkiDochodzaceDoStanu('10')
        self.assertEqual(1, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '00', 2)

    def testSciezkiDochodzaceDoStanu_2Krok_11(self):
        self.v.liczPierwszy([1, 1])
        sciezki = self.v.getSciezkiDochodzaceDoStanu('11')
        self.assertEqual(1, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '10', 0)

    def testDrugiegoKroku(self):
        self.v.liczPierwszy([1,1])
        sciezki = self.v.liczSciezke([1,0])

        self.assertEqual(4, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '00', 3)
        self.sprawdzStanSciezki(sciezki[2], '00', '10', 3)
        self.sprawdzStanSciezki(sciezki[1], '10', '01', 0)
        self.sprawdzStanSciezki(sciezki[3], '10', '11', 2)

    def testTrzeciegoKroku(self):
        self.v.liczPierwszy([1,1])
        self.v.liczSciezke([1,0])
        sciezki = self.v.liczSciezke([1, 1])

        self.assertEqual(4, len(sciezki))
        self.sprawdzStanSciezki(sciezki[0], '00', '10', 3)
        self.sprawdzStanSciezki(sciezki[1], '01', '00', 0)
        self.sprawdzStanSciezki(sciezki[2], '11', '01', 3)
        self.sprawdzStanSciezki(sciezki[3], '10', '11', 4)

    def testAsd(self):
        tab=[{'id':1, 'val':1, 'czyUsunac':False},
             {'id': 5, 'val': 2, 'czyUsunac':False},
             {'id':2, 'val':1, 'czyUsunac':False},
             {'id': 4, 'val': 2, 'czyUsunac':False},
             {'id':1, 'val':0, 'czyUsunac':False},
             {'id':4, 'val':2, 'czyUsunac':False},
             {'id':5, 'val':3, 'czyUsunac':False},
             {'id': 1, 'val': 1, 'czyUsunac': False},
             {'id': 5, 'val': 1, 'czyUsunac': False},
             {'id': 2, 'val': 1, 'czyUsunac': False},
             {'id': 4, 'val': 2, 'czyUsunac': False},
             {'id': 1, 'val': 3, 'czyUsunac': False},
             {'id': 4, 'val': 2, 'czyUsunac': False},
             {'id': 5, 'val': 0, 'czyUsunac': False},
             {'id': 1, 'val': 1, 'czyUsunac': False},
             {'id': 5, 'val': 1, 'czyUsunac': False},
             {'id': 2, 'val': 1, 'czyUsunac': False},
             {'id': 4, 'val': 2, 'czyUsunac': False},
             {'id': 1, 'val': 0, 'czyUsunac': False},
             {'id': 4, 'val': 2, 'czyUsunac': False},
             {'id': 5, 'val': 3, 'czyUsunac': False}]


        for i in range(len(tab)):
            el1 = tab[i]
            if(el1['czyUsunac']):
                continue
            for j in range(len(tab)):
                if(i==j):
                    continue
                el2 = tab[j]
                if(el1['id'] == el2['id']):
                    if(el1['val'] == el2['val']):
                        el2['czyUsunac'] = True
                    elif(el1['val'] > el2['val']):
                        el1['czyUsunac'] = True
                    else:
                        el2['czyUsunac'] = True

        outTab = list(filter(lambda x: not x['czyUsunac'], tab))

        expTab=[{'id':2, 'val':1, 'czyUsunac':False},
                {'id': 4, 'val': 2, 'czyUsunac':False},
                {'id': 1, 'val': 0, 'czyUsunac':False},
                {'id': 5, 'val': 0, 'czyUsunac': False}]

        self.assertEqual(expTab, outTab)

if __name__ == '__main__':
    unittest.main()
