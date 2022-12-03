#! /usr/bin/env python3

nominal_points = {
    'A': 1,
    'B': 2,
    'C': 3
}

beats = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

loses = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}


def part1():
    points_accumulator = 0
    with open('data', 'r') as f:
        for line in f.readlines():
            calls = line.strip().split(' ')
            calls[1] = chr(ord(calls[1]) - 23)
            if calls[0] == calls[1]:
                result_points = 3
            elif beats[calls[1]] == calls[0]:
                result_points = 6
            else:
                result_points = 0
            round_points += nominal_points[calls[1]]
            points_accumulator = points_accumulator + round_points
    print(points_accumulator)


def part2():
    points_accumulator = 0
    with open('data', 'r') as f:
        for line in f.readlines():
            calls = line.strip().split(' ')
            calls[1] = chr(ord(calls[1]) - 23)
            if calls[1] == 'A':
                result_points = 0
                call_points = nominal_points[beats[calls[0]]]
            if calls[1] == 'B':
                result_points = 3
                call_points = nominal_points[calls[0]]
            if calls[1] == 'C':
                result_points = 6
                call_points = nominal_points[loses[calls[0]]]
            round_points += call_points
            points_accumulator = points_accumulator + round_points
    print(points_accumulator)


part1()
# part2()
