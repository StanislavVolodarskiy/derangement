import collections
import functools
import random
import time


@functools.cache
def prob(u):
    f1 = 0.
    f2 = 1.
    for i in range(u - 1):
        f1, f2 = f2, i * (f1 + f2)
        if f1 > 1.:
            f2 /= f1
            f1 = 1.

    d = f2

    for i in range(u - 1, u + 1):
        f1, f2 = f2, i * (f1 + f2)

    n = f2
    return u * d / n


def derangement(n, r=random):
    a = list(range(n))
    mark = [False] * n
    i = n - 1
    u = n - 1
    while u >= 1:
        if not mark[i]:
            while True:
                j = r.randrange(i)
                if not mark[j]:
                    break
            a[i], a[j] = a[j], a[i]
            if r.random() < prob(u):
                mark[j] = True
                u -= 1
            u -= 1
        i -= 1
    return a


def derangementFisherYates1(n, r=random):
    a = list(range(n))
    while True:
        r.shuffle(a)
        if all(i != ai for i, ai in enumerate(a)): # is derangement?
            return a


def derangementFisherYates2(n, r=random):
    a = list(range(n))
    while True:
        for i in range(n):
            j = r.randrange(i, n)
            if i == a[j]:
                break
            a[i], a[j] = a[j], a[i]
        else:
            return a
