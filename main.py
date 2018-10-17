import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import random
from transmiterOfdm import TransmiterOfdm
from przetwornikSP import PrzetwornikSzeregowoRownolegly
from koderTurbo import KoderTurbo, budujDomyslnyKoder, budujBrakKodowania
import utils
from rozpraszaczWidma import RozpraszaczBipolarny
from generatorKoduWalsha import GeneratorKoduWalsha
from config import Konfiguracja
from modulator import Qpsk, Bpsk

def stworzModulator(konfiguracja):
    mod = konfiguracja.read('modulacja')
    if mod == 'BPSK':
        return Bpsk()
    else:
        return Qpsk()

def budujKoder(konfiguracja):
    if konfiguracja.read('koder'):
        return budujDomyslnyKoder()
    else:
        return budujBrakKodowania()

def main(konfiguracja, snr):

    daneBinarne = utils.generujDaneBinarne(konfiguracja.read('ileBitow'))
    
    koder = budujKoder(konfiguracja)
    bityZakodowane = koder.kodujE2E(daneBinarne)

    modulator = stworzModulator(konfiguracja)
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
    bityOdebrane = modulator.demapuj(zdemodulowane)
    eb,n0 = utils.liczEbN0(nadany, snr)

    zdekodowane = koder.dekoduj(bityOdebrane, ileItracji=konfiguracja.read('ileIteracjiDekodera'), lc = eb/n0)

    ileBledow = 0
    assert len(zdekodowane) == len(daneBinarne)
    for z,d in zip(zdekodowane, daneBinarne):
        if z != d:
            ileBledow +=1

    return ileBledow/len(daneBinarne)
    

konfiguracja = Konfiguracja()
# json do pliku config.json
print(konfiguracja)

minSnr = konfiguracja.read('minSnr')
maxSnr = konfiguracja.read('maxSnr')

snrTab=[snr for snr in range(minSnr, maxSnr)]
wyniki=[]
for snr in snrTab:
    ber = main(konfiguracja, snr)
        
    if not konfiguracja.read('tylkoPrzebiegiCzasowe'):
        print("snr %d, ile bledow: %f" % (snr, ber))
    
    wyniki.append(ber)

if not konfiguracja.read('tylkoPrzebiegiCzasowe'):
    plt.semilogy(snrTab, wyniki)
    plt.grid(True)
    plt.show()