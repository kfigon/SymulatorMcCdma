import json

class Konfiguracja:
    def __init__(self, jsonstr=None):
        self.jsonDict = self.__getDefaultDict()

        if jsonstr:
            readJsonDict = json.loads(jsonstr)
            for k,v in readJsonDict.items():
                self.jsonDict[k]=v

    def read(self, pole):
        return self.jsonDict[pole]

    def write(self, pole, val):
        self.jsonDict[pole] = val

    def __getDefaultDict(self):
        return {
            'ileBitow': 100,
            'ileStrumieni':5,
            'tylkoPrzebiegiCzasowe':False,
            'dlugoscKoduWalsha': 64,
            'numerKoduWalsha':2,
            'minSnr': -10,
            'maxSnr': 1,
            'ileIteracjiDekodera': 10,
            'modulacja': 'QPSK',
            'koder': True,
            'tytul': "tytul konfiguracji",
            'ileKomorekRejestru': 4,
            'odczepy': [[0,1,3],[0,1]],
            'odczepySprzezenia': [2,4]
        }

    def __str__(self):
        out = "konfiguracja:\n\n"
        for k,v in self.jsonDict.items():
            out += k + ":\t" + str(v) + '\n'
        return out

    # bpsk bez mcdma:
    # ilebitow=ileStrumieni, modulacja bpsk
    # qpsk: ilebitow * 2 =ileStrumieni 