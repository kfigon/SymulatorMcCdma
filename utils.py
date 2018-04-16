from random import randint

# tablice
def odlegloscHamminga(daneA, daneB):
    assert (len(daneA) == len(daneB))
    roznica = 0
    for i in range(len(daneA)):
        if (daneA[i] != daneB[i]):
            roznica += 1
    return roznica

# podzialListy
def podziel(dane, ileNaRaz):
    assert (len(dane) % ileNaRaz == 0)
    out=[None]* (len(dane)//ileNaRaz)
    for i in range(len(out)):
        out[i] = dane[i*ileNaRaz: ((i+1)*ileNaRaz)]

    return out

def str2List(data):
    out = [0]*len(data)
    for i in range(len(data)):
        out[i]=int(data[i])
    return out

def generujDaneBinarne(ile):
    return list(generujDaneBinarneGen(ile))

def generujDaneBinarneGen(ile):
    '''
    generator
    '''
    for i in range(ile):
        yield randint(0,1)

def probkuj(dane, fp, fs):
    '''
    :param dane: dane binarne
    :param fp: cz. probkowania
    :param fs: cz. sygnalu
    :return:  sprobkowane dane
    '''
    return list(probkujGen(dane, fp, fs))

def probkujGen(dane, fp, fs):
    ileProbekNaBit = int(fp/fs)
    for b in dane:
        for _ in range(ileProbekNaBit):
            yield b

def getCzasTransmisji(ileBitow, fb):
    return int(ileBitow/fb)