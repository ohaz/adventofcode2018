with open('input.txt', 'r') as input_file:
    changes = input_file.readlines()

frequency = 0

for change in changes:
    frequency += int(change)

print(frequency)
