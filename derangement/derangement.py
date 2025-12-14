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
    1.0,                   # float(1 * !0 / !2)
    0.0,                   # float(2 * !1 / !3)
    0.3333333333333333,    # float(3 * !2 / !4)
    0.18181818181818182,   # float(4 * !3 / !5)
    0.16981132075471697,   # float(5 * !4 / !6)
    0.1423948220064725,    # float(6 * !5 / !7)
    0.12505899008966492,   # float(7 * !6 / !8)
    0.1111044525678672,    # float(8 * !7 / !9)
    0.10000067417699843,   # float(9 * !8 / !10)
    0.09090902900118969,   # float(10 * !9 / !11)
    0.08333333853531667,   # float(11 * !10 / !12)
    0.07692307652012609,   # float(12 * !11 / !13)
    0.07142857145752496,   # float(13 * !12 / !14)
    0.06666666666472654,   # float(14 * !13 / !15)
    0.0625000000001218,    # float(15 * !14 / !16)
    0.058823529411757516,  # float(16 * !15 / !17)
    0.055555555555555955,  # float(17 * !16 / !18)
    0.0526315789473684     # float(18 * !17 / !19)
)


def prob(u):
    if u < len(SMALL_PROBS):
        return SMALL_PROBS[u]
    return 1 / (u + 1)


def derangement(n, r=random):
    a = list(range(n))  # derangement
    x = list(range(n))  # marked if x[i] == -1
    y = list(range(n))  # unmarked xs to choose

    i = n - 1
    u = n - 1
    while u >= 1:
        if x[i] >= 0:

            # mark x[i]
            x[y[-1]] = x[i]
            y[x[i]] = y[-1]
            x[i] = -1
            y.pop()

            j = r.choice(y)
            a[i], a[j] = a[j], a[i]
            if r.random() < prob(u):

                # mark x[j]
                x[y[-1]] = x[j]
                y[x[j]] = y[-1]
                x[j] = -1
                y.pop()

                u -= 1
            u -= 1
        i -= 1
    return a
