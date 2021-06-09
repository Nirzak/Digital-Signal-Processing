import numpy as np

#Implementing DFT function
def dft(x):
    N = len(x)
    x = np.concatenate([x,[0]*(N - len(x))])
    n = np.arange(N)
    k = n.reshape((N, 1))
    temp = np.exp((-2j * np.pi * n * k) / N)
    dft_x = np.dot(temp, x)
    return dft_x

def fact(x):
    res = []
    for i in range(1, x+1):
        if x % i == 0:
            res.append(i)
    fact = res[len(res)//2]
    ans = x//fact
    return fact, ans

def dac_dft(x):
    N = len(x)
    L, M = fact(N)
    X = x.reshape((M, L)).T
    dft_x = np.apply_along_axis(dft, axis=1, arr=X)
    k = np.arange(M)
    n = (np.arange(L)).reshape((L, 1))
    temp = np.exp((-2j * np.pi * k * n) / N)
    y = dft_x * temp
    dft_ans = np.zeros(y.shape, dtype=np.complex64)
    for i in range(M):
        dft_ans[:, i] = dft(y[:, i])
    dft_ans = np.round(dft_ans)
    return dft_ans

x = np.array([0,1,2,3])
fft = dac_dft(x)
print("FFT of the signal = ", fft)