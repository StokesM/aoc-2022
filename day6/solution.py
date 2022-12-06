#! /usr/bin/env python3

def part1():
    with open('data', 'r') as f:
        signal_buffer = f.read()

    for end_packet_buffer_index in range(4, len(signal_buffer)):
        start_packet_buffer = set(signal_buffer[end_packet_buffer_index -
                                                4:end_packet_buffer_index])
        if len(start_packet_buffer) == 4:
            return end_packet_buffer_index


def part2():
    with open('data', 'r') as f:
        signal_buffer = f.read()

    for end_packet_buffer_index in range(14, len(signal_buffer)):
        start_packet_buffer = set(signal_buffer[end_packet_buffer_index -
                                                14:end_packet_buffer_index])
        if len(start_packet_buffer) == 14:
            return end_packet_buffer_index


print(part1())
# print(part2())
