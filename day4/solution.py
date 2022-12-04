#! /usr/bin/env python3

def envelopes(range1, range2):
    enveloping1 = range2[0] >= range1[0] and range2[1] <= range1[1]
    enveloping2 = range1[0] >= range2[0] and range1[1] <= range2[1]
    return enveloping1 or enveloping2


def overlaps(range1, range2):
    return range2[1] >= range1[0] and range1[1] >= range2[0]


def part1():
    with open('data', 'r') as f:
        pair_assignments = [(tuple(int(coord) for coord in seg[0].split('-')),
                             tuple(int(coord) for coord in seg[1].split('-')))
                            for seg in (line.strip().split(',') for line in f.readlines())]
    print(len([seg for seg in pair_assignments if envelopes(seg[0], seg[1])]))


def part2():
    with open('data', 'r') as f:
        pair_assignments = [(tuple(int(coord) for coord in seg[0].split('-')),
                             tuple(int(coord) for coord in seg[1].split('-')))
                            for seg in (line.strip().split(',') for line in f.readlines())]
    print(len([seg for seg in pair_assignments if overlaps(seg[0], seg[1])]))


part1()
# part2()
