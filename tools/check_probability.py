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


SMALL_PROBS = (
    float('nan'),
    1.0,
    0.0,
    0.3333333333333333,
    0.18181818181818182,
    0.16981132075471697,
    0.1423948220064725,
    0.12505899008966492,
    0.1111044525678672,
    0.10000067417699843,
    0.09090902900118969,
    0.08333333853531667,
    0.07692307652012609,
    0.07142857145752496,
    0.06666666666472654,
    0.0625000000001218,
    0.058823529411757516,
    0.055555555555555955,
    0.0526315789473684
)


def prob(u):
    if u < len(SMALL_PROBS):
        return SMALL_PROBS[u]
    return 1 / (u + 1)


n = 10_000
for u in range(1, n):
    print(f'\r{u}/{n}', end='', flush=True)
    assert prob_exact(u) == prob(u)
print()
