from functools import lru_cache


@lru_cache(maxsize=5000)
def distance(left, right):
    counter = 0
    idx = -1
    for index, cleft in enumerate(left):
        if cleft != right[index]:
            counter += 1
            idx = index
        if counter > 1:
            return None
    return idx


def part2(id_list):
    for index, input in enumerate(id_list):
        for other_input in id_list[index:]:
            dist = distance(input, other_input)
            if dist and dist >= 0:
                return input[:dist] + input[dist+1:]


def part1(id_list):
    threes = 0
    twos = 0

    for box in id_list:
        three = False
        two = False
        uniques = set(box)
        for unique in uniques:
            if box.count(unique) == 3:
                three = True
            if box.count(unique) == 2:
                two = True
        if three:
            threes += 1
        if two:
            twos += 1

    return threes * twos


with open('input.txt', 'r') as id_file:
    id_lines = id_file.readlines()

print(part1(id_lines))
print(part2(id_lines))
