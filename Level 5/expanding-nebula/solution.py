def solution(g):
    prev_g = [[None] * (len(g[0]) + 1) for _ in range(len(g) + 1)]
    return solution_rec(g, 0, 0, prev_g, list(), dict())


def solution_rec(g, x, y, prev_g, prior_states, cache):
    if x >= len(prev_g[0]):
        return 1

    cache_key = tuple(prior_states[-(len(prev_g)+1):] + [x, y])
    cache_val = cache.get(cache_key)
    if cache_val is not None:
        return cache_val

    num_states = 0
    for gas_state in (False, True):
        if x == 0 or y == 0 or g[y-1][x-1] == next_step(x, y, gas_state, prev_g):
            prev_g[y][x] = gas_state
            prior_states.append(gas_state)
            column_step, next_row = divmod(y + 1, len(prev_g))  # column_step is either 0 or 1
            num_states += solution_rec(g, x + column_step, next_row, prev_g, prior_states, cache)
            del prior_states[-1]

    cache[cache_key] = num_states
    return num_states


def next_step(x, y, gas_state, prev_g):
    sum2x2 = gas_state + prev_g[y][x-1] + prev_g[y-1][x-1] + prev_g[y-1][x]
    return sum2x2 == 1


from time import time

t = time()

print(solution([
    [True, False, True],
    [False, True, False],
    [True, False, True]
]))

print(solution([
    [True, False, True, False, False, True, True, True],
    [True, False, True, False, False, False, True, False],
    [True, True, True, False, False, False, True, False],
    [True, False, True, False, False, False, True, False],
    [True, False, True, False, False, True, True, True]
]))

print(solution([
    [True, True, False, True, False, True, False, True, True, False],
    [True, True, False, False, False, False, True, True, True, False],
    [True, True, False, False, False, False, False, False, False, True],
    [False, True, False, False, False, False, True, True, False, False]
]))

print(time() - t)
