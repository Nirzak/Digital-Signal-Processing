import numpy as np

x = [0,1,2,3]
N = len(x)

X = [0+0j,0+0j,0+0j,0+0j]

def dft(x,N):
    for K in range(N):
        temp = 0+0j
        for n in range(N):
            temp = temp+x[n]*np.exp(-2j*np.pi*n*K/N)
        X[K] = np.round(temp)
    return
dft(x,N)
print('Discrete Fourier Transform of x =',X)