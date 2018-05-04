from modulatorQpsk import Qpsk

import utils
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack

def wykresQpsk():
    dane = utils.generujDaneBinarne(20)
    fp = 50
    fn= 3
    fb =5
    qpsk = Qpsk(fp, fn,fb)
    modulowany = qpsk.moduluj(dane)
    zdemodulowany = qpsk.demodulacja(modulowany)
    print(dane)
    print(zdemodulowany)
    assert(dane == zdemodulowany)

    plt.subplot(3,1,1)
    plt.stem(dane)
    plt.subplot(3, 1, 2)
    plt.plot(modulowany)
    
    plt.subplot(3,1,3)
    plt.stem(zdemodulowany)
    plt.show()

    #cz sygnalu = Fs/dlugosc * nrProbki z pikiem
    fourier = scipy.fftpack.fft(modulowany)
    plt.subplot(2,1,1)
    plt.stem(np.abs(fourier))

    plt.subplot(2,1,2)
    plt.stem(np.angle(fourier))
    plt.show()

wykresQpsk()
