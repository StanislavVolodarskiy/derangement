import collections
import random
import time

import derangement


def elapsed(f):
    start = time.perf_counter()
    r = f()
    finish = time.perf_counter()
    return r, finish - start


class RandomCounter:
    def __init__(self, seed):
        self._r = random.Random(seed)
        self._c = 0

    def random(self):
        self._c += 1
        return self._r.random()

    def randrange(self, *args):
        self._c += 1
        return self._r.randrange(*args)

    def choice(self, a):
        self._c += 1
        return self._r.choice(a)

    def shuffle(self, a):
        self._c += len(a) - 1
        self._r.shuffle(a)

    def counter(self):
        return self._c


def test_function(n, k, label, f):
    r = RandomCounter(42)
    c, e = elapsed(
        lambda: collections.Counter(tuple(f(n, r)) for _ in range(k))
    )

    for a in c.keys():
        assert all(i != ai for i, ai in enumerate(a))  # is derangement

    m = len(c)
    print(
        label,
        f'{e:5.2f}',
        f'{r.counter():10d}',
        f'{k / m:10.2f}',
        [min(c.values()), '...', max(c.values())]
    )


def test_all_functions(n, m):
    print('n =', n, 'm =', m)
    test_function(n, m, 'derangement ', derangement.derangement)
    test_function(n, m, 'FisherYates1', derangement.derangementFisherYates1)
    test_function(n, m, 'FisherYates2', derangement.derangementFisherYates2)


def main():
    for n in range(2, 11):
        test_all_functions(n, 10_000_000)

    test_all_functions(10, 1_000_000)
    test_all_functions(100, 100_000)
    test_all_functions(1_000, 10_000)
    test_all_functions(10_000, 1_000)
    test_all_functions(100_000, 100)
    test_all_functions(1_000_000, 10)
    test_all_functions(10_000_000, 1)


main()
