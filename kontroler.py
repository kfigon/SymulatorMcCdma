import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
from transmiterOfdm import TransmiterOfdm
from przetwornikSP import PrzetwornikSzeregowoRownolegly
import utils
from rozpraszaczWidma import RozpraszaczBipolarny
from generatorKoduWalsha import GeneratorKoduWalsha
from math import log10
from decimal import *

def liczBer(konfiguracja, snr):

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
        plt.title(konfiguracja.read("tytul"))
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
    zdemodulowane=[]

    for i, strumien in enumerate(odebraneStrumienie):
        rozpraszaczWidma = RozpraszaczBipolarny()
        chip = ciagRozpraszajacy[i]
        skupiony = rozpraszaczWidma.skupBipolarne(strumien, [chip])

        zdemodulowanyStrumien = transmiter.demoduluj(skupiony)
        zdemodulowane += zdemodulowanyStrumien

    if konfiguracja.read('tylkoKonstelacje') == True:
        plt.title(konfiguracja.read("tytul"))
        re = [i.real for i in zdemodulowane]
        im = [i.imag for i in zdemodulowane]
        plt.xlim(left=-4, right=4)
        plt.ylim(bottom=-4, top=4)
        plt.scatter(re, im)
        plt.grid()
        plt.show()
        return (0,0)

    # dekodowanie
    bipolarneOdebrane = modulator.demapuj(zdemodulowane)
    eb,n0 = utils.liczEbN0(nadany, snr)

    zdekodowane = koder.dekoduj(bipolarneOdebrane, ileItracji=konfiguracja.read('ileIteracjiDekodera'), lc = eb/n0)

    ileBledow = 0
    assert len(zdekodowane) == len(daneBinarne)
    for z,d in zip(zdekodowane, daneBinarne):
        if z != d:
            ileBledow +=1
    ber = Decimal(ileBledow)/Decimal(len(bityZakodowane))
    return ber, 100*ber, 10*log10(eb/n0)
    
def iteracjaDlaKonfiga(konfiguracja):
    print(konfiguracja)

    snrTab = konfiguracja.getSrnTab()
    ebn0Tab = []
    wyniki=[]
    for snr in snrTab:
        ber,berProcent,ebn0 = liczBer(konfiguracja, snr)
        ebn0Tab.append(ebn0)

        if konfiguracja.read('tylkoPrzebiegiCzasowe') == False:
            print("snr {}, eb/n0 {}, ile bledow: {}, {}%".format(snr, ebn0, ber, berProcent))
        
        wyniki.append(ber)
    return ebn0Tab, wyniki
