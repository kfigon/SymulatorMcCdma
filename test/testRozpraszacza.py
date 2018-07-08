import unittest
from rozpraszaczWidma import RozpraszaczWidma


class TestRozpraszacza(unittest.TestCase):
    def testOk(self):
        r = RozpraszaczWidma(3) #3 chipy na bit
        bity = [1,0,0,1]
        ciagRozpraszajacy = [1,1,1,0,0,1,0,0,1,0,0,0]
        exp=[0,0,0, 0,0,1, 0,0,1, 1,1,1]
        self.assertEqual(exp, list(r.rozpraszaj(bity, ciagRozpraszajacy)))

    def testKrotszeDane(self):
        r = RozpraszaczWidma(3)
        bity = [1,0]
        ciagRozpraszajacy = [1,1,1,0,0,1,0,0,1,0,0]
        exp = [0,0,0, 0,0,1]
        self.assertEqual(exp, list(r.rozpraszaj(bity, ciagRozpraszajacy)))

    def testDluzszeDane(self):
        r = RozpraszaczWidma(3)
        bity = [1,0,1]
        ciagRozpraszajacy = [1,1,1,0,0,1]
        exp = [0,0,0, 0,0,1, 0,0,0]
        self.assertEqual(exp, list(r.rozpraszaj(bity, ciagRozpraszajacy)))
    
    def testNotAligned(self):
        r = RozpraszaczWidma(3)
        bity = [1,0,1]
        ciagRozpraszajacy = [1,1,1,0,0,1,0]
        exp = [0,0,0, 0,0,1, 1,0,0]
        self.assertEqual(exp, list(r.rozpraszaj(bity, ciagRozpraszajacy)))

if __name__ == '__main__':
    unittest.main()