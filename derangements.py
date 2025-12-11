import collections
import functools
import random
import time


@functools.cache
def subfactorial(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        f1, f2 = f2, i * (f1 + f2)
    return f2


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


def fisherYatesDerangement1(n, r=random):
    a = list(range(n))
    while True:
        r.shuffle(a)
        if all(i != ai for i, ai in enumerate(a)): # is derangement?
            return a


def fisherYatesDerangement2(n, r=random):
    a = list(range(n))
    while True:
        for i in range(n):
            j = r.randrange(i, n)
            if i == a[j]:
                break
            a[i], a[j] = a[j], a[i]
        else:
            return a


def elapsed(f):
    start = time.perf_counter()
    r = f()
    finish = time.perf_counter()
    return r, finish - start


def test_function(n, k, label, f):
    c, e = elapsed(lambda: collections.Counter(tuple(f(n)) for _ in range(k)))
    m = len(c)
    print(
        label,
        f'{e:5.2f}',
        f'{k / m:10.2f}',
        [min(c.values()), '...', max(c.values())]
    )


def test_all_functions(n, m):
    print('n =', n, 'm =', m)
    test_function(n, m, 'derangement            ', derangement            )
    test_function(n, m, 'fisherYatesDerangement1', fisherYatesDerangement1)
    test_function(n, m, 'fisherYatesDerangement2', fisherYatesDerangement2)


def main():
    test_all_functions(        10, 1_000_000)
    test_all_functions(       100,   100_000)
    test_all_functions(     1_000,    10_000)
    test_all_functions(    10_000,     1_000)
    test_all_functions(   100_000,       100)
    test_all_functions( 1_000_000,        10)
    test_all_functions(10_000_000,         1)
    for n in range(2, 11):
        test_all_functions(n, 1_000_000)

    test_all_generators(100, 1_000_000)
    for n in range(2, 11):
        test_all_generators(n, 1_000_000)


main()
