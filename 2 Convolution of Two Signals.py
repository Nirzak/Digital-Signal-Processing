import numpy as np

# impulse response
h = [1, 2, 3, 3, 2, 1]
# input response
x = [1, 2, 3, 4, 5]
N1 = len(x)
N2 = len(h)
N = N1 + N2 - 1
y = np.zeros(N)
m = N - N1
n = N - N2
# Padding zeros to x and h to make their length to N
x = np.pad(x, (0, m), 'constant')
h = np.pad(h, (0, n), 'constant')

# Linear convolution using convolution sum formula
for n in range(N):
    for k in range(N):
        if n >= k:
            y[n] = y[n] + x[n - k] * h[k]

print('Linear convolution of two signals =', y.astype('int'))