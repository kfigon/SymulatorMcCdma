import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import random
from transmiterOfdm import TransmiterOfdm
from przetwornikSP import PrzetwornikSzeregowoRownolegly
from koderTurbo import KoderTurbo, budujDomyslnyKoder
import utils
from rozpraszaczWidma import RozpraszaczBipolarny
from generatorKoduWalsha import GeneratorKoduWalsha
from config import Konfiguracja


def main(konfiguracja, snr):

    daneBinarne = utils.generujDaneBinarne(konfiguracja.read('ileBitow'))
    for _ in range(10):
        daneBinarne.append(0)

    koder = budujDomyslnyKoder()
    bityZakodowane = koder.koduj(daneBinarne)
    bityZakodowane = koder.combine(bityZakodowane[0], bityZakodowane[1], bityZakodowane[2])

    symboleBipolarne = utils.generujQpskZBitow(bityZakodowane)

    pSP = PrzetwornikSzeregowoRownolegly(konfiguracja.read('ileStrumieni'))
    strumienie = pSP.rozdziel(symboleBipolarne)
    
    generatorKoduWalsha = GeneratorKoduWalsha(konfiguracja.read('dlugoscKoduWalsha'))
    ciagRozpraszajacy = generatorKoduWalsha.generuj(konfiguracja.read('numerKoduWalsha'))
    
    transmiter = TransmiterOfdm()

    nadany = []
    for i, strumien in enumerate(strumienie):
        
        zmodulowanyStrumien = transmiter.modulujStrumien(strumien)
        rozpraszaczWidma = RozpraszaczBipolarny()
        chip = ciagRozpraszajacy[i]
        rozproszony = rozpraszaczWidma.rozpraszajBipolarne(zmodulowanyStrumien, [chip])

# zmienic na zmodulowanyStrumien jesli ma byc bez SS. i wyrzucic z demodulatora skupianie
        for x in rozproszony:
            nadany.append(x)
        
    if konfiguracja.read('tylkoPrzebiegiCzasowe'):
        plt.subplot(2,1,1)
        plt.plot(np.real(nadany))
        # plt.plot(np.real(rozproszony))
        plt.subplot(2,1,2)
        plt.plot(np.abs(fft.fft(nadany[:len(nadany)//2])))
        # plt.plot(np.abs(fft.fft(rozproszony[:len(rozproszony)//2])))
        plt.show()
        return

    # odebrane = nadany
    odebrane = utils.awgn(nadany, snr)

    odebraneStrumienie = pSP.rozdziel(odebrane)
    zdemodulowaneStrumienie = []
    zdemodulowane=[]

    for i, strumien in enumerate(odebraneStrumienie):
        rozpraszaczWidma = RozpraszaczBipolarny()
        chip = ciagRozpraszajacy[i]
        skupiony = rozpraszaczWidma.skupBipolarne(strumien, [chip])

        zdemodulowanyStrumien = transmiter.demoduluj(skupiony)
        zdemodulowaneStrumienie.append(zdemodulowanyStrumien)
        zdemodulowane += zdemodulowanyStrumien

    # for i in range(len(strumienie)):
    #     assert zdemodulowaneStrumienie[i] == strumienie[i]
    # assert symboleBipolarne == zdemodulowane


    # dekodowanie
    bityOdebrane = utils.demodulujQpsk(zdemodulowane)
    # assert bityZakodowane == bityOdebrane
    zdekodowane = koder.dekoduj(bityOdebrane, ileItracji=10)

    ileBledow = 0
    assert len(zdekodowane) == len(daneBinarne)
    for z,d in zip(zdekodowane, daneBinarne):
        if z != d:
            ileBledow +=1


    ber =  100*ileBledow/len(daneBinarne)
    return ber
    



konfiguracja = Konfiguracja()
snr = 20
# todo - snr do dekodowania map?
# json do pliku config.json
print(konfiguracja)

for i in range(konfiguracja.read('ileIteracji')):
    ber = main(konfiguracja, snr)
    
    if not konfiguracja.read('tylkoPrzebiegiCzasowe'):
        print("ile bledow: " + str(ber) + "%")
