import numpy as np
import cmath

x = [0,1,2,3]
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
print('Discrete Fourier Transform of x[k] =\n',X)