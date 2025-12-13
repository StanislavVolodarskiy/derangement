import collections
import time

import derangement


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
    test_function(
        n,
        m,
        'derangement            ',
        derangement.derangement
    )
    test_function(
        n,
        m,
        'derangementFisherYates1',
        derangement.derangementFisherYates1
    )
    test_function(
        n,
        m,
        'derangementFisherYates2',
        derangement.derangementFisherYates2
    )


def main():
    test_all_functions(10, 1_000_000)
    test_all_functions(100, 100_000)
    test_all_functions(1_000, 10_000)
    test_all_functions(10_000, 1_000)
    test_all_functions(100_000, 100)
    test_all_functions(1_000_000, 10)
    test_all_functions(10_000_000, 1)
    for n in range(2, 11):
        test_all_functions(n, 1_000_000)


main()
