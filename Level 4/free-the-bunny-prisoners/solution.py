from itertools import combinations


def solution(num_buns, num_required):
    result = [[] for _ in range(num_buns)]

    positions = combinations([i for i in range(num_buns)], num_buns - num_required + 1)
    for key, bunny_indices in enumerate(positions):
        for bunny_index in bunny_indices:
            result[bunny_index].append(key)

    return result


print(solution(2, 1))
print(solution(4, 4))
print(solution(5, 3))
print(solution(5, 4))

print(solution(1, 0))
print(solution(2, 0))
print(solution(3, 0))
print(solution(9, 0))

print(solution(1, 1))
print(solution(2, 1))
print(solution(3, 1))
print(solution(9, 1))
