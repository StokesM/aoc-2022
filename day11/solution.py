#! /usr/bin/env python3

import re
import functools

# Why couldn't the input just be valid yaml :(
monkey_pattern = '^Monkey (\d):'
items_list_pattern = '^\s*Starting items: ((?:\d*(?:(?:, )|(?=\n)))*)'
op_pattern = '^\s*Operation: new = (\w* [*/+-] \w*)'
test_pattern = '^\s*Test: divisible by (\d*)'
if_true_pattern = '^\s*If true: throw to monkey (\d*)'
if_false_pattern = '^\s*If false: throw to monkey (\d*)'


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def parse_monkeys():
    with open('data', 'r') as f:
        text = f.read()
    complete_monkeys = {}
    monkeys = re.findall(monkey_pattern, text, re.MULTILINE)
    item_lists = re.findall(items_list_pattern, text, re.MULTILINE)
    operations = re.findall(op_pattern, text, re.MULTILINE)
    tests = re.findall(test_pattern, text, re.MULTILINE)
    if_trues = re.findall(if_true_pattern, text, re.MULTILINE)
    if_falses = re.findall(if_false_pattern, text, re.MULTILINE)

    for i in range(len(monkeys)):
        complete_monkeys[int(monkeys[i])] = {'items': [int(item.strip()) for item in item_lists[i].split(',')],
                                             'operation': operations[i],
                                             'test': int(tests[i]),
                                             'if_true': int(if_trues[i]),
                                             'if_false': int(if_falses[i]),
                                             'inspections': 0}

    return complete_monkeys


def part1():
    monkeys = parse_monkeys()

    for _ in range(20):
        for monkey in sorted(monkeys):
            held_item_count = len(monkeys[monkey]['items'])
            for _ in range(held_item_count):
                item = monkeys[monkey]['items'].pop(0)
                monkeys[monkey]['inspections'] += 1
                item_operation = monkeys[monkey]['operation'].replace(
                    'old', 'item')
                item = eval(item_operation)
                item = item // 3
                if item % monkeys[monkey]['test'] == 0:
                    monkeys[monkeys[monkey]['if_true']]['items'].append(item)
                else:
                    monkeys[monkeys[monkey]['if_false']]['items'].append(item)

    inspection_counts = sorted(
        [monkeys[monkey]['inspections'] for monkey in monkeys], reverse=True)
    print(inspection_counts[0] * inspection_counts[1])


def part2():
    monkeys = parse_monkeys()

    monkey_test_numbers = [monkeys[monkey]['test'] for monkey in monkeys]
    monkey_test_product = functools.reduce(
        lambda x, y: x * y, monkey_test_numbers)
    lcm = monkey_test_product // functools.reduce(gcd, monkey_test_numbers)

    for _ in range(10000):
        for monkey in sorted(monkeys):
            held_item_count = len(monkeys[monkey]['items'])
            for _ in range(held_item_count):
                item = monkeys[monkey]['items'].pop(0)
                monkeys[monkey]['inspections'] += 1
                item_operation = monkeys[monkey]['operation'].replace(
                    'old', 'item')
                item = eval(item_operation)
                item = item % lcm
                if item % monkeys[monkey]['test'] == 0:
                    monkeys[monkeys[monkey]['if_true']]['items'].append(item)
                else:
                    monkeys[monkeys[monkey]['if_false']]['items'].append(item)

    inspection_counts = sorted(
        [monkeys[monkey]['inspections'] for monkey in monkeys], reverse=True)
    print(inspection_counts[0] * inspection_counts[1])


# part1()
part2()
