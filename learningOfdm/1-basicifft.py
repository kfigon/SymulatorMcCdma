import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np

probkiCzestotliwosci = [0 for _ in range(100)]

# probkiCzestotliwosci[0] = 1 skladowa stala
# wartosc x -> amplituda = x/dlugosc
probkiCzestotliwosci[2] = 1  # im wieksza liczba, tym gestszy sinus

sinusy = fft.ifft(probkiCzestotliwosci)

plt.subplot(2,1,1)
plt.plot(np.real(sinusy))

plt.subplot(2,1,2)
plt.plot(np.imag(sinusy))
plt.show()