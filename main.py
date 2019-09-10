from config import *
from kontroler import *
import sys

def main(plik=None):
    konfiguracje = budujKonfiguracje(plik)
    for konfiguracja in konfiguracje:
        ebn0Tab,wyniki = iteracjaDlaKonfiga(konfiguracja)
            
        if konfiguracja.read('tylkoPrzebiegiCzasowe') or konfiguracja.read('tylkoKonstelacje'):
            continue

        # labelki, osie, tytuly wykresow
        plt.semilogy(ebn0Tab, wyniki, label=konfiguracja.read('tytul'))

    if konfiguracja.read('tylkoPrzebiegiCzasowe') or konfiguracja.read('tylkoKonstelacje'):
        return

    plt.legend()
    plt.xlabel('Eb/N0 [dB]')
    plt.ylabel('BER')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        sciezka = sys.argv[1]

        with open(sciezka) as plik:
            main(plik.read())

    else:
        main()

        