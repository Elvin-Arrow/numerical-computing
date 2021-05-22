from tabulate import tabulate


def f(x):
    return 0.2 + (25 * x) - (200 * x * x) + (675 * x * x * x) - \
        (900 * x * x * x * x) + (400 * x * x * x * x * x)


def trapm(h, n):
    sum = f(0)
    print(sum)
    for i in range(1, n):
        sum += 2 * f(i)

    sum += f(n)

    print(sum)

    i = h * (sum / 2)

    return i


a = 0
b = 0.8

table = [['n', 'h', 'i']]

for n in range(2, 11):
    h = (a + b) / n
    i = trapm(h, n)
    table.append([n, h, i])

print(tabulate(table))
