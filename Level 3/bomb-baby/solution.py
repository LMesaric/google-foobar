def solution(m, f):
    m, f = int(m), int(f)
    cnt = 0

    while True:
        if m == 1 and f == 1:
            return str(cnt)
        if (m == f) or (m % 2 == 0 and f % 2 == 0):
            return "impossible"
        if m < f:
            m, f = f, m

        if f == 0:
            return "impossible"
        if f == 1:
            cnt += m - 1
            return str(cnt)

        times = m / f
        m -= f * times
        cnt += times


print(solution('4', '7'))
print(solution('2', '1'))
print(solution('1', '1'))
print(solution('2', '1'))
print(solution('1', '2'))
print(solution('3', '1'))
print(solution('4', '1'))
print(solution('4', '3'))
print(solution('999', '1'))
print(solution('999', '2'))
print(solution('999', '3'))
