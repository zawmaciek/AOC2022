
import re

class Monkey_1():
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
        monkeys.append(Monkey_1(items, operator, value, test_value, target_1, target_2))
    for round in range(1, 20 + 1):
        for monkey in monkeys:
            to_throw = monkey.inspect()
            for item in to_throw:
                monkeys[item[1]].ctch(item[0])
    counts = sorted([monkey.inspect_counter for monkey in monkeys], reverse=True)
    print(counts[0] * counts[1])


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]
class Monkey_2():
    def __init__(self, items, operation, operation_value, test_value, target_1, target_2):
        self.inspect_counter = 0
        self.items = items
        self.operation = operation
        self.operation_value = operation_value
        self.test_value = test_value
        self.target_1 = target_1
        self.target_2 = target_2

    def calc(self, item):
        if self.operation_value == 'old':
            for prime in PRIMES:
                item[prime] = (item[prime] ** 2) % prime
        else:
            self.operation_value = int(self.operation_value)
            if self.operation == '*':
                for prime in PRIMES:
                    item[prime] = (item[prime] * self.operation_value) % prime
            else:
                for prime in PRIMES:
                    item[prime] = (item[prime] + self.operation_value) % prime
        return item

    def inspect(self):
        to_throw = []
        for item in self.items:
            item = self.calc(item)
            if item[self.test_value] == 0:
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


def two():
    def calc_prime_modulos(item):
        d = dict()
        for prime in PRIMES:
            d[prime] = item % prime
        return d

    with open('input.txt') as f:
        content = f.read()
    monkeys = []
    for monkey in re.findall(
            r"Monkey (\d+):\s+Starting items: (.*$)\s+Operation: new = old (.*)\s+Test: divisible by (\d+)\s+If true: throw to monkey (\d+)\s+If false: throw to monkey (\d+)",
            content, flags=re.M):
        items = [calc_prime_modulos(int(i)) for i in monkey[1].split(',')]
        operator, value = monkey[2].split()
        test_value = int(monkey[3])
        target_1 = int(monkey[4])
        target_2 = int(monkey[5])
        monkeys.append(Monkey_2(items, operator, value, test_value, target_1, target_2))
    for round in range(1, 10000 + 1):
        for monkey in monkeys:
            to_throw = monkey.inspect()
            for item in to_throw:
                monkeys[item[1]].ctch(item[0])
    counts = sorted([monkey.inspect_counter for monkey in monkeys], reverse=True)
    print(counts[0] * counts[1])


one()
two()
