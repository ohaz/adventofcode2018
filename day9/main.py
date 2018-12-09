from collections import deque

def part1(players, last_marble):
    current_marbles = deque([0])
    current_index = 0
    scores = {}
    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            points = marble
            current_marbles.rotate(7)
            points += current_marbles.popleft()
            current_player = marble % players
            scores[current_player] = scores.get(current_player, 0) + points
        else:
            current_marbles.rotate(-2)
            current_marbles.insert(0, marble)
    return max(scores.values())


with open('input.txt', 'r') as input_file:
    input_line = input_file.read().split(' ')

players = int(input_line[0])
last_marble = int(input_line[6])
print(part1(players, last_marble))
print(part1(players, last_marble * 100))
