import unittest
from rejestrPrzesuwny import RejestrPrzesuwny
from maszynaStanow import MaszynaStanow


class TestMaszynyStanow(unittest.TestCase):
    def setUp(self):
        odczepy = [[0,1,2], [1,2]]
        r = RejestrPrzesuwny(3, odczepy)
        self.m = MaszynaStanow(r,1)

    def testDlugosc(self):
        self.assertEqual(4, self.m.getNumberOfStates())

    def sprawdzajStan(self, stan, expIn, expOut, expInSt, expOutSt):
        self.assertEqual(expIn, stan['in'])
        self.assertEqual(expOut, stan['out'])
        self.assertEqual(expInSt, stan['inState'])
        self.assertEqual(expOutSt, stan['outState'])

    def testStan00_0(self):
        stan = self.m.checkState("00", [0])
        self.sprawdzajStan(stan, [0], [0,0], "00", "00")

    def testStan00_1(self):
        stan = self.m.checkState("00", [1])
        self.sprawdzajStan(stan, [1], [1,0], "00", "10")

    def testStan01_0(self):
        stan = self.m.checkState("01", [0])
        self.sprawdzajStan(stan, [0], [1,1], "01", "00")

    def testStan01_1(self):
        stan = self.m.checkState("01", [1])
        self.assertEqual([1], stan['in'])
        self.assertEqual([0,1], stan['out'])
        self.assertEqual("01", stan['inState'])
        self.assertEqual("10", stan['outState'])

    def testStan10_0(self):
        stan = self.m.checkState("10", [0])
        self.sprawdzajStan(stan, [0], [1,1], "10", "01")

    def testStan10_1(self):
        stan = self.m.checkState("10", [1])
        self.sprawdzajStan(stan, [1], [0,1], "10", "11")

    def testStan11_0(self):
        stan = self.m.checkState("11", [0])
        self.sprawdzajStan(stan, [0], [0,0], "11", "01")

    def testStan11_1(self):
        stan = self.m.checkState("11", [1])
        self.sprawdzajStan(stan, [1], [1,0], "11", "11")

    def testPrzejscStanow00(self):
        stany = self.m.getMozliwePrzejscia('00')
        self.assertEqual(2, len(stany))
        self.assertEqual("00", stany[0]['inState'])
        self.assertEqual("00", stany[0]['outState'])
        self.assertEqual([0], stany[0]['in'])
        self.assertEqual([0,0], stany[0]['out'])

        self.assertEqual("00", stany[1]['inState'])
        self.assertEqual("10", stany[1]['outState'])
        self.assertEqual([1], stany[1]['in'])
        self.assertEqual([1,0], stany[1]['out'])

    def testPrzejscStanow01(self):
        stany = self.m.getMozliwePrzejscia('01')
        self.assertEqual(2, len(stany))
        self.assertEqual("01", stany[0]['inState'])
        self.assertEqual("00", stany[0]['outState'])
        self.assertEqual([0], stany[0]['in'])
        self.assertEqual([1,1], stany[0]['out'])

        self.assertEqual("01", stany[1]['inState'])
        self.assertEqual("10", stany[1]['outState'])
        self.assertEqual([1], stany[1]['in'])
        self.assertEqual([0,1], stany[1]['out'])

    def testDojsciaDo00(self):
        stany = self.m.getMozliweDojscia('00')
        self.assertEqual(2, len(stany))
        self.assertEqual("00", stany[0]['inState'])
        self.assertEqual("00", stany[0]['outState'])
        self.assertEqual([0], stany[0]['in'])
        self.assertEqual([0,0], stany[0]['out'])

        self.assertEqual([0], stany[1]['in'])
        self.assertEqual([1,1], stany[1]['out'])
        self.assertEqual("01", stany[1]['inState'])
        self.assertEqual("00", stany[1]['outState'])

    def testDojsciaDo01(self):
        stany = self.m.getMozliweDojscia('01')
        self.assertEqual(2, len(stany))
        
        self.assertEqual([0], stany[1]['in'])
        self.assertEqual([0,0], stany[1]['out'])
        self.assertEqual("11", stany[1]['inState'])
        self.assertEqual("01", stany[1]['outState'])

        self.assertEqual([0], stany[0]['in'])
        self.assertEqual([1,1], stany[0]['out'])
        self.assertEqual("10", stany[0]['inState'])
        self.assertEqual("01", stany[0]['outState'])

    def testDojsciaDo10(self):
        stany = self.m.getMozliweDojscia('10')
        self.assertEqual(2, len(stany))

        self.assertEqual([1], stany[0]['in'])
        self.assertEqual([1,0], stany[0]['out'])
        self.assertEqual("00", stany[0]['inState'])
        self.assertEqual("10", stany[0]['outState'])
        
        self.assertEqual([1], stany[1]['in'])
        self.assertEqual([0,1], stany[1]['out'])
        self.assertEqual("01", stany[1]['inState'])
        self.assertEqual("10", stany[1]['outState'])

    def testDojsciaDo11(self):
        stany = self.m.getMozliweDojscia('11')
        self.assertEqual(2, len(stany))

        self.assertEqual([1], stany[0]['in'])
        self.assertEqual([0,1], stany[0]['out'])
        self.assertEqual("10", stany[0]['inState'])
        self.assertEqual("11", stany[0]['outState'])

        self.assertEqual([1], stany[1]['in'])
        self.assertEqual([1,0], stany[1]['out'])
        self.assertEqual("11", stany[1]['inState'])
        self.assertEqual("11", stany[1]['outState'])
        
class TestMaszynyStanow2(unittest.TestCase):
    def setUp(self):
        #inne odczepy
        odczepy = [[0,2,3], [0,1,3], [0,2]]
        r = RejestrPrzesuwny(4, odczepy)
        self.m = MaszynaStanow(r,1)

    def testDlugosc(self):
        self.assertEqual(8, self.m.getNumberOfStates())

    def testStan000_0(self):
        stan = self.m.checkState("000", [0])
        self.sprawdzajStan(stan, [0], [0,0,0], "000", "000")

    def testStan000_1(self):
        stan = self.m.checkState("000", [1])
        self.sprawdzajStan(stan, [1], [1,1,1], "000", "100")

    def testStan001_0(self):
        stan = self.m.checkState("001", [0])
        self.sprawdzajStan(stan, [0], [1,1,0], "001", "000")

    def testStan001_1(self):
        stan = self.m.checkState("001", [1])
        self.sprawdzajStan(stan, [1], [0,0,1], "001", "100")

    def testStan010_0(self):
        stan = self.m.checkState("010", [0])
        self.sprawdzajStan(stan, [0], [1,0,1], "010", "001")

    def testStan010_1(self):
        stan = self.m.checkState("010", [1])
        self.sprawdzajStan(stan, [1], [0,1,0], "010", "101")

    def testStan011_0(self):
        stan = self.m.checkState("011", [0])
        self.sprawdzajStan(stan, [0], [0,1,1], "011", "001")

    def testStan011_1(self):
        stan = self.m.checkState("011", [1])
        self.sprawdzajStan(stan, [1], [1,0,0], "011", "101")

    def testStan100_0(self):
        stan = self.m.checkState("100", [0])
        self.sprawdzajStan(stan, [0], [0,1,0], "100", "010")

    def testStan100_1(self):
        stan = self.m.checkState("100", [1])
        self.sprawdzajStan(stan, [1], [1,0,1], "100", "110")

    def testStan101_0(self):
        stan = self.m.checkState("101", [0])
        self.sprawdzajStan(stan, [0], [1,0,0], "101", "010")

    def testStan101_1(self):
        stan = self.m.checkState("101", [1])
        self.sprawdzajStan(stan, [1], [0,1,1], "101", "110")

    def testStan110_0(self):
        stan = self.m.checkState("110", [0])
        self.sprawdzajStan(stan, [0], [1,1,1], "110", "011")

    def testStan110_1(self):
        stan = self.m.checkState("110", [1])
        self.sprawdzajStan(stan, [1], [0,0,0], "110", "111")

    def testStan111_0(self):
        stan = self.m.checkState("111", [0])
        self.sprawdzajStan(stan, [0], [0,0,1], "111", "011")

    def testStan111_1(self):
        stan = self.m.checkState("111", [1])
        self.sprawdzajStan(stan, [1], [1,1,0], "111", "111")

class TestMaszynyStanow3(unittest.TestCase):
    def setUp(self):
        # wiele inputow
        odczepy = [[1,4,6,8],
                   [0,2,4],
                   [2,3,5,7],
                   [1,5,6,8]]
        r = RejestrPrzesuwny(9, odczepy)
        self.m = MaszynaStanow(r,3)

    def testDlugosc(self):
        self.assertEqual(64, self.m.getNumberOfStates())

    def testStan000110_110(self):
        stan = self.m.checkState("000110", [1,1,0])
        self.assertEqual([1,1,0], stan['in'])
        self.assertEqual([0,1,1,0], stan['out'])
        self.assertEqual("000110", stan['inState'])
        self.assertEqual("110000", stan['outState'])

    def testStan110000_001(self):
        stan = self.m.checkState("110000", [0,0,1])
        self.assertEqual([0,0,1], stan['in'])
        self.assertEqual([1,0,0,0], stan['out'])
        self.assertEqual("110000", stan['inState'])
        self.assertEqual("001110", stan['outState'])

    def testStan100101_010(self):
        stan = self.m.checkState("100101", [0,1,0])
        self.assertEqual([0,1,0], stan['in'])
        self.assertEqual([1,0,1,1], stan['out'])
        self.assertEqual("100101", stan['inState'])
        self.assertEqual("010100", stan['outState'])

    def testStan110111_010(self):
        stan = self.m.checkState("110111", [0,1,0])
        self.assertEqual([0,1,0], stan['in'])
        self.assertEqual([0,1,0,1], stan['out'])
        self.assertEqual("110111", stan['inState'])
        self.assertEqual("010110", stan['outState'])

    def testStan001000_000(self):
        stan = self.m.checkState("001000", [0,0,0])
        self.assertEqual([0,0,0], stan['in'])
        self.assertEqual([0,0,1,1], stan['out'])
        self.assertEqual("001000", stan['inState'])
        self.assertEqual("000001", stan['outState'])

    def testStan111010_100(self):
        stan = self.m.checkState("111010", [1,0,0])
        self.assertEqual([1,0,0], stan['in'])
        self.assertEqual([1,0,1,1], stan['out'])
        self.assertEqual("111010", stan['inState'])
        self.assertEqual("100111", stan['outState'])

    def testPrzejscia000110(self):
        stany = self.m.getMozliwePrzejscia("000110")
        self.assertEqual(8, len(stany))

        stan = None
        for s in stany:
            if(s['in'] == [1,1,0] and s['out'] == [0,1,1,0]):
                stan=s
                break

        self.assertIsNotNone(stan)
        self.assertEqual([1,1,0], stan['in'])
        self.assertEqual([0,1,1,0], stan['out'])
        self.assertEqual("000110", stan['inState'])
        self.assertEqual("110000", stan['outState'])
        
if __name__ == '__main__':
    unittest.main()
