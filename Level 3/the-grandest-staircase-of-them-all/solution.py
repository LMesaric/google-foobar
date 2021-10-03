def solution(n):
    cache = [0] * (n + 1)
    cache[0] = 1

    # Use xrange in Python 2.
    for j in range(1, n + 1):
        for i in range(n, j - 1, -1):
            cache[i] += cache[i - j]

    return cache[-1] - 1


print(solution(3))
print(solution(200))
