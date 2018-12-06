def manhattan_distance(x1, x2, y1, y2):
    return abs(x1 - y1) + abs(x2 - y2)


def generate_borders(coordinates):
    leftmost = coordinates[0][0]
    rightmost = coordinates[0][0]
    topmost = coordinates[0][1]
    bottommost = coordinates[0][1]
    for coordinate in coordinates:
        if leftmost > coordinate[0]:
            leftmost = coordinate[0]
        if rightmost < coordinate[0]:
            rightmost = coordinate[0]
        if topmost > coordinate[1]:
            topmost = coordinate[1]
        if bottommost < coordinate[1]:
            bottommost = coordinate[1]

    return leftmost, rightmost, topmost, bottommost


def part1(coordinates):

    leftmost, rightmost, topmost, bottommost = generate_borders(coordinates)

    points = []

    for x in range(leftmost, rightmost + 1):
        for y in range(topmost, bottommost + 1):
            lowest_distance = manhattan_distance(x, y, coordinates[0][0], coordinates[0][1])
            lowest_index = 0
            for index, coordinate in enumerate(coordinates[1:]):
                distance = manhattan_distance(x, y, coordinate[0], coordinate[1])
                if distance < lowest_distance:
                    lowest_distance = distance
                    lowest_index = index
                elif distance == lowest_distance:
                    lowest_index = None
            points.append([x, y, lowest_index])

    for point in points:
        if point[0] == leftmost or point[0] == rightmost or point[1] == topmost or point[1] == bottommost:
            my_index = point[2]
            for other_point in points:
                if other_point[2] == my_index:
                    other_point[2] = None
            point[2] = None

    area = {}

    for point in points:
        area[point[2]] = area.get(point[2], 0) + 1

    largest_area = 0
    for key in area.keys():
        if key is None:
            continue
        if area[key] > largest_area:
            largest_area = area[key]
    return largest_area


def part2(coordinates):
    leftmost, rightmost, topmost, bottommost = generate_borders(coordinates)

    points = []

    for x in range(leftmost, rightmost + 1):
        for y in range(topmost, bottommost + 1):
            sum_distance = manhattan_distance(x, y, coordinates[0][0], coordinates[0][1])
            for index, coordinate in enumerate(coordinates[1:]):
                sum_distance += manhattan_distance(x, y, coordinate[0], coordinate[1])
            if sum_distance < 10000:
                points.append([x, y])

    return len(points)


with open('input.txt', 'r') as input_file:
    inputs = [(int(x.split(', ')[0]), int(x.split(', ')[1])) for x in input_file.readlines()]

print(part1(inputs))
print(part2(inputs))
