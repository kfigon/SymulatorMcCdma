import unittest
from rozpraszaczWidma import RozpraszaczWidma


class TestRozpraszacza(unittest.TestCase):
    def test1(self):
        r = RozpraszaczWidma(3) #3 chipy na bit
        bity = [1,0,0,1]
        ciagRozpraszajacy = [1,1,1,0,0,1,0,0,1,0,0,0]
        exp=[0,0,0, 0,0,1, 0,0,1, 1,1,1]
        self.assertEqual(exp, list(r.rozpraszaj(bity, ciagRozpraszajacy)))

    def test2(self):
        r = RozpraszaczWidma(3) #3 chipy na bit
        bity = [1,0,0,1]
        ciagRozpraszajacy = [1,1,1,0,0,1,0,0,1,0,0]
        with self.assertRaises(Exception):
            r.rozpraszaj(bity,ciagRozpraszajacy)

if __name__ == '__main__':
    unittest.main()