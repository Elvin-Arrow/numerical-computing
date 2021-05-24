from tabulate import tabulate


def f(x):
    return 0.2 + (25 * x) - (200 * x * x) + (675 * x * x * x) - \
        (900 * x * x * x * x) + (400 * x * x * x * x * x)


def trapm(h, n):
    temp = a
    sum = 0

    for i in range(1, n):
        temp += h
        sum = sum + f(temp)

    i = (b - a) * (f(a) + (2 * sum) + f(b)) / (2 * n)

    return round(i, 4)


def epsillon_a(estimate):
    percentage = ((val - estimate) / val) * 100
    return round(percentage, 2)


a = 0
b = 0.8
val = 1.640533
table = [['n', 'h', 'i', 'Et(%)']]

for n in range(2, 11):
    h = (a + b) / n
    i = trapm(h, n)

    table.append([n, round(h, 4), i, epsillon_a(i)])

print(tabulate(table))
