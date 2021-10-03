from itertools import combinations


def concat_num(l):
    l.sort(reverse=True)
    res = 0
    for n in l:
        res *= 10
        res += n
    return res


def solution(l):
    safe = []
    working = []

    for num in l:
        if num % 3:
            working.append(num)
        else:
            safe.append(num)

    working.sort()
    sum_working = sum(working)
    if sum_working % 3 == 0:
        return concat_num(safe + working)

    for index, num in enumerate(working):
        if (sum_working - num) % 3 == 0:
            del working[index]
            return concat_num(safe + working)

    combs = list(combinations(working, 2))
    combs.sort(key=lambda x: x[1])  # stable sort
    for num1, num2 in combs:
        if (sum_working - num1 - num2) % 3 == 0:
            working.remove(num1)
            working.remove(num2)
            return concat_num(safe + working)

    return 0


print(solution([1, 1, 3, 4]))
print(solution([1, 1, 3, 4, 5, 9]))
print(solution([2]))
print(solution([2, 2]))
print(solution([7, 7, 8]))
