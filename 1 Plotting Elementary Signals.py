# importing libraries
import numpy as np
import matplotlib.pyplot as plt


# Plotting unit step signal
a = 2
n = np.arange(-10, 10, 1)
step = []
for unit in n:
    if unit < a:
        step.append(0)
    else:
        step.append(1)

#plotting graph
plt.stem(n, step)
plt.xlabel('n')
plt.ylabel('u[n]')
plt.title('Unit step Signal')
plt.show()


# Plotting Impulse Signal
a = 4
n = np.arange(-10, 10, 1)
#d = unit_impulse(a, n)
impulse = []
for unit in n:
    if unit == a:
        impulse.append(1)
    else:
        impulse.append(0)

#Plotting graph
plt.stem(n, impulse)
plt.xlabel('n')
plt.ylabel('d[n]')
plt.title('Impulse Signal')
plt.show()


# Plotting ramp signal
n = np.arange(-10, 10, 1)
ramp = []
for unit in n:
    if unit < 0:
        ramp.append(0)
    else:
        ramp.append(unit)
plt.stem(n, ramp)
plt.xlabel('n')
plt.ylabel('r[n]')
plt.title('Ramp Signal')
plt.show()


# Plotting Exponential Signal
a = 2
n = np.arange(-1, 1, 0.1)
expo = []
for unit in n:
    expo.append(np.exp(a * unit))
plt.stem(n, expo)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Exponential Signal')
plt.show()
