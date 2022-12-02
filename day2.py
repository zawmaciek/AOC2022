def calc1(line: str):
    abc, xyz = line.split()
    if abc == 'A':
        if xyz == 'X':
            return 4
        if xyz == 'Y':
            return 8
        if xyz == 'Z':
            return 3
    if abc == 'B':
        if xyz == 'X':
            return 1
        if xyz == 'Y':
            return 5
        if xyz == 'Z':
            return 9
    if abc == 'C':
        if xyz == 'X':
            return 7
        if xyz == 'Y':
            return 2
        if xyz == 'Z':
            return 6


def one():
    score = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            score += calc1(line)
    print(score)


def calc2(line):
    abc, xyz = line.split()
    if abc == 'A':  # ROCK
        if xyz == 'X':
            return calc1('A Z')
        elif xyz == 'Y':
            return calc1('A X')
        elif xyz == 'Z':
            return calc1('A Y')
        else:
            print('ERROR')
    elif abc == 'B':  # PAPER
        if xyz == 'X':
            return calc1('B X')
        elif xyz == 'Y':
            return calc1('B Y')
        elif xyz == 'Z':
            return calc1('B Z')
        else:
            print('ERROR')
    elif abc == 'C':  # SCISSORS
        if xyz == 'X':
            return calc1('C Y')
        elif xyz == 'Y':
            return calc1('C Z')
        elif xyz == 'Z':
            return calc1('C X')
        else:
            print('ERROR')
    else:
        print('ERROR')

def two():
    score = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            score += calc2(line)
    print(score)


two()
