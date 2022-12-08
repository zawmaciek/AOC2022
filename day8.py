def one():
    with open('input.txt') as f:
        lines = f.readlines()
    SIZE = len(lines)
    map = [[int(i) for i in line.replace('\n', '')] for line in lines]
    mask = [[int(x == 0 or x == SIZE - 1 or y == 0 or y == SIZE - 1) for x in range(SIZE)] for y in range(SIZE)]
    # UP
    for x in range(1, SIZE - 1):
        max = map[0][x]
        for y in range(1, SIZE - 1):
            if map[y][x] > max:
                max = map[y][x]
                mask[y][x] = 1
    # LEFT
    for y in range(1, SIZE - 1):
        max = map[y][0]
        for x in range(1, SIZE - 1):
            if map[y][x] > max:
                max = map[y][x]
                mask[y][x] = 1
    # DOWN
    for x in range(SIZE - 2, 0, -1):
        max = map[SIZE - 1][x]
        for y in range(SIZE - 2, 0, -1):
            if map[y][x] > max:
                max = map[y][x]
                mask[y][x] = 1
    # RIGHT
    for y in range(SIZE - 2, 0, -1):
        max = map[y][SIZE - 1]
        for x in range(SIZE - 2, 0, -1):
            if map[y][x] > max:
                max = map[y][x]
                mask[y][x] = 1
    print(map)
    print(mask)
    print(f"Part 1: {sum([item for sublist in mask for item in sublist])}")


def two():
    def score(map, X, Y):
        score = 1
        SIZE = len(map)
        # RIGHT
        for x in range(X + 1, SIZE):
            if map[Y][x] >= map[Y][X]:
                score *= (x - X)
                break
        else:
            score *= SIZE - X - 1
        # LEFT
        for x in range(X - 1, 0, -1):
            if map[Y][x] >= map[Y][X]:
                score *= (X - x)
                break
        else:
            score *= X
        # UP
        for y in range(Y + 1, SIZE):
            if map[y][X] >= map[Y][X]:
                score *= (y - Y)
                break
        else:
            score *= SIZE - Y - 1
        # DOWN
        for y in range(Y - 1, 0, -1):
            if map[y][X] >= map[Y][X]:
                score *= (Y - y)
                break
        else:
            score *= Y
        return score

    with open('input.txt') as f:
        lines = f.readlines()
    SIZE = len(lines)
    map = [[int(i) for i in line.replace('\n', '')] for line in lines]
    mask = [[0 for x in range(SIZE)] for y in range(SIZE)]
    for y in range(1, SIZE - 1):
        for x in range(1, SIZE - 1):
            mask[y][x] = score(map, x, y)
    print(f"Part 2: {max([item for sublist in mask for item in sublist])}")


two()
