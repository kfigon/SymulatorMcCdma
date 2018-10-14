import unittest
from rejestrPrzesuwny import RejestrPrzesuwny,RejestrSystematyczny
from maszynaStanow import MaszynaStanow


class TestMaszynyStanow(unittest.TestCase):
    def setUp(self):
        odczepy = [[0,1,2], [1,2]]
        r = RejestrPrzesuwny(3, odczepy)
        self.m = MaszynaStanow(r,1)

    def testDlugosc(self):
        self.assertEqual(4, self.m.getNumberOfStates())

    def sprawdzStan(self, stan, expIn, expOut, expInSt, expOutSt):
        self.assertEqual(expIn, stan['in'], 'blad! Bity wejsciowe')
        self.assertEqual(expOut, stan['out'], 'blad! Bity wyjsciowe')
        self.assertEqual(expInSt, stan['inState'], 'blad! Stan wejsciowy')
        self.assertEqual(expOutSt, stan['outState'], 'blad! Stan wyjsciowy')

    def testStan00_0(self):
        stan = self.m.checkState("00", [0])
        self.sprawdzStan(stan, [0],[0,0], "00", "00")

    def testStan00_1(self):
        stan = self.m.checkState("00", [1])
        self.sprawdzStan(stan, [1],[1,0], "00", "10")

    def testStan01_0(self):
        stan = self.m.checkState("01", [0])
        self.sprawdzStan(stan, [0],[1,1], "01", "00")

    def testStan01_1(self):
        stan = self.m.checkState("01", [1])
        self.sprawdzStan(stan, [1],[0,1], "01", "10")

    def testStan10_0(self):
        stan = self.m.checkState("10", [0])
        self.sprawdzStan(stan, [0],[1,1], "10", "01")

    def testStan10_1(self):
        stan = self.m.checkState("10", [1])
        self.sprawdzStan(stan, [1],[0,1], "10", "11")

    def testStan11_0(self):
        stan = self.m.checkState("11", [0])
        self.sprawdzStan(stan, [0],[0,0], "11", "01")

    def testStan11_1(self):
        stan = self.m.checkState("11", [1])
        self.sprawdzStan(stan, [1],[1,0], "11", "11")

    def testPrzejscStanow00(self):
        stany = self.m.getMozliwePrzejscia('00')
        self.assertEqual(2, len(stany))

        self.sprawdzStan(stany[0], [0],[0,0], "00", "00")
        self.sprawdzStan(stany[1], [1],[1,0], "00", "10")

    def testPrzejscStanow01(self):
        stany = self.m.getMozliwePrzejscia('01')
        self.assertEqual(2, len(stany))
        self.sprawdzStan(stany[0], [0],[1,1], "01", "00")
        self.sprawdzStan(stany[1], [1],[0,1], "01", "10")

    def testDojsciaDo00(self):
        stany = self.m.getMozliweDojscia('00')
        self.assertEqual(2, len(stany))

        self.sprawdzStan(stany[0], [0],[0,0], "00", "00")
        self.sprawdzStan(stany[1], [0],[1,1], "01", "00")

    def testDojsciaDo01(self):
        stany = self.m.getMozliweDojscia('01')
        self.assertEqual(2, len(stany))

        self.sprawdzStan(stany[0], [0],[1,1], "10", "01")
        self.sprawdzStan(stany[1], [0],[0,0], "11", "01")

    def testDojsciaDo10(self):
        stany = self.m.getMozliweDojscia('10')
        self.assertEqual(2, len(stany))

        self.sprawdzStan(stany[0], [1],[1,0], "00", "10")
        self.sprawdzStan(stany[1], [1],[0,1], "01", "10")

    def testDojsciaDo11(self):
        stany = self.m.getMozliweDojscia('11')
        self.assertEqual(2, len(stany))

        self.sprawdzStan(stany[0], [1],[0,1], "10", "11")
        self.sprawdzStan(stany[1], [1],[1,0], "11", "11")

    def testStanPoczatkowy(self):
        stan = self.m.getStanPoczatkowy()
        self.assertEqual('00', stan)

    def testListyStanow(self):
        stany = self.m.getListaStanow()
        self.assertEqual(4, len(stany))
        self.assertEqual('00', stany[0])
        self.assertEqual('01', stany[1])
        self.assertEqual('10', stany[2])
        self.assertEqual('11', stany[3])

    def testPolaczenia(self):
        self.assertTrue(self.m.czyPolaczone('00', '00'))
        self.assertTrue(self.m.czyPolaczone('00', '10'))
        self.assertTrue(self.m.czyPolaczone('10', '01'))
        self.assertTrue(self.m.czyPolaczone('10', '11'))
        self.assertTrue(self.m.czyPolaczone('01', '00'))
        self.assertTrue(self.m.czyPolaczone('01', '10'))
        self.assertTrue(self.m.czyPolaczone('11', '01'))
        self.assertTrue(self.m.czyPolaczone('11', '11'))

        self.assertFalse(self.m.czyPolaczone('00', '11'))
        self.assertFalse(self.m.czyPolaczone('11', '00'))
        self.assertFalse(self.m.czyPolaczone('01', '11'))

    def testGetStan(self):
        self.sprawdzStan(self.m.getStan('00', '00'),
                         [0], [0,0], '00','00')

        self.sprawdzStan(self.m.getStan('10', '01'),
                         [0], [1, 1], '10', '01')

        self.sprawdzStan(self.m.getStan('11', '01'),
                         [0], [0,0], '11','01')


class TestMaszynyStanow2(unittest.TestCase):
    def setUp(self):
        #inne odczepy
        odczepy = [[0,2,3], [0,1,3], [0,2]]
        r = RejestrPrzesuwny(4, odczepy)
        self.m = MaszynaStanow(r,1)

    def testListyStanow(self):
        stany = self.m.getListaStanow()
        self.assertEqual(8, len(stany))
        self.assertEqual('000', stany[0])
        self.assertEqual('001', stany[1])
        self.assertEqual('010', stany[2])
        self.assertEqual('011', stany[3])
        self.assertEqual('100', stany[4])
        self.assertEqual('101', stany[5])
        self.assertEqual('110', stany[6])
        self.assertEqual('111', stany[7])

    def sprawdzStan(self, stan, expIn, expOut, expInSt, expOutSt):
        self.assertEqual(expIn, stan['in'])
        self.assertEqual(expOut, stan['out'])
        self.assertEqual(expInSt, stan['inState'])
        self.assertEqual(expOutSt, stan['outState'])

    def testDlugosc(self):
        self.assertEqual(8, self.m.getNumberOfStates())

    def testStan000_0(self):
        stan = self.m.checkState("000", [0])
        self.sprawdzStan(stan, [0],[0,0,0],"000","000")

    def testStan000_1(self):
        stan = self.m.checkState("000", [1])
        self.sprawdzStan(stan, [1],[1,1,1],"000","100")

    def testStan001_0(self):
        stan = self.m.checkState("001", [0])
        self.sprawdzStan(stan, [0],[1,1,0],"001","000")

    def testStan001_1(self):
        stan = self.m.checkState("001", [1])
        self.sprawdzStan(stan, [1],[0,0,1],"001","100")

    def testStan010_0(self):
        stan = self.m.checkState("010", [0])
        self.sprawdzStan(stan, [0],[1,0,1],"010","001")

    def testStan010_1(self):
        stan = self.m.checkState("010", [1])
        self.sprawdzStan(stan, [1],[0,1,0],"010","101")

    def testStan011_0(self):
        stan = self.m.checkState("011", [0])
        self.sprawdzStan(stan, [0],[0,1,1],"011","001")

    def testStan011_1(self):
        stan = self.m.checkState("011", [1])
        self.sprawdzStan(stan, [1],[1,0,0],"011","101")

    def testStan100_0(self):
        stan = self.m.checkState("100", [0])
        self.sprawdzStan(stan, [0],[0,1,0],"100","010")

    def testStan100_1(self):
        stan = self.m.checkState("100", [1])
        self.sprawdzStan(stan, [1],[1,0,1],"100","110")

    def testStan101_0(self):
        stan = self.m.checkState("101", [0])
        self.sprawdzStan(stan, [0],[1,0,0],"101","010")

    def testStan101_1(self):
        stan = self.m.checkState("101", [1])
        self.sprawdzStan(stan, [1],[0,1,1],"101","110")

    def testStan110_0(self):
        stan = self.m.checkState("110", [0])
        self.sprawdzStan(stan, [0],[1,1,1],"110","011")

    def testStan110_1(self):
        stan = self.m.checkState("110", [1])
        self.sprawdzStan(stan, [1],[0,0,0],"110","111")

    def testStan111_0(self):
        stan = self.m.checkState("111", [0])
        self.sprawdzStan(stan, [0],[0,0,1],"111","011")

    def testStan111_1(self):
        stan = self.m.checkState("111", [1])
        self.sprawdzStan(stan, [1],[1,1,0],"111","111")

    def testStanPoczatkowy(self):
        stan = self.m.getStanPoczatkowy()
        self.assertEqual('000', stan)

class TestMaszynyStanow3(unittest.TestCase):
    def setUp(self):
        # wiele inputow
        odczepy = [[1,4,6,8],
                   [0,2,4],
                   [2,3,5,7],
                   [1,5,6,8]]
        r = RejestrPrzesuwny(9, odczepy)
        self.m = MaszynaStanow(r,3)

    def testListyStanow(self):
        stany = self.m.getListaStanow()
        self.assertEqual(64, len(stany))

    def testDlugosc(self):
        self.assertEqual(64, self.m.getNumberOfStates())

    def sprawdzStan(self, stan, expIn, expOut, expInSt, expOutSt):
        self.assertEqual(expIn, stan['in'])
        self.assertEqual(expOut, stan['out'])
        self.assertEqual(expInSt, stan['inState'])
        self.assertEqual(expOutSt, stan['outState'])

    def testStan000110_110(self):
        stan = self.m.checkState("000110", [1,1,0])
        self.sprawdzStan(stan, [1,1,0],[0,1,1,0],"000110", "110000")

    def testStan110000_001(self):
        stan = self.m.checkState("110000", [0,0,1])
        self.sprawdzStan(stan, [0,0,1],[1,0,0,0],"110000", "001110")

    def testStan100101_010(self):
        stan = self.m.checkState("100101", [0,1,0])
        self.sprawdzStan(stan, [0,1,0],[1,0,1,1],"100101", "010100")

    def testStan110111_010(self):
        stan = self.m.checkState("110111", [0,1,0])
        self.sprawdzStan(stan, [0,1,0],[0,1,0,1],"110111", "010110")

    def testStan001000_000(self):
        stan = self.m.checkState("001000", [0,0,0])
        self.sprawdzStan(stan, [0,0,0],[0,0,1,1],"001000", "000001")

    def testStan111010_100(self):
        stan = self.m.checkState("111010", [1,0,0])
        self.sprawdzStan(stan, [1,0,0],[1,0,1,1],"111010", "100111")

# moze nie dzialac co iles iteracji, albo na pewnych srodowiskach - kolejnosc dodawabua do stanow
    def testPrzejscia000110(self):
        stany = self.m.getMozliwePrzejscia("000110")
        self.assertEqual(8, len(stany))
        stan = stany[6]
        self.sprawdzStan(stan, [1,1,0],[0,1,1,0],"000110", "110000")

    def testStanPoczatkowy(self):
        stan = self.m.getStanPoczatkowy()
        self.assertEqual('000000', stan)


class TestMaszynyStanowRejestruSystematyczego(unittest.TestCase):
    def setUp(self):
        r = RejestrSystematyczny(3, [[0,2]], [0,1,2])
        self.m = MaszynaStanow(r,1)

    def test(self):
        self.fail("to do")

if __name__ == '__main__':
    unittest.main()
