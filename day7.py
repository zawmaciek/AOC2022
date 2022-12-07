def main():
    dir_sizes = []

    def two():
        unused_space = 70000000 - [dir[1] for dir in dir_sizes if dir[0] == 'GLOBAL'][0]
        missing_space = 30000000 - unused_space
        print(f"part two {sorted([dir for dir in dir_sizes if dir[1] > missing_space], key=lambda x: x[1], reverse=False)[0]}")

    def recur(tree: dict, dir_name):
        if type(tree) is int:
            return tree
        sum = 0
        for key in tree:
            if key != '__prev':
                sum += recur(tree[key], key)
        dir_sizes.append((dir_name, sum))
        return sum

    def calc(tree: dict):
        sum = 0
        recur(tree, 'GLOBAL')
        for dir in dir_sizes:
            if dir[1] <= 100000:
                sum += dir[1]
        print(f"part one: {sum}")

    with open('input.txt') as f:
        global_dict = dict()
        current_dict = global_dict
        for line in f.readlines():
            if line.startswith('$ cd'):
                if line.startswith('$ cd /'):
                    current_dict = global_dict
                elif line.startswith('$ cd ..'):
                    current_dict = current_dict['__prev']
                else:
                    target = line.split()[2]
                    current_dict = current_dict[target]
            elif line.startswith('$ ls'):
                # ignore, we can use dir and size to detect file listing
                pass
            elif line.startswith('dir '):
                dir_name = line.split()[1]
                current_dict[dir_name] = {'__prev': current_dict}
            else:
                size, name = line.split()
                current_dict[name] = int(size)
    calc(global_dict)
    two()


main()
