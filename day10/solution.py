#! /usr/bin/env python3


def part1():
    with open('data', 'r') as f:
        instructions = [instruction.strip().split(' ')
                        for instruction in f.readlines()]

    register_x = 1
    ip_lock = False
    signal_strength_records = []

    for cycle in range(1, 221):
        if (cycle - 20) % 40 == 0:
            signal_strength_records.append(cycle * register_x)
        if ip_lock == False:
            try:
                process = instructions.pop(0)
            except ValueError:
                process = 'noop'
            if process[0] == 'noop':
                continue
            else:
                ip_lock = True
        else:
            ip_lock = False
            register_x += int(process[1])

    print(sum(signal_strength_records))


def part2():
    screen = [['.' for _ in range(40)] for _ in range(6)]

    with open('data', 'r') as f:
        instructions = [instruction.strip().split(' ')
                        for instruction in f.readlines()]

    register_x = 1
    ip_lock = False

    for cycle in range(0, 240):
        screen_normalised_horizontal = (cycle) % 40
        if screen_normalised_horizontal >= register_x - 1 and screen_normalised_horizontal <= register_x + 1:
            screen[(cycle) // 40][(cycle) % 40] = '#'

        if ip_lock == False:
            try:
                process = instructions.pop(0)
            except ValueError:
                process = 'noop'
            if process[0] == 'noop':
                continue
            else:
                ip_lock = True
        else:
            ip_lock = False
            register_x += int(process[1])

    for row in screen:
        for char in row:
            print(char, end='')
        print()


# part1()
part2()
