import numpy as np

#x = eval(input('Enter the input sequence x[n]='))
x = [1, 2, 3, 4, 5]
N1 = len(x)
#h = eval(input('Enter the input sequence h[n]='))
h = [1, 2, 3, 3, 2, 1]
N2 = len(h)
N = N1 + N2 - 1
y = np.zeros(N)
for i in range(N2):
    h[N2 - 1 - i] = h[i]

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

print('Cross-Correlation of Two Signals =', y.astype('int'))