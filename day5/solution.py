#! /usr/bin/env python3

def parse_input(file):
    with open(file, 'r') as f:
        all_input = f.readlines()

    separator = all_input.index('\n')
    print(f'Separator between graph and commands is at index: {separator+1}')

    container_graph = [line.strip('\n') for line in all_input[:separator]]
    columns = len(
        [char for char in container_graph[-1].split(' ') if char != ''])
    print(f'There are: {columns} container columns')

    containers = [[] for _ in range(columns)]

    for container_row in container_graph[:-1]:
        for i in range(columns):
            if container_row[(i * 4) + 1] != ' ':
                containers[i].insert(0, container_row[(i * 4) + 1])

    commands = []
    for instruction in all_input[separator+1:]:
        command_set = []
        for word in instruction.strip().split(' '):
            if word.isdigit():
                command_set.append(int(word))
        commands.append(command_set)

    return containers, commands


def part1():
    containers, commands = parse_input('data')
    for command in commands:
        for _ in range(command[0]):
            moving = containers[command[1]-1].pop()
            containers[command[2]-1].append(moving)

    for container_column in containers:
        print(container_column.pop(), end='')
    print()


def part2():
    containers, commands = parse_input('data')
    for command in commands:
        containers[command[2] -
                   1].extend(containers[command[1]-1][-command[0]:])
        del containers[command[1]-1][-command[0]:]

    for container_column in containers:
        print(container_column.pop(), end='')
    print()


part1()
# part2()
