from modulatorQpsk import Qpsk, WalidatorPredkosciSygnalow
from rozpraszaczWidma import RozpraszaczWidma
from generatorKoduWalsha import GeneratorKoduWalsha

import utils
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack

def aplikujKod(zmodulowany, ciag):
    i = 0
    out = []
    for d in zmodulowany:
        asd = d * utils.bipolar(ciag[i])
        i+=1
        out.append(asd)
        if(i >= len(ciag)):
            i = 0
    return out


def wykresCdma():
    dane = utils.generujDaneBinarne(10)

    x = 10
    rozpraszacz = RozpraszaczWidma(x)

    fp = 200
    fn= 5
    fb =1
    if not WalidatorPredkosciSygnalow.waliduj(fn, fb, fp):
        print("Niewlasciwe predkosci probkowania")
        return

    qpsk = Qpsk(fp, fn,fb)
    zmodulowany = qpsk.moduluj(dane)
    ciagRozpraszajacy = list(rozpraszacz.rozpraszaj(dane, GeneratorKoduWalsha(5).generuj(3)))

    rozproszony = aplikujKod(zmodulowany, ciagRozpraszajacy)
    skupiony = aplikujKod(rozproszony, ciagRozpraszajacy)

    zdemodulowany = qpsk.demodulacja(skupiony)
    print(dane)
    print(zdemodulowany)
    assert(dane == zdemodulowany)

    plt.subplot(2,1,1)
    plt.title("QPSK")
    plt.plot(zmodulowany)
    
    plt.subplot(2, 1, 2)
    plt.title("Rozproszony QPSK")
    plt.plot(rozproszony)
    plt.show()

    zwyklyFft=scipy.fftpack.fft(zmodulowany)
    rozpFft = scipy.fftpack.fft(rozproszony)

    plt.figure(1)
    plt.title('Fourier')
    plt.plot(np.abs(zwyklyFft[:len(zwyklyFft)//2]), label='zmodulowany')
    plt.plot(np.abs(rozpFft[:len(rozpFft)//2]), label='rozproszony')
    plt.legend()
    plt.show()

wykresCdma()
