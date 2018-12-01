import itertools


def part1(p1_changes):
    frequency = 0

    for change in p1_changes:
        frequency += change

    return frequency


def part2(p2_changes):
    frequency = 0
    old_frequencies = [0]
    duplicate = None

    for change in itertools.cycle(p2_changes):
        frequency += change
        if frequency in old_frequencies:
            duplicate = frequency
            break
        old_frequencies.append(frequency)
    return duplicate


with open('input.txt', 'r') as input_file:
    changes = [int(x) for x in input_file.readlines()]

print(part1(changes))
print(part2(changes))
