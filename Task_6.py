from itertools import count, cycle

rep = ['a', 'b', 'c', 'd', 't']


def c_el():
    for i in count(5):
        if i >= 10:
            break
        yield i


def cy_el():
    for i, j in enumerate(cycle(rep)):
        if i >= 10:
            break
        yield j


print(list(c_el()), list(cy_el()))
