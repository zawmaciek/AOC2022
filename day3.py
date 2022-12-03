def str_to_int(char):
    char = char.pop()
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


def one():
    score = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            half_1, half_2 = line[:len(line) // 2], line[len(line) // 2:]
            a = str_to_int(set(half_2).intersection(set(half_1)))
            score += a
    print(score)


def two():
    score = 0
    with open('input.txt', 'r') as f:
        elves = f.read().splitlines()
    for i in range(0, len(elves) - 2, 3):
        score += str_to_int(set(elves[i]).intersection(set(elves[i + 1]), set(elves[i + 2])))
    print(score)


one()
two()
