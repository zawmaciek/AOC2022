import re


def one():
    stacks = []
    with open('input.txt') as f:
        for line in f.readlines():
            if line.startswith('   ') or line.startswith('['):
                for index in range(0, len(line) // 4):
                    if line[index * 4] != '[':
                        stacks.append([])
                    else:
                        try:
                            stacks[index].insert(0, line[index * 4 + 1])
                        except IndexError:
                            stacks.append([])
                            stacks[index].insert(0, line[index * 4 + 1])
            if line.startswith('move'):
                numbers = [int(i) for i in re.findall('[0-9]+', line)]
                for i in range(numbers[0]):
                    item = stacks[numbers[1] - 1].pop()
                    stacks[numbers[2] - 1].append(item)
    for stack in stacks:
        if len(stack) > 0:
            print(stack[-1], end='')


def two():
    stacks = []
    with open('input.txt') as f:
        for line in f.readlines():
            if line.startswith('   ') or line.startswith('['):
                for index in range(0, len(line) // 4):
                    if line[index * 4] != '[':
                        stacks.append([])
                    else:
                        try:
                            stacks[index].insert(0, line[index * 4 + 1])
                        except IndexError:
                            stacks.append([])
                            stacks[index].insert(0, line[index * 4 + 1])
            if line.startswith('move'):
                numbers = [int(i) for i in re.findall('[0-9]+', line)]
                items = stacks[numbers[1] - 1][-numbers[0]:]
                for i in range(numbers[0]):
                    stacks[numbers[1] - 1].pop()
                stacks[numbers[2] - 1] += items
                print(stacks)
    for stack in stacks:
        if len(stack) > 0:
            print(stack[-1], end='')


two()
