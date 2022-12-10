def one():
    sum = 0
    with open('input.txt') as f:
        lines = iter(f.readlines())
    register = 1
    cycle = 1
    buffer = None
    while True:
        try:
            if cycle in list(range(20, 221, 40)):
                print(f"{cycle} {register} {cycle * register}")
                sum += cycle * register
            if buffer is not None:
                register += buffer
                buffer = None
            else:
                operation = next(lines).replace('\n', '')
                if operation == 'noop':
                    pass
                if operation.startswith('addx'):
                    buffer = int(operation.split()[1])
            cycle += 1
        except StopIteration:
            break
    print(sum)


def two():
    with open('input.txt') as f:
        lines = iter(f.readlines())
    register = 1
    cycle = 1
    buffer = None
    line_buff = ''
    while True:
        try:
            if cycle in list(range(41, 241, 40)):
                print(line_buff)
                line_buff = ''
                cycle -= 40

            # End of cycle
            if buffer is not None:
                register += buffer
                buffer = None
            else:
                operation = next(lines).replace('\n', '')
                if operation == 'noop':
                    pass
                if operation.startswith('addx'):
                    buffer = int(operation.split()[1])
            if register - 1 <= cycle <= register + 1:
                line_buff += '#'
            else:
                line_buff += '.'
            cycle += 1
        except StopIteration:
            break


two()
