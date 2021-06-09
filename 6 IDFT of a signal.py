import numpy as np
import cmath

x = [0,1,2,3]
t = np.array(x)
print("Original Signal = ", t)
N = len(x)

X = [0+0j,0+0j,0+0j,0+0j]
x_mag_res =  np.zeros(N)

def dft(x,N):
    for K in range(N):
        temp = 0+0j
        for n in range(N):
            temp = temp+x[n]*cmath.exp(-2*cmath.sqrt(-1)*cmath.pi*n*K/N)
        X[K] = temp
        x_mag_res[K] = abs(X[K])
    return;
dft(x,N)
print('DFT of the signal x =\n',X)

def idft(X, N):
    for n in range(N):
        temp = 0 + 0j
        for K in range(N):
            temp = temp + X[K] * cmath.exp(2 * cmath.sqrt(-1) * cmath.pi * n * K / N)
        x[n] = temp / N

    return;

idft(X, N)
x_n = np.real(x)
x_n = np.round(x_n, decimals=0)
print('IDFT of the signal x =', x_n.astype('int'))
assert x_n.all() == t.all() # Cheking if the output match with the original one.
