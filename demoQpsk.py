from modulatorQpsk import Qpsk, WalidatorPredkosciSygnalow

import utils
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack

def wykresQpsk():
    dane = utils.generujDaneBinarne(10)
    fp = 60
    fn= 2
    fb =1
    if not WalidatorPredkosciSygnalow.waliduj(fn, fb, fp):
        print("Niewlasciwe predkosci probkowania")
        return

    qpsk = Qpsk(fp, fn,fb)
    modulowany = qpsk.moduluj(dane)
    zdemodulowany = qpsk.demodulacja(modulowany)
    print(dane)
    print(zdemodulowany)
    assert(dane == zdemodulowany)

    plt.subplot(3,1,1)
    plt.title("QPSK")
    plt.stem(dane)
    plt.subplot(3, 1, 2)
    plt.plot(modulowany)
    
    plt.subplot(3,1,3)
    plt.stem(zdemodulowany)
    plt.show()

    #cz sygnalu = Fs/dlugosc * nrProbki z pikiem
    fourier = scipy.fftpack.fft(modulowany)
    plt.subplot(2,1,1)
    plt.title("Fourier")
    plt.stem(np.abs(fourier))

    plt.subplot(2,1,2)
    plt.title("Fourier kat")
    plt.stem(np.angle(fourier))
    plt.show()

wykresQpsk()
