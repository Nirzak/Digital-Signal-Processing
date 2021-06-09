import numpy as np

x = [1,0,0,2]
#x = eval(input('Enter the input sequence x[n]='))
N1 = len(x)
h = np.zeros(N1)
N2 = len(x)
N = N1 + N2 - 1
y = np.zeros(N)
for i in range(N1):
    h[N1 - 1 - i] = x[i]

m = N - N1
n = N - N2
# Padding zeros to x and h to make their length to N
x = np.pad(x, (0, m), 'constant')
h = np.pad(h, (0, n), 'constant')

# correlation using formula
for n in range(N):
    for k in range(N):
        if n >= k:
            y[n] = y[n] + x[n - k] * h[k]

print('Auto-Correlation of signal x =', y.astype('int'))