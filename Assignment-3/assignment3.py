import math


def f(x):
    # return 53.44 * (1 - math.exp(-0.18355 * x))
    # return 2 * math.pow(x, 3) - 11.7 * math.pow(x, 2) + 17.7 * x - 5
    # return (9.81 * x) * (1 - math.exp(-(150/x))) - 540
    # return -25 + 82 * x - 90 * math.pow(x, 2) + 44 * math.pow(x, 3) - 8 * math.pow(x, 4) + 0.7 * math.pow(x, 5)
    return math.exp(-x)


def f_prime(x):
    return 6 * math.pow(x, 2) - 23.4 * x + 17.7


# def c(a, b):
#     return b - (f(b) * (a - b)) / (f(a) - f(b))
    # return a - ((f(a) * (b-a)) / (f(b) - f(a)))

x = 0
for i in range(10):
    x1 = f(x)
    print("xi = {}\nxi+1 = {}\n".format(x, x1))
    x = x1

# print(f(0.5796))
# print(c(0.5, 0.5805))

# a = 55  # -ve
# b = 60  # +ve

# for i in range(10):
#     t1 = f(a)
#     t2 = f(b)
#     h = b - a

#     ci = c(a, b)
#     print("c = {}\n".format(ci))

#     if f(ci) == 0:
#         break
#     if f(ci) < 0:
#         a = ci
#     else:
#         b = ci

#     print("a: {}".format(a))
#     print("b: {}\n".format(b))
# x0 = 3
# for i in range(3):
#     x1 = x0
#     x1 = f(x1)
#     print("Fixed: {}".format(x1))

#     x0 = x0 - (f(x0) / f_prime(x0))
#     print("Newton: {}\n".format(x0))

# x0 = 4
# x_0 = 3

# for i in range(3):
#     x = (f(x0) * (x_0 - x0)) / (f(x_0) - f(x0))

#     print("Secant: {}".format(x))

#     x_0 = x0
#     x0 = x

# x = 0
# for i in range(30):
#     print("At t={}, velocity={}\n".format(i, f(x)))
#     x = x + 2
