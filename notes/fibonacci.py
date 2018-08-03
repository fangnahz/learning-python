# Several fibonacci sequence implementations


def fibonacci_recursion(n):
    if n == 0:
        nth = 0
    if n == 1:
        nth = 1
    if n > 1:
        nth = fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
        print('f[{}]: {}'.format(n, nth))
    return nth


def fibonacci_cache(n, cache={0: 0, 1: 1}):
    if n in cache:
        return cache[n]
    if n > 1:
        nth = fibonacci_cache(n-1) + fibonacci_cache(n-2)
        cache[n] = nth
        print('cache[{}]: {}'.format(n, nth))
    return nth


def fibonacci_straight(n):
    if n <= 0:
        nth = 0
    if n > 0:
        prev = 0
        nth = 1
        for _ignore in range(2, n+1):
            new = nth + prev
            prev = nth
            nth = new
    return nth


# Very similar to fibonacci:
# Suppose climing a stair way with n stairs,
# Randomly goes up 1 or 2 steps each time,
# How many possible climbing combinitions?
def climb(n):
    if n == 1:
        num = 1
    if n == 2:
        num = 2
    if n > 2:
        num = climb(n-1) + climb(n-2)
    return num


def climb_cache(n, cache={1: 1, 2: 2}):
    if n in cache:
        return cache[n]
    if n > 2:
        num = climb_cache(n-1) + climb_cache(n-2)
        cache[n] = num
    return num
