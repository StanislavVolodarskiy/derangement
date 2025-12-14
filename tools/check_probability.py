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


n = 10_000
for u in range(1, n):
    print(f'\r{u}/{n}', end='', flush=True)
    assert prob_exact(u) == prob(u)
print()
