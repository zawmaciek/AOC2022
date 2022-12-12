from queue import Queue


def one():
    with open('input.txt') as f:
        map = [list(line.replace('\n', '')) for line in f.readlines()]
    start, goal = None, None
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'S':
                start = (x, y)
                map[y][x] = 'a'
            if map[y][x] == 'E':
                goal = (x, y)
                map[y][x] = 'z'
            if goal is not None and start is not None:
                break
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    came_from[start] = None
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        neighbours = []
        if current[0] > 0:
            neighbours.append((current[0] - 1, current[1]))
        if current[0] < len(map[0]) - 1:
            neighbours.append((current[0] + 1, current[1]))
        if current[1] > 0:
            neighbours.append((current[0], current[1] - 1))
        if current[1] < len(map) - 1:
            neighbours.append((current[0], current[1] + 1))
        neighbours = [neighbour for neighbour in neighbours if
                      ord(map[current[1]][current[0]]) >= ord(map[neighbour[1]][neighbour[0]]) - 1]
        for next in neighbours:
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    print(len(path))


def two():
    with open('input.txt') as f:
        map = [list(line.replace('\n', '')) for line in f.readlines()]
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'E':
                start = (x, y)
                map[y][x] = 'z'
                break
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    came_from[start] = None
    while not frontier.empty():
        current = frontier.get()
        if map[current[1]][current[0]] == 'a':
            goal = (current[0], current[1])
            break
        neighbours = []
        if current[0] > 0:
            neighbours.append((current[0] - 1, current[1]))
        if current[0] < len(map[0]) - 1:
            neighbours.append((current[0] + 1, current[1]))
        if current[1] > 0:
            neighbours.append((current[0], current[1] - 1))
        if current[1] < len(map) - 1:
            neighbours.append((current[0], current[1] + 1))
        neighbours = [neighbour for neighbour in neighbours if
                      ord(map[current[1]][current[0]]) <= ord(map[neighbour[1]][neighbour[0]]) + 1]
        for next in neighbours:
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    print(len(path) - 1)


one()
two()
