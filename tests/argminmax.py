import ulab

# Adapted from https://docs.python.org/3.8/library/itertools.html#itertools.permutations
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

# Combinations expected to throw
try:
    print(ulab.numerical.argmin([]))
except ValueError:
    print("ValueError")

try:
    print(ulab.numerical.argmax([]))
except ValueError:
    print("ValueError")

# Combinations expected to succeed
print(ulab.numerical.argmin([1]))
print(ulab.numerical.argmax([1]))
print(ulab.numerical.argmin(ulab.array([1])))
print(ulab.numerical.argmax(ulab.array([1])))

print()
print("max tests")
for p in permutations((100,200,300)):
    m1 = ulab.numerical.argmax(p)
    m2 = ulab.numerical.argmax(ulab.array(p))
    print(p, m1, m2)
    if m1 != m2 or p[m1] != max(p):
        print("FAIL", p, m1, m2, max(p))

print()
print("min tests")
for p in permutations((100,200,300)):
    m1 = ulab.numerical.argmin(p)
    m2 = ulab.numerical.argmin(ulab.array(p))
    print(p, m1, m2)
    if m1 != m2 or p[m1] != min(p):
        print("FAIL", p, m1, m2, min(p))
