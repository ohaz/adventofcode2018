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
