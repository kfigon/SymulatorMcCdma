import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy as np
import math


dane = [1,0,1,1,0,1,0,1]
bipolar = lambda x: 1 if x==0 else -1

