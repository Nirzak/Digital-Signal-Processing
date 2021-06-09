import numpy as np

# Implementing redix-fft function
def Rad_fft(x):
    N = len(x)
    if N<=1:
        return x
    e = Rad_fft(x[0::2])
    o = Rad_fft(x[1::2])
    fft_x = np.zeros(N).astype(np.complex64)
    for i in range(N//2):
        fft_x[i] = e[i] + np.exp((-2j * np.pi * i) / N) * o[i]
        fft_x[i + N // 2] = e[i] - np.exp((-2j * np.pi * i) / N) * o[i]

    return fft_x

x = [0,1,2,3,4,5,6,7]
print("N =", len(x))
fft = Rad_fft(x)
print("FFT of the given signal =\n", fft)