import scipy.fftpack as fft

def addPadding(dane, dopasowanie):
    dl = len(dane)*dopasowanie
    out = [0 for _ in range(dl)]
    for i in range(len(dane)):
        out[i+1] = dane[i]
    return out

class TransmiterOfdm:
    def __init__(self, mnoznikNyquista=10):
        self.__dopasowanieNyquista = mnoznikNyquista

    def modulujStrumien(self, strumienComplexBipolarny):
        '''strumienComplexBipolarny - bity, symbole zespolone z QPSK, dowolnie. 
        Jeden strumien szeregowy, ale zespolony'''
        daneZPaddingiem = addPadding(strumienComplexBipolarny, self.__dopasowanieNyquista)
        return fft.ifft(daneZPaddingiem)

    def __zaokragleniaBipolar(self, val):
        if (val < 0.0001 and val >= 0) or (val > -0.0001 and val <= 0):
            return 0
        if val > 0:
            return 1
        else:
            return -1

    def demoduluj(self, odebranyStrumien):
        '''demoduluje jeden strumien na symbole jak weszly'''
        probkiCzestotliwosci = fft.fft(odebranyStrumien)
        out = []
        for p in probkiCzestotliwosci:
            bi = self.__zaokragleniaBipolar(p.real)
            bq = self.__zaokragleniaBipolar(p.imag)
            if bi != 0 or bq != 0:
                out.append(complex(bi, bq))

        return out


