import unittest
from rejestrPrzesuwny import RejestrPrzesuwny, RejestrSystematyczny

class TestyRejestruPrzesuwnego1(unittest.TestCase):
    def setUp(self):
        self.r = RejestrPrzesuwny(3, [[0,1,2], [0,2]])
        self.assertEqual("000", str(self.r))

    def testStalych(self):
        self.assertEqual(2, self.r.getDlugoscRejestru())
        self.assertEqual(2, self.r.getIleBitowWyjsciowych())
        self.assertEqual(4, self.r.getNumberOfStates())

    def test1(self):
        self.r.shift(1)
        self.assertEqual([1,1], self.r.licz())
        self.assertEqual("100", str(self.r))
        self.assertEqual("00", self.r.getState())

        self.r.shift(0)
        self.assertEqual([1,0], self.r.licz())
        self.assertEqual("010", str(self.r))
        self.assertEqual("10", self.r.getState())

        self.r.shift(0)
        self.assertEqual([1,1], self.r.licz())
        self.assertEqual("001", str(self.r))
        self.assertEqual("01", self.r.getState())

        self.r.shift(1)
        self.assertEqual([1,1], self.r.licz())
        self.assertEqual("100", str(self.r))
        self.assertEqual("00", self.r.getState())

        self.r.shift(1)
        self.assertEqual([0,1], self.r.licz())
        self.assertEqual("110", str(self.r))
        self.assertEqual("10", self.r.getState())

    def test2(self):
        self.r.shift(0)
        self.assertEqual([0,0], self.r.licz())
        self.r.shift(1)
        self.assertEqual([1,1], self.r.licz())
        self.r.shift(1)
        self.assertEqual([0,1], self.r.licz())
        self.r.shift(0)
        self.assertEqual([0,1], self.r.licz())

class TestyRejestruPrzesuwnego2(unittest.TestCase):
    def setUp(self):
        self.r = RejestrPrzesuwny(3, [[0],[0,2],[0,1,2]])
        self.assertEqual("000", str(self.r))

    def testStalych(self):
        self.assertEqual(2, self.r.getDlugoscRejestru())
        self.assertEqual(3, self.r.getIleBitowWyjsciowych())
        self.assertEqual(4, self.r.getNumberOfStates())

    def test(self):
        self.r.shift(1)
        self.assertEqual([1,1,1], self.r.licz())
        self.r.shift(0)
        self.assertEqual([0,0,1], self.r.licz())
        self.r.shift(0)
        self.assertEqual([0,1,1], self.r.licz())
        self.r.shift(1)
        self.assertEqual([1,1,1], self.r.licz())
        self.r.shift(1)
        self.assertEqual([1,1,0], self.r.licz())
        self.r.shift(0)
        self.assertEqual([0,1,0], self.r.licz())
        self.r.shift(1)
        self.assertEqual([1,0,0], self.r.licz())

class TestyRejestruPrzesuwnego3(unittest.TestCase):
    def setUp(self):
        self.r = RejestrPrzesuwny(4, [[0,2,3],[0,1,3],[0,2]])
        self.assertEqual("0000", str(self.r))

    def testStalych(self):
        self.assertEqual(3, self.r.getDlugoscRejestru())
        self.assertEqual(3, self.r.getIleBitowWyjsciowych())

    def test(self):
        self.r.shift(1)
        self.assertEqual([1,1,1], self.r.licz())
        self.r.shift(0)
        self.assertEqual([0,1,0], self.r.licz())
        self.r.shift(0)
        self.assertEqual([1,0,1], self.r.licz())
        self.r.shift(1)
        self.assertEqual([0,0,1], self.r.licz())
        self.r.shift(1)
        self.assertEqual([1,0,1], self.r.licz())
        self.r.shift(0)
        self.assertEqual([1,1,1], self.r.licz())
        self.r.shift(1)
        self.assertEqual([1,0,0], self.r.licz())

    def testZerowania(self):
        self.r.shift(1)
        self.r.shift(1)
        self.r.shift(1)
        self.r.shift(0)
        self.assertEqual("0111", str(self.r))
        
        self.r.reset()
        self.assertEqual("0000", str(self.r))
        self.assertEqual([0,0,0], self.r.licz())

class TestRejestruSystematycznego(unittest.TestCase):
    def setUp(self):
        # sprzezenie jest na 1,2, w matematyce jest 0,1,2
        self.r = RejestrSystematyczny(3, [[0,2]],[1,2])

    def testStalych(self):
        self.assertEqual(2, self.r.getDlugoscRejestru())
        self.assertEqual(2, self.r.getIleBitowWyjsciowych())
        self.assertEqual(4, self.r.getNumberOfStates())

    def testPusty(self):
        self.assertEqual([0,0], self.r.licz())
        self.assertEqual('000', str(self.r))
    
    def test1(self):
        self.r.shift(1)
        self.assertEqual([1,1], self.r.licz())
        self.assertEqual('100', str(self.r))

    def test2(self):
        self.r.shift(1)
        self.r.shift(1)

        self.assertEqual([1,0], self.r.licz())
        self.assertEqual('010', str(self.r))

    def testInject(self):
        data = [
            {'state':'00', 'in':0, 'expNext':'00' ,'expOut':[0,0]},
            {'state':'00', 'in':1, 'expNext':'10' ,'expOut':[1,1]},

            {'state':'01', 'in':0, 'expNext':'10' ,'expOut':[0,0]},
            {'state':'01', 'in':1, 'expNext':'00' ,'expOut':[1,1]},

            {'state':'10', 'in':0, 'expNext':'11' ,'expOut':[0,1]},
            {'state':'10', 'in':1, 'expNext':'01' ,'expOut':[1,0]},

            {'state':'11', 'in':0, 'expNext':'01' ,'expOut':[0,1]},
            {'state':'11', 'in':1, 'expNext':'11' ,'expOut':[1,0]}
        ]

        for d in data:
            with self.subTest('inject '+str(d)):
                self.r.reset()
                self.r.injectState(d['state'], d['in'])
                
                self.assertEqual(d['state'], self.r.getState())
                self.assertEqual(d['expNext'], self.r.getStateAfterShift())
                self.assertEqual(d['expOut'], self.r.licz())

if __name__ == '__main__':
    unittest.main()

