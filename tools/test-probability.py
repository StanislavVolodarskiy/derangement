import fractions
import functools


@functools.cache
def subfactorial(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        f1, f2 = f2, i * (f1 + f2)
    return f2


def prob_exact(u):
    return u * subfactorial(u - 1) / subfactorial(u + 1)


@functools.cache
def prob_approx(u):
    if u >= 20:
        return 1 / (u + 1)

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


for u in range(1, 10_000):
    e = prob_exact(u)
    a = prob_approx(u)
    if e != a:
        print(u, e - a, f'{e:.15f}', f'{a:.15f}')
