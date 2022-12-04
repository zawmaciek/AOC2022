def one():
    count = 0
    with open('input.txt') as f:
        for line in f.readlines():
            elve_1, elve_2 = line.split(',')
            elve_1 = [int(i) for i in elve_1.split('-')]
            elve_2 = [int(i) for i in elve_2.split('-')]
            if elve_1[0] <= elve_2[0] and elve_1[1] >= elve_2[1] or elve_2[0] <= elve_1[0] and elve_2[1] >= elve_1[1]:
                print(line)
                count += 1
    print(count)


def two():
    count = 0
    with open('input.txt') as f:
        for line in f.readlines():
            elve_1, elve_2 = line.split(',')
            elve_1 = [int(i) for i in elve_1.split('-')]
            elve_2 = [int(i) for i in elve_2.split('-')]
            if elve_2[0] <= elve_1[1] <= elve_2[1] or elve_1[0] >= elve_2[1] >= elve_1[0] or elve_1[0] <= elve_2[1] <= \
                    elve_1[1] or elve_1[1] <= elve_2[0] <= elve_1[1]:
                print(line)
                count += 1
    print(count)


two()
