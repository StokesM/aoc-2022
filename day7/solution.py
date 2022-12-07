#! /usr/bin/env python3

class Node:
    def __init__(self, name=None, parent=None, children=None, size=0) -> None:
        self.name = name
        self.parent = parent
        if children is None:
            self.children = []
        self.files_size = size

    def __str__(self) -> str:
        return (f'Node: {self.name}')

    def node_info(self) -> str:
        child_string = ' | '.join([str(child) for child in self.children])
        return (
            f'''Node: {self.name}
Parent: {str(self.parent)}
Children: {str(child_string)}
Total Size: {self.node_size()}''')

    def node_size(self) -> int:
        total_size = self.files_size
        for node in self.children:
            total_size += node.node_size()
        return total_size


def terminal_output_to_file_tree(terminal_output_lines):
    current_node = Node()
    fs_nodes = [current_node]

    for line in terminal_output_lines:
        commands = line.split(' ')
        if commands[0] == '$':
            if commands[1] == 'cd':
                if commands[2] == '..':
                    current_node = current_node.parent
                else:
                    next_node = Node(
                        name=commands[2], parent=current_node)
                    current_node.children.append(next_node)
                    current_node = next_node
                    fs_nodes.append(current_node)
        elif commands[0] == 'dir':
            continue
        else:
            current_node.files_size += int(commands[0])
    return fs_nodes


def part1(file_name='data'):
    with open(file_name, 'r') as f:
        terminal_output = [line.strip() for line in f.readlines()]
    fs = terminal_output_to_file_tree(terminal_output)
    candidate_nodes = filter(lambda node: node.node_size() <= 100000, fs)
    print(sum([node.node_size() for node in candidate_nodes]))


def part2(file_name='data'):
    with open(file_name, 'r') as f:
        terminal_output = [line.strip() for line in f.readlines()]
    fs = terminal_output_to_file_tree(terminal_output)
    need_to_free = 30000000-(70000000 - fs[0].node_size())
    delete_me = sorted(
        filter(lambda node: node.node_size() >= need_to_free, fs), key=lambda delete_candidate: delete_candidate.node_size())[0]
    print(delete_me.node_size())


part1()
# part2()
