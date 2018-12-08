from copy import copy

all_metas = []


def p1_parse_current(area):
    children = area[0]
    metadatas = area[1]
    consumed = 2
    for _ in range(children):
        consumed += p1_parse_current(area[consumed:])
    for _ in range(metadatas):
        all_metas.append(area[consumed])
        consumed += 1
    return consumed


def part1(line):
    parsed = p1_parse_current(line[0:])
    if parsed != len(line):
        print('parsed too short:', parsed, len(line))
    return sum(all_metas)


def p2_parse_current(area):
    children = area[0]
    metadatas = area[1]
    consumed = 2
    children_meta = []
    value = 0
    for _ in range(children):
        child_consumed, child_value = p2_parse_current(area[consumed:])
        consumed += child_consumed
        children_meta.append(child_value)
    for _ in range(metadatas):
        meta_value = area[consumed] - 1
        if meta_value < len(children_meta):
            value += children_meta[meta_value]
        if len(children_meta) == 0:
            value += meta_value + 1
        consumed += 1
    return consumed, value


def part2(line):
    parsed, value = p2_parse_current(line[0:])
    if parsed != len(line):
        print('parsed too short:', parsed, len(line))
    return value


with open('input.txt', 'r') as input_file:
    input_line = [int(x) for x in input_file.read().split(' ')]

print(part1(copy(input_line)))
print(part2(copy(input_line)))
