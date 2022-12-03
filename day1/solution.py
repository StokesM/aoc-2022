#! /usr/bin/env python3

def part1():
    with open('data', 'r') as f:
        most_cals = 0
        current_cals = 0
        for line in f.readlines():
            if line == '\n':
                if current_cals > most_cals:
                    most_cals = current_cals
                current_cals = 0
                continue
            current_cals += int(line)
    print(f'Most cals are: { most_cals }')


def part2():
    with open('data', 'r') as f:
        cal_counts = []
        current_cals = 0
        for line in f.readlines():
            if line == '\n':
                cal_counts.append(current_cals)
                current_cals = 0
                continue
            current_cals += int(line)
        total_top_three = sum(sorted(cal_counts, reverse=True)[:3])
        print(f'Total cals: { total_top_three }')


part1()
# part2()
