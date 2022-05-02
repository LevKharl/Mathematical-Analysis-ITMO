import math
import matplotlib.pyplot as plt
import numpy as np
from jupyterthemes import jtplot

jtplot.style('gruvboxd')

print("введите количество точек разбиения:")
n = int(input())
print('Введите способ выбора оснащения: (l - left, r-right, c-central)')
osn = str(input())

a = 0
b = np.pi / 2
S = shift = 0
m = -10000

x = np.linspace(a, b, n)
delta_xi = math.pi / (2 * n)
y = [0.0] * n

if osn == 'l':
    shift = -delta_xi
elif osn == 'r':
    shift = delta_xi
elif osn == 'c':
    shift = 0
for i in range(len(x)):
    if osn == 'l' or osn == 'r':
        epsilon = np.abs(-2 * np.sin(2 * x[i])) * np.power((b - a), 2) / (2 * n)
    elif osn == 'c':
        epsilon = np.abs(-4 * np.cos(2 * x[i])) * np.power((b - a), 3) / (24 * np.power(n, 2))
    if epsilon > m:
        m = epsilon

for i in range(len(x)):
    y[i] = math.cos(2 * (x[i] + shift))
    S += y[i] * delta_xi
    print(S)
print('Итого, площадь под графиком функции cos(2x) равна: ', S)

plt.figure(figsize=(20, 10))
plt.xlabel(r'$x$', fontsize=18)
plt.ylabel(r'$cos (2x)$', fontsize=18)
plt.grid(False)
plt.plot(x, np.cos(2 * x), label='График функции cos (2x)', color='red', linewidth=8, marker=".", markerfacecolor='orange', markersize=20)
plt.legend(loc='best', fontsize=18)
plt.gca()
plt.bar(x, y, width=delta_xi, color='blue', align='center')
plt.show()

Rn = 0 - S
print('Проверка погрешности интеграла и его приближения')
if np.abs(Rn) <= np.abs(epsilon):
    print('|Rn| = ', np.abs(Rn), '<=', np.abs(epsilon), 'значит всё гуд')
else:
    print('|Rn| = ', np.abs(Rn), '>', np.abs(epsilon), 'не гуд')
