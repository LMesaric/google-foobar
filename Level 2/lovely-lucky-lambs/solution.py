from math import log


def solution(total_lambs):
    return solution_min_paid(total_lambs) - solution_max_paid(total_lambs)


def solution_max_paid(total_lambs):
    return int(log(1 + total_lambs, 2))


def solution_min_paid(total_lambs):
    a = b = i = 1
    while True:
        a, b = b, a+b
        i += 1
        if b > total_lambs + 1:
            return i - 2


print(solution(143))
print(solution(10))
