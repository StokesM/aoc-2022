#! /usr/bin/env python3
import string

character_priority_mapping = {char: idx+1 for (
    idx, char) in enumerate(string.ascii_letters)}


def part1():
    priority_sum = 0
    with open('data', 'r') as f:
        for backpack in f.readlines():
            compartment_one = backpack[:len(backpack)//2]
            compartment_two = backpack[len(backpack)//2:]
            mistake = set(compartment_one).intersection(compartment_two).pop()
            priority_sum += character_priority_mapping[mistake]
    print(priority_sum)


def part2():
    priority_sum = 0
    with open('data', 'r') as f:
        backpacks = [line.strip() for line in f.readlines()]
        for i in range(1, len(backpacks)-1, 3):
            badge = set(backpacks[i]).intersection(
                backpacks[i-1], backpacks[i+1]).pop()
            priority_sum += character_priority_mapping[badge]
    print(priority_sum)


part1()
# part2()
