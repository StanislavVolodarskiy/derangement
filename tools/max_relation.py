import math
import functools


@functools.cache
def subfactorial(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        f1, f2 = f2, i * (f1 + f2)
    return f2


mx = 0
for n in range(30):
    f = math.factorial(n)
    s = subfactorial(n)
    if s == 0:
        r = float('inf')
    else:
        r = f / s
        mx = max(mx, r)
    print(n, f, s, r)
print(mx)
