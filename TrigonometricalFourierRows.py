import matplotlib.pyplot as plt
from numpy import *
from jupyterthemes import jtplot

jtplot.style('gruvboxd')

variant = int(input("Введите вариант построения ряда Фурье:" + "\n1 - общий тригонометрический ряд Фурье"
                    + "\n2 - по синусам" + "\n3 - по косинусам" + "\n"))
x_begin = float(input("Введите координату начала отрезка: "))
x_end = float(input("Введите координату конца отрезка: "))
summation_limit = int(input("Введите предел суммирования по n: "))

x_func = arange(x_begin, x_end, 0.01)
y_func = []
y_fourier = []
if variant == 1:
    def f(x):
        return 1 + sin(x + pi / 2 * (x // (3 * pi / 2)))


    def f_fourier(x):
        result = 1 + 2 / (3 * pi)
        for n in range(1, summation_limit):
            result += ((12 * ((-1) ** n) * cos(4 / 3 * n * x)) + (16 * n * sin(4 / 3 * n * x))) / (
                    pi * (16 * n ** 2 - 9))
        return result


    for i in range(x_func.size):
        y_func.append(f(x_func[i]))
        y_fourier.append(f_fourier(x_func[i]))

    title = 'График частичной суммы Sn через общий тригонометрический ряд'
    legend = 'Приближение по Фурье'

if variant == 2:
    def f_odd(x):
        return ((-1) ** (x // (3 * pi / 2))) * (1 + sin(x))


    def f_fourier_sin(x):
        result = 0
        for n in range(1, summation_limit):
            result += (18 * ((-1) ** n - 1) + 8 * n ** 2) * sin(2 / 3 * n * x) / (pi * n * (4 * n ** 2 - 9))
        return result


    for i in range(x_func.size):
        y_func.append(f_odd(x_func[i]))
        y_fourier.append(f_fourier_sin(x_func[i]))

    legend = 'Приближение по синусам'
    title = 'График частичной суммы Sn по синусам'

if variant == 3:
    def f_even(x):
        return 1 + sin(x)


    def f_fourier_cos(x):
        result = 1 + 2 / (3 * pi)
        for n in range(1, summation_limit):
            result += (-12 * cos(2 / 3 * n * x) / (pi * (4 * n ** 2 - 9)))
        return result


    for i in range(x_func.size):
        y_func.append(f_even(x_func[i]))
        y_fourier.append(f_fourier_cos(x_func[i]))

    legend = 'Приближение по косинусам'
    title = 'График частичной суммы Sn по косинусам'

if (variant == 1) or (variant == 2) or (variant == 3):
    plt.figure(figsize=(20, 10))
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x_func, y_func, linewidth=0.75, color='red', linestyle='--')
    plt.plot(x_func, y_fourier, linewidth=1, color='orange')
    plt.legend([legend, 'Исходная функция'], loc='best', fontsize=18)
    plt.show()