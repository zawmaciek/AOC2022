import re
from tqdm import tqdm
import sys


def calc_distance(x, y, X, Y):
    return abs(X - x) + abs(Y - y)


def one():
    pos = set()
    LINE_Y = 2000000
    with open('input.txt') as f:
        for line in f.read().splitlines():
            match = re.search(r'Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)', line)
            x, y, X, Y = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
            dis = calc_distance(x, y, X, Y)
            for dx in range(x - dis - 1, x + dis + 2):
                pos.add((dx, dx - abs(LINE_Y - y)))
                pos.add((dx, dx + abs(LINE_Y - y)))
    print(len(pos))


MAX_CORD = 4000000 + 1


def get_borders(beacon):
    pos = set()
    x, y, dist = beacon[0], beacon[1], beacon[4]
    for dx in range(x - dist - 1, x + dist + 2):
        if 0 <= dx <= MAX_CORD:
            dy = dist - abs(x - dx) + 1
            e = beacon[1] + dy
            if 0 <= e <= MAX_CORD:
                pos.add((dx, e))
            e = beacon[1] - dy
            if 0 <= e <= MAX_CORD:
                pos.add((dx, e))
    return pos


def two():
    beacons = []
    with open('input.txt') as f:
        for line in f.read().splitlines():
            match = re.search(r'Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)', line)
            x, y, X, Y = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
            DISTANCE = calc_distance(x, y, X, Y)
            beacons.append((x, y, X, Y, DISTANCE))
    borders = set.union(*[get_borders(becaon) for becaon in tqdm(beacons)])
    for d in tqdm(borders):
        dx, dy = d
        for beacon in beacons:
            if calc_distance(dx, dy, beacon[0], beacon[1]) <= beacon[4]:
                break
        else:
            print(4000000 * dx + dy)
            print(f"{dx} {dy}")
            sys.exit(0)


two()
