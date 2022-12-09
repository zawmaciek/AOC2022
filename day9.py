class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dir: str):
        if dir == 'R':
            self.x += 1
        elif dir == 'L':
            self.x -= 1
        elif dir == 'U':
            self.y += 1
        else:
            self.y -= 1

    def __str__(self):
        return f"{self.x}_{self.y}"

    def follow(self, point):
        def magn(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0

        dist_x = self.x - point.x
        dist_y = self.y - point.y
        if abs(dist_x) == 0 and abs(dist_y) < 2 or abs(dist_y) == 0 and abs(dist_x) < 2 or abs(dist_y) == abs(
                dist_x) == 1:
            pass
        else:  # MOOOOVE
            self.x -= magn(dist_x)
            self.y -= magn(dist_y)

    def __repr__(self):
        return str(self)


def one():
    head = Point(0, 0)
    tail = Point(0, 0)
    visited = set()
    with open('input.txt') as f:
        for line in f.readlines():
            dir, steps = line.split()
            steps = int(steps)
            for _ in range(steps):
                head.move(dir)
                tail.follow(head)
                visited.add(str(tail))
    print(len(visited))


def two():
    rope = [Point(0, 0) for _ in range(10)]
    visited = set()
    with open('input.txt') as f:
        for line in f.readlines():
            dir, steps = line.split()
            steps = int(steps)
            for _ in range(steps):
                rope[0].move(dir)
                for i in range(1, len(rope)):
                    rope[i].follow(rope[i - 1])
                visited.add(str(rope[-1]))
    print(len(visited))


one()
two()
