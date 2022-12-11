import re


class Monkey():
    def __init__(self, items, operation, operation_value, test_value, target_1, target_2):
        self.inspect_counter = 0
        self.items = items
        self.operation = operation
        self.operation_value = operation_value
        self.test_value = test_value
        self.target_1 = target_1
        self.target_2 = target_2
        if operation_value == 'old':
            self.calc = lambda x: x ** 2
        else:
            self.operation_value = int(self.operation_value)
            if operation == '*':
                self.calc = lambda x: x * self.operation_value
            else:
                self.calc = lambda x: x + self.operation_value

    def inspect(self):
        to_throw = []
        for item in self.items:
            item = self.calc(item) // 3
            if item % self.test_value == 0:
                to_throw.append((item, self.target_1))
            else:
                to_throw.append((item, self.target_2))
            self.inspect_counter += 1
        self.items = []
        return to_throw

    def ctch(self, item):
        self.items.append(item)

    def __repr__(self):
        return str(self.items)


def one():
    with open('sample.txt') as f:
        content = f.read()
    monkeys = []
    for monkey in re.findall(
            r"Monkey (\d+):\s+Starting items: (.*$)\s+Operation: new = old (.*)\s+Test: divisible by (\d+)\s+If true: throw to monkey (\d+)\s+If false: throw to monkey (\d+)",
            content, flags=re.M):
        items = [int(i) for i in monkey[1].split(',')]
        operator, value = monkey[2].split()
        test_value = int(monkey[3])
        target_1 = int(monkey[4])
        target_2 = int(monkey[5])
        monkeys.append(Monkey(items, operator, value, test_value, target_1, target_2))
    for round in range(1, 20 + 1):
        print(f"ROUND: {round}")
        for monkey in monkeys:
            to_throw = monkey.inspect()
            for item in to_throw:
                monkeys[item[1]].ctch(item[0])
        print(monkeys)
    counts = sorted([monkey.inspect_counter for monkey in monkeys], reverse=True)
    print(counts[0] * counts[1])

one()
