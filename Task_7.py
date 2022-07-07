from functools import reduce


def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
        yield s


for i in fact(4):
    print(i)
