import random


def derangementFisherYates1(n, r=random):
    a = list(range(n))
    while True:
        r.shuffle(a)
        if all(i != ai for i, ai in enumerate(a)):  # is derangement?
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
