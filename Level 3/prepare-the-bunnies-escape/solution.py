from collections import deque, namedtuple


def solution(map):
    h, w = len(map), len(map[0])

    def neighbours(x, y):
        if x > 0:
            yield (x-1, y)
        if y > 0:
            yield (x, y-1)
        if x < w-1:
            yield (x+1, y)
        if y < h-1:
            yield (x, y+1)

    State = namedtuple('State', ['x', 'y', 'walled'])
    start = State(w-1, h-1, False)

    visited = {start: 1}
    queue = deque([start])

    while queue:
        s = queue.popleft()
        if s.x == 0 and s.y == 0:
            return visited[s]

        for neighbour in neighbours(s.x, s.y):
            if s.walled and map[neighbour[1]][neighbour[0]]:
                continue

            next_s = State(neighbour[0],
                           neighbour[1],
                           s.walled or map[neighbour[1]][neighbour[0]])

            if next_s not in visited:
                visited[next_s] = visited[s] + 1
                queue.append(next_s)

    return 0


print(solution([
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0]
]))

print(solution([
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]))
