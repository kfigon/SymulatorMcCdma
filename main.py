from config import *
from kontroler import *
import sys

def main(plik=None):
    konfiguracje = budujKonfiguracje(plik)
    for konfiguracja in konfiguracje:
        snrTab,wyniki = iteracjaDlaKonfiga(konfiguracja)
            
        if konfiguracja.read('tylkoPrzebiegiCzasowe') == True:
            continue

        # labelki, osie, tytuly wykresow
        plt.semilogy(snrTab, wyniki, label=konfiguracja.read('tytul'))

    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        sciezka = sys.argv[1]

        with open(sciezka) as plik:
            main(plik)

    else:
        main()

        