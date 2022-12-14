class Sand:
    def __init__(self):
        self.x = 500
        self.y = 0
        self.is_moving = False

    def find_place(self, map):
        while True:
            try:
                if map[self.y + 1][self.x] == ' ':
                    self.y += 1
                elif map[self.y + 1][self.x - 1] == ' ':
                    self.y += 1
                    self.x -= 1
                elif map[self.y + 1][self.x + 1] == ' ':
                    self.y += 1
                    self.x += 1
                else:
                    if self.x == 500 and self.y == 0:
                        return False, map
                    else:
                        map[self.y][self.x] = 'o'
                        return True, map
            except IndexError:
                return False, map


def save_map(map):
    with open('debug.txt', 'w') as f:
        for line in map:
            f.write(''.join(line) + '\n')


def draw_line(map, x, y, X, Y):
    if x > X:
        x, X = X, x
    if y > Y:
        y, Y = Y, y
    if x == X:
        for i in range(y, Y + 1):
            map[i][x] = '#'
    else:
        for i in range(x, X + 1):
            map[y][i] = '#'
    return map


def one():
    map = [[' ' for _ in range(0, 1000)] for __ in range(0, 180)]
    with open('input.txt') as f:
        for line in f.readlines():
            points = line.replace('\n', '').split(' -> ')
            for i in range(len(points) - 1):
                p1 = points[i].split(',')
                p2 = points[i + 1].split(',')
                map = draw_line(map, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
    sum = 0
    while True:
        curr = Sand()
        result, map = curr.find_place(map)
        if not result:
            print(sum)
            break
        else:
            sum += 1
    save_map(map)


def two():
    map = [[' ' for _ in range(0, 1000)] for __ in range(0, 180)]
    with open('input.txt') as f:
        for line in f.readlines():
            points = line.replace('\n', '').split(' -> ')
            for i in range(len(points) - 1):
                p1 = points[i].split(',')
                p2 = points[i + 1].split(',')
                map = draw_line(map, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
    for i in range(len(map) - 1, -1, -1):
        if '#' in ''.join(map[i]):
            for j in range(0, len(map[i])):
                map[i + 2][j] = '#'
            break
    sum = 0
    counter = 0
    while True:
        counter += 1
        curr = Sand()
        result, map = curr.find_place(map)
        if not result:
            print(sum+1)
            break
        else:
            sum += 1
    save_map(map)

one()
two()
