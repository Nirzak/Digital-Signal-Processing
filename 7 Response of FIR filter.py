import numpy as np

#Implementing DFT function
def dft(x,N):
    x = np.concatenate([x,[0]*(N - len(x))])
    n = np.arange(N)
    k = n.reshape((N, 1))
    temp = np.exp((-2j * np.pi * n * k) / N)
    # print(twiddler_mat)

    dft_x = np.dot(temp, x)
    return dft_x

# Implementing idft function
def idft(X, N):
    k = np.arange(N)
    n = k.reshape((N, 1))
    temp = np.exp((2j * np.pi * k * n) / N)
    idft_x = (np.dot(temp, X)) / N
    idft_x = np.real(idft_x)
    return idft_x


def fir(x, h):
    N = len(x) + len(h) - 1
    dft_x = dft(x, N)
    dft_h = dft(h, N)
    mul = dft_x * dft_h

    inv = idft(mul, N)
    return np.round(inv)

x = np.array([1,4,4,2])
h = np.array([1,2,3])
FIR = fir(x,h)
print("Response of the FIR filter =", FIR.astype('int'))

