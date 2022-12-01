def one():
    elves = [0]
    with open('input.txt', 'r') as f:
        for raw_line in f.readlines():
            if raw_line == '\n':
                elves.append(0)
            else:
                elves[-1] += int(raw_line)
        print(max(elves))


def two():
    elves = [0]
    with open('input.txt', 'r') as f:
        for raw_line in f.readlines():
            if raw_line == '\n':
                elves.append(0)
            else:
                elves[-1] += int(raw_line)
        print(sum(sorted(elves, reverse=True)[0:3]))


if __name__ == '__main__':
    one()
    two()
