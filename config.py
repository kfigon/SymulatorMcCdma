import json
from rejestrPrzesuwny import RejestrSystematyczny
from przeplot import Przeplatacz
import koderTurbo
import modulator

def budujKonfiguracje(jsonString=None):
    if jsonString is None:
        return [Konfiguracja()]

    readJsonDict = json.load(jsonString)
    konfigi = []
    for cfg in readJsonDict:
        konfigi.append(Konfiguracja(cfg))
    return konfigi

class Konfiguracja:
    def __init__(self, jsonDict=None):
        self.jsonDict = self.__getDefaultDict()

        if jsonDict:
            for k,v in jsonDict.items():
                self.jsonDict[k]=v

    def read(self, pole):
        return self.jsonDict[pole]

    def write(self, pole, val):
        self.jsonDict[pole] = val

    def __getDefaultDict(self):
        return {
            'tytul': "Domyslna konfiguracja",
            
            'ileBitow': 100,
            'ileStrumieni':5,
            'tylkoPrzebiegiCzasowe':False,
            'dlugoscKoduWalsha': 64,
            'numerKoduWalsha':2,
            
            'minSnr': -10,
            'maxSnr': 1,
            'modulacja': 'QPSK',
            
            'koder': True,
            'ileIteracjiDekodera': 10,
            'dlugoscPrzeplotu': 10,
            'koder1': {
                'ileKomorekRejestru': 3,
                'odczepy': [[0,2]],
                'odczepySprzezenia': [1,2],
            },
            'koder2': {
                'ileKomorekRejestru': 3,
                'odczepy': [[0,2]],
                'odczepySprzezenia': [1,2],
            }
        }

    def getSrnTab(self):
        return [snr for snr in range(self.read('minSnr'), self.read('maxSnr'))]
    
    def __str__(self):
        out = "konfiguracja:\n\n"
        for k,v in self.jsonDict.items():
            out += k + ":\t" + str(v) + '\n'
        return out

    def stworzModulator(self):
        mod = self.read('modulacja')
        if mod == 'BPSK':
            return modulator.Bpsk()
        else:
            return modulator.Qpsk()

    def __budujRejestrSystematyczny(self, k):
            return RejestrSystematyczny(k['ileKomorekRejestru'], 
                    k['odczepy'],
                    k['odczepySprzezenia'])
        
    def budujKoder(self):
        if self.read('koder'):
        
            k1 = self.read('koder1')
            k2 = self.read('koder1')
            rej1 = self.__budujRejestrSystematyczny(k1)
            rej2 = self.__budujRejestrSystematyczny(k2)
            przeplatacz = Przeplatacz(self.read('dlugoscPrzeplotu'))

            return koderTurbo.KoderTurbo(rej1, rej2, przeplatacz)
        else:
            return koderTurbo.Koder()

    # bpsk bez mcdma:
    # ilebitow=ileStrumieni, modulacja bpsk
    # qpsk: ilebitow * 2 =ileStrumieni 