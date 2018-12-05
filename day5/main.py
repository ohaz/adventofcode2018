import string


def part1(line):
    killers = [x+x.lower() for x in string.ascii_uppercase] + [x.lower()+x for x in string.ascii_uppercase]
    while True:
        counter = 0
        for killer in killers:
            if line.find(killer) >= 0:
                newline = line[:line.find(killer)] + line[line.find(killer)+2:]
                if len(newline) < len(line):
                    counter += 1
                    line = newline
        if counter == 0:
            break
    return len(line)


with open('input.txt', 'r') as input_file:
    input_line = input_file.readline()

print(part1(input_line))