import unittest
import math

class Sygnal:
    def __init__(self, dataTab, samplingFrequency):
        self.__tab = dataTab
        self__fs = samplingFrequency

    def get(self, idx):
        return self.__tab[idx]
    def set(self, idx, val):
        self.__tab[idx] = val
    def getLen(self):
        return len(self.__tab)
    
    def getSampligFreq(self):
        return self.__fs
        
class Kanal:
    def __init__(self, parm):
        self.__parm = parm
    def przepusc(self, sygnal):
        pass

class GeneratorKodow:
    def generujWalsha(self, numer):
        pass
    
class McCdma:
    def rozprosz(self, daneBinarne):
        pass
    def skup(self, sygnalZmodulowany):
        pass

# parametry
class TurboKoder:
    def koduj(self, daneBinarne):
        pass
    def dekoduj(self, daneBinarne):
        pass

    # dzieli na 2, zwraca tuple: Lewy, Prawy.
    # Lewy moze miec wiekszy rozmiar gdy nieparzyste
    def split(self, daneBinarne):
        leftLen = math.ceil(len(daneBinarne)/2)
        rightLen = len(daneBinarne) - leftLen
        left = [0] * leftLen
        right = [0] * rightLen

        iL = 0
        iR = 0
        i = 0
        while(i < len(daneBinarne)):
            if(iL < leftLen):
                left[iL] = daneBinarne[i]
                iL+=1
                i+=1
            if(iR < rightLen):
                right[iR] = daneBinarne[i]
                iR+=1
                i+=1
            
        return left, right


class TestTurboKodera(unittest.TestCase):
    def setUp(self):
        self.k = TurboKoder()
        
    def test1(self):
        dane = [1,1,1,0,1,0,1,1,0,0]
        exp = []
        self.assertEqual(exp, self.k.koduj(dane))

    def testSplittera1(self):
        dane = [1,1,1,0,1,0,1,1,0,1]
        expL = [1,1,1,1,0]
        expR = [1,0,0,1,1]
        resL, resR = self.k.split(dane)
        self.assertEqual(expL, resL)
        self.assertEqual(expR, resR)

    def testSplittera2(self):
        dane = [1,1,1,0,1,1,1,0,1]
        expL = [1,1,1,1,1]
        expR = [1,0,1,0]
        resL, resR = self.k.split(dane)
        self.assertEqual(expL, resL)
        self.assertEqual(expR, resR)

class KoderSplotowy:
    def koduj(self, daneBinarne):
        pass

class TestKoderaSplotowego(unittest.TestCase):
    def setUp(self):
        self.k = KoderSplotowy()

    def test1(self):
        dane = [1,1,1,0,1,0,1,1,0,0]
        exp = []
        self.assertEqual(exp, self.k.koduj(dane))
        
if __name__ == '__main__':
    unittest.main()
