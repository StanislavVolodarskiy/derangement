import collections
import functools
import random
import time


def is_derangement(a):
    return all(i != v for i, v in enumerate(a))


# suggested by [MotiNK](https://cs.stackexchange.com/users/37884/motink)
#
# for i=0..n-2
#   swapIdx = random(i+1,n) // random(start,end) --> start <= i < end
#   swapElement(array, i, swapIdx)


class MotiNK:
    def __init__(self, n):
        self._n = n
        self._c = 0

    def next(self):
        a = list(range(self._n))
        for i in range(self._n - 1):
            j = random.randrange(i + 1, self._n)
            self._c += 1
            a[i], a[j] = a[j], a[i]
        assert is_derangement(a)
        return tuple(a)

    def count(self):
        return self._c


class FisherYates:
    def __init__(self, n):
        self._n = n
        self._c = 0

    def next(self):
        a = list(range(self._n))
        for i in range(self._n - 1):
            j = random.randrange(i, self._n)
            self._c += 1
            a[i], a[j] = a[j], a[i]
        return tuple(a)

    def count(self):
        return self._c


class FisherYatesDerangement1:
    def __init__(self, n):
        self._n = n
        self._c = 0

    def next(self):
        while True:
            a = list(range(self._n))
            random.shuffle(a)
            self._c += self._n - 1
            if is_derangement(a):
                return tuple(a)

    def count(self):
        return self._c


class FisherYatesDerangement2:
    def __init__(self, n):
        self._n = n
        self._c = 0

    def next(self):
        while True:
            a = list(range(self._n))
            if self._shuffle(a):
                assert is_derangement(a)
                return tuple(a)

    def count(self):
        return self._c

    def _shuffle(self, a):
        for i in range(self._n):
            j = random.randrange(i, self._n)
            self._c += 1
            if i == a[j]:
                return False
            a[i], a[j] = a[j], a[i]
        return True


@functools.cache
def subfactorial(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        f1, f2 = f2, i * (f1 + f2)
    return f2


class Derangement:
    def __init__(self, n):
        self._n = n
        self._c = 0

    def next(self):
        a = self._derangement(self._n)
        assert(is_derangement(a))
        return tuple(a)

    def count(self):
        return self._c

    def _derangement(self, n):
        a = list(range(n))
        mark = [False] * n
        i = n - 1
        u = n - 1
        while u >= 1:
            if not mark[i]:
                while True:
                    j = random.randrange(i)
                    self._c += 1
                    if not mark[j]:
                        break
                a[i], a[j] = a[j], a[i]
                p = random.random()
                self._c += 1
                if p < u * subfactorial(u - 1) / subfactorial(u + 1):
                    mark[j] = True
                    u -= 1
                u -= 1
            i -= 1
        return a


class DerangementRecursive:
    def __init__(self, n):
        self._n = n
        self._c = 0

    def next(self):
        a = self._derangement(self._n)
        assert(is_derangement(a))
        return tuple(a)

    def count(self):
        return self._c

    def _derangement(self, n):
        assert n != 1
        if n == 0:
            return []
        n1 = subfactorial(n - 1)
        n2 = subfactorial(n - 2)
        k = random.randrange(n1 + n2)
        self._c += 1
        i = random.randrange(n - 1)
        self._c += 1
        if k < n1:
            a = self._derangement(n - 1)
        else:
            a = self._derangement(n - 2)
            for j in range(n - 2):
                if a[j] >= i:
                    a[j] += 1
            a.insert(i, i)
        a.append(n - 1)
        a[i], a[n - 1] = a[n - 1], a[i]
        return a


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


def test_generator(k, label, gen):
    c, e = elapsed(lambda: collections.Counter(gen.next() for _ in range(k)))
    m = len(c)
    print(
        label,
        f'{e:5.2f}',
        f'{gen.count():10}',
        f'{k / m:10.2f}',
        [min(c.values()), '...', max(c.values())]
    )


def test_all_generators(n, m):
    print('n =', n, 'm =', m)
    # test_generator(m, 'MotiNK                 ', MotiNK(n))
    test_generator(m, 'Derangement            ', Derangement(n))
    # test_generator(m, 'DerangementRecursive   ', DerangementRecursive(n))
    test_generator(m, 'FisherYatesDerangement1', FisherYatesDerangement1(n))
    test_generator(m, 'FisherYatesDerangement2', FisherYatesDerangement2(n))
    # test_generator(m, 'FisherYates            ', FisherYates(n))


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
