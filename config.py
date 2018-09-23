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
            'ileBitow':90,
            'ileStrumieni':5,
            'ileIteracji':1,
            'tylkoPrzebiegiCzasowe':False,
            'dlugoscKoduWalsha': 64,
            'numerKoduWalsha':2
        }

    def __str__(self):
        out = "konfiguracja:\n\n"
        for k,v in self.jsonDict.items():
            out += k + ":\t" + str(v) + '\n'
        return out