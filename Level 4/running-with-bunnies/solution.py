from collections import deque, namedtuple


# Using regular tuples and access by index cut execution time in half,
# but this is more readable so I sticked with namedtuple.
State = namedtuple('State', ['position', 'time_left', 'saved'])


def solution(times, time_limit):
    positions = [i for i in range(len(times))]
    end_position = positions[-1]

    solutions = set()

    start = State(0, time_limit, frozenset())
    visited = {start.position: {start}}
    queue = deque((start,))

    while queue:
        curr_state = queue.popleft()
        curr_pos = curr_state.position

        if curr_pos == end_position and curr_state.time_left >= 0:
            # Avoid infinite looping in negative cycles by stopping everything
            # as soon as all bunnies are saved.
            if len(curr_state.saved) == len(times) - 2:
                return [i for i in range(len(times) - 2)]
            solutions.add(curr_state)

        for next_pos in positions:
            if next_pos == curr_pos:
                # Relying on the fact that the diagonal consists only of zeros.
                # It was not explicitly stated in the task,
                # but any other value would not make sense.
                continue

            next_time_left = curr_state.time_left - times[curr_pos][next_pos]

            next_saved = curr_state.saved
            if next_pos != 0 and next_pos != end_position:
                # position N holds bunny with ID N-1
                next_saved = next_saved.union((next_pos - 1,))

            next_state = State(next_pos, next_time_left, next_saved)

            if visited.get(next_pos) is None:
                visited[next_pos] = {next_state}
                queue.append(next_state)
                continue

            visited_for_position = visited[next_pos]
            to_remove = set()
            is_next_state_usefull = True

            for visited_state in visited_for_position:
                if visited_state.saved == next_state.saved:
                    if visited_state.time_left < next_state.time_left:
                        to_remove.add(visited_state)
                    else:
                        is_next_state_usefull = False

                elif visited_state.saved > next_state.saved:
                    if visited_state.time_left >= next_state.time_left:
                        is_next_state_usefull = False

                elif visited_state.saved < next_state.saved:
                    if visited_state.time_left <= next_state.time_left:
                        to_remove.add(visited_state)

            for state in to_remove:
                visited_for_position.remove(state)

            if is_next_state_usefull:
                visited_for_position.add(next_state)
                queue.append(next_state)

    return get_best_solution(solutions)


def get_best_solution(solutions):
    if not solutions:
        return []

    all_saved = set(map(lambda x: tuple(sorted(x.saved)), solutions))
    max_len = max(map(lambda x: len(x), all_saved))

    return list(min(filter(lambda x: len(x) == max_len, all_saved)))


print(solution([
    [0, 2, 2, 2, -1],
    [9, 0, 2, 2, -1],
    [9, 3, 0, 2, -1],
    [9, 3, 2, 0, -1],
    [9, 3, 2, 2, 0]
], 1))

print(solution([
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
], 3))

# negative loop - hacked solution
print(solution([
    [0, -1, 1, 1, 1],
    [-1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
], 3))
