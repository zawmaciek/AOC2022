import functools


def recur_compare(left, right):
    for i in range(max(len(left), len(right))):
        result = None
        try:
            l = left[i]
        except IndexError:
            return True
        try:
            r = right[i]
        except IndexError:
            return False
        if type(l) == type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
        elif type(l) == int and type(r) == list:
            result = recur_compare([l], r)
        elif type(r) == int and type(l) == list:
            result = recur_compare(l, [r])
        else:
            result = recur_compare(l, r)
        if result is not None:
            return result


def recur_sort_compare(left, right):
    for i in range(max(len(left), len(right))):
        result = None
        try:
            l = left[i]
        except IndexError:
            return 1
        try:
            r = right[i]
        except IndexError:
            return -1
        if type(l) == type(r) == int:
            if l < r:
                return 1
            elif l > r:
                return -1
        elif type(l) == int and type(r) == list:
            result = recur_sort_compare([l], r)
        elif type(r) == int and type(l) == list:
            result = recur_sort_compare(l, [r])
        else:
            result = recur_sort_compare(l, r)
        if result is not None:
            return result


def one():
    pairs = []
    i = 1
    with open('input.txt') as f:
        for line in f.readlines():
            if i % 3 == 1:
                pairs.append([eval(line.replace('\n', ''))])
            elif i % 3 == 2:
                pairs[-1].append(eval(line.replace('\n', '')))
            else:
                pass
            i += 1
    sum = 0
    for index, pair in enumerate(pairs):
        print(f"PAIR {index + 1}")
        result = recur_compare(pair[0], pair[1])
        print(result)
        if result is True:
            sum += (index + 1)
    print(sum)


def two():
    packets = [[[2]], [[6]]]
    with open('input.txt') as f:
        for line in f.readlines():
            if line != '\n':
                packets.append(eval(line.replace('\n', '')))
    sorted_packets = sorted(packets, key=functools.cmp_to_key(recur_sort_compare), reverse=True)
    result = 1
    for index, packet in enumerate(sorted_packets):
        if packet in [[[2]], [[6]]]:
            result *= (index + 1)
    print(result)


two()
