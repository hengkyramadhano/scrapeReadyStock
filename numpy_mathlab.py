import numpy as np

# Ukuran DFT yang diinginkan
N = 1024

# Data X yang akan dihitung DFT-nya
x = np.array([0,4,3,9,6,7,6,8])

# Hitung DFT menggunakan numpy.fft.fft
X = np.fft.fft(x, N)

print(X)