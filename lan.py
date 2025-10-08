import numpy as np

n = int(input('enter number of data point: '))
x = np.zeros(n)
y = np.zeros(n)
print('enter data of x and y:')
for i in range(n):
    x[i] = float(input('x[' + str(i) + ']= '))
    y[i] = float(input('y[' + str(i) + ']= '))
xp = float(input('enter interpolation point: '))
yp = 0
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p *= (xp - x[j]) / (x[i] - x[j])
    yp += p * y[i]
print(f'\nInterpolated value at {xp} is {round(yp, 6)}')