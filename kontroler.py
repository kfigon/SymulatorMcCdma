import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import random
from transmiterOfdm import TransmiterOfdm
from przetwornikSP import PrzetwornikSzeregowoRownolegly
import utils
from rozpraszaczWidma import RozpraszaczBipolarny
from generatorKoduWalsha import GeneratorKoduWalsha
from config import Konfiguracja, budujKonfiguracje
from modulator import Qpsk, Bpsk

def main(konfiguracja, snr):

    daneBinarne = utils.generujDaneBinarne(konfiguracja.read('ileBitow'))
    
    koder = konfiguracja.budujKoder()
    bityZakodowane = koder.kodujE2E(daneBinarne)

    modulator = konfiguracja.stworzModulator()
    symboleBipolarne = modulator.mapuj(bityZakodowane)

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
        
    if konfiguracja.read('tylkoPrzebiegiCzasowe') == True:
        plt.subplot(2,1,1)
        plt.plot(np.real(nadany))
        # plt.plot(np.real(rozproszony))
        plt.subplot(2,1,2)
        plt.plot(np.abs(fft.fft(nadany[:len(nadany)//2])))
        # plt.plot(np.abs(fft.fft(rozproszony[:len(rozproszony)//2])))
        plt.show()
        return

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

    # dekodowanie
    bityOdebrane = modulator.demapuj(zdemodulowane)
    eb,n0 = utils.liczEbN0(nadany, snr)

    zdekodowane = koder.dekoduj(bityOdebrane, ileItracji=konfiguracja.read('ileIteracjiDekodera'), lc = eb/n0)

    ileBledow = 0
    assert len(zdekodowane) == len(daneBinarne)
    for z,d in zip(zdekodowane, daneBinarne):
        if z != d:
            ileBledow +=1

    return ileBledow/len(daneBinarne)
    
def iteracjaDlaKonfiga(konfiguracja):
    print(konfiguracja)

    snrTab = konfiguracja.getSrnTab()
    wyniki=[]
    for snr in snrTab:
        ber = main(konfiguracja, snr)

        if konfiguracja.read('tylkoPrzebiegiCzasowe') == False:
            print("snr %d, ile bledow: %f" % (snr, ber))
        
        wyniki.append(ber)
    return snrTab, wyniki
