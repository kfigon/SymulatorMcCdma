import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import random
from transmiterOfdm import TransmiterOfdm
from przetwornikSP import PrzetwornikSzeregowoRownolegly
from koderTurbo import *
import utils

def main():
    daneBinarne = utils.generujDaneBinarne(90)
    for _ in range(10):
        daneBinarne.append(0)

    koder = budujDomyslnyKoder()
    bityZakodowane = koder.koduj(daneBinarne)
    bityZakodowane = koder.combine(bityZakodowane[0], bityZakodowane[1], bityZakodowane[2])

    symboleBipolarne = utils.generujQpskZBitow(bityZakodowane)
    pSP = PrzetwornikSzeregowoRownolegly(5)
    strumienie = pSP.rozdziel(symboleBipolarne)

    transmiter = TransmiterOfdm()

    zmodulowany = []
    for strumien in strumienie:
        zmodulowanyStrumien = transmiter.modulujStrumien(strumien)
        for x in zmodulowanyStrumien:
            zmodulowany.append(x)


    # plt.subplot(2,1,1)
    # plt.plot(np.real(zmodulowany))

    # plt.subplot(2,1,2)
    # plt.plot(np.abs(fft.fft(zmodulowany[:len(zmodulowany)//2])))
    # plt.show()

    odebraneStrumienie = pSP.rozdziel(zmodulowany)
    zdemodulowaneStrumienie = []
    zdemodulowane=[]
    for strumien in odebraneStrumienie:
        zdemodulowanyStrumien = transmiter.demoduluj(strumien)
        zdemodulowaneStrumienie.append(zdemodulowanyStrumien)
        zdemodulowane += zdemodulowanyStrumien

    for i in range(len(strumienie)):
        assert zdemodulowaneStrumienie[i] == strumienie[i]

    assert symboleBipolarne == zdemodulowane


    # dekodowanie
    bityOdebrane = utils.demodulujQpsk(zdemodulowane)
    assert bityZakodowane == bityOdebrane
    zdekodowane = koder.dekoduj(bityOdebrane, ileItracji=10)

    ileBledow = 0
    assert len(zdekodowane) == len(daneBinarne)
    for z,d in zip(zdekodowane, daneBinarne):
        if z != d:
            ileBledow +=1


    ber =  ileBledow/len(daneBinarne)
    print("ile bledow: " + str(ber))



for i in range(20):
    main()