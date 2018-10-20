from config import *
from kontroler import *

if __name__ == '__main__':
    sciezka = r'C:\Users\JIT\Desktop\repo\skrypty\konf.json'
    with open(sciezka, 'r') as plik:

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
