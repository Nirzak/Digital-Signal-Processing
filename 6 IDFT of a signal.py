import numpy as np

x = [0,1,2,3]
t = np.array(x)
print("Original Signal = ", t)
N = len(x)

X = [0+0j,0+0j,0+0j,0+0j]

#Implementing DFT to get the output to use for IDFT
def dft(x,N):
    for K in range(N):
        temp = 0+0j
        for n in range(N):
            temp = temp+x[n]*np.exp(-2j*np.pi*n*K/N)
        X[K] = np.round(temp)
    return
dft(x,N)
print('DFT of the signal x = ',X)

# Implementing idft function to compute IDFT of the sequence
def idft(X, N):
    for n in range(N):
        temp = 0 + 0j
        for K in range(N):
            temp = temp + X[K] * np.exp(2j * np.pi * n * K / N)
        x[n] = temp / N

    return

idft(X, N)
x_n = np.real(x)
x_n = np.round(x_n, decimals=0)
print('IDFT of the signal x =', x_n.astype('int'))

assert x_n.all() == t.all() # Cheking if the output match with the original one.
