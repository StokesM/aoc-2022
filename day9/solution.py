#! /usr/bin/env python3

def part1():
    with open('data', 'r') as f:
        commands = [line.strip().split(' ') for line in f.readlines()]

    position_head = [0, 0]
    position_tail = [0, 0]
    visited = {(0, 0)}

    for command in commands:
        for _ in range(int(command[1])):
            if command[0] == 'U':
                position_head[1] += 1
            elif command[0] == 'D':
                position_head[1] -= 1
            elif command[0] == 'R':
                position_head[0] += 1
            elif command[0] == 'L':
                position_head[0] -= 1

            diff_x = position_head[0] - position_tail[0]
            diff_y = position_head[1] - position_tail[1]

            if diff_x == 2:
                position_tail[0] += 1
                if abs(diff_y) == 1:
                    position_tail[1] += diff_y
            if diff_x == -2:
                position_tail[0] -= 1
                if abs(diff_y) == 1:
                    position_tail[1] += diff_y
            if diff_y == 2:
                position_tail[1] += 1
                if abs(diff_x) == 1:
                    position_tail[0] += diff_x
            if diff_y == -2:
                position_tail[1] -= 1
                if abs(diff_x) == 1:
                    position_tail[0] += diff_x
            visited.add(tuple(position_tail))

    print(len(visited))


def part2():
    with open('data', 'r') as f:
        commands = [line.strip().split(' ') for line in f.readlines()]

    knot_chain = [[0, 0] for _ in range(10)]
    visited = {(0, 0)}

    for command in commands:
        for _ in range(int(command[1])):
            if command[0] == 'U':
                knot_chain[0][1] += 1
            elif command[0] == 'D':
                knot_chain[0][1] -= 1
            elif command[0] == 'R':
                knot_chain[0][0] += 1
            elif command[0] == 'L':
                knot_chain[0][0] -= 1

            for knot in range(1, len(knot_chain)):
                diff_x = knot_chain[knot-1][0] - knot_chain[knot][0]
                diff_y = knot_chain[knot-1][1] - knot_chain[knot][1]

                if diff_x == 2:
                    knot_chain[knot][0] += 1
                    if abs(diff_y) == 1:
                        knot_chain[knot][1] += diff_y
                if diff_x == -2:
                    knot_chain[knot][0] -= 1
                    if abs(diff_y) == 1:
                        knot_chain[knot][1] += diff_y
                if diff_y == 2:
                    knot_chain[knot][1] += 1
                    if abs(diff_x) == 1:
                        knot_chain[knot][0] += diff_x
                if diff_y == -2:
                    knot_chain[knot][1] -= 1
                    if abs(diff_x) == 1:
                        knot_chain[knot][0] += diff_x
                visited.add(tuple(knot_chain[len(knot_chain) - 1]))

    print(len(visited))


# part1()
part2()
