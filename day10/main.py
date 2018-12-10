from copy import deepcopy

best_area = None


def calculate_points(points):
    global best_area
    minx = points[0]['x']
    miny = points[0]['y']
    maxx = points[0]['x']
    maxy = points[0]['y']

    for point in points:
        minx = min(minx, point['x'])
        maxx = max(maxx, point['x'])
        miny = min(miny, point['y'])
        maxy = max(maxy, point['y'])
    area = (maxx - minx) * (maxy - miny)
    if best_area is None:
        best_area = area

    if area > best_area:
        return None

    best_area = area
    sparse_grid = {}
    for point in points:
        sparse_grid[(point['x'], point['y'])] = '#'

    return {'grid': sparse_grid, 'minx': minx, 'maxx': maxx, 'miny': miny, 'maxy': maxy}


def draw_sparse_grid(minx, maxx, miny, maxy, sparse_grid, output_file):

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            output_file.write(sparse_grid.get((x, y), '.'))
        output_file.write('\n')

    output_file.write('----------------------------------------------------------------\n\n')


def move_points(points):
    for point in points:
        point['x'] += point['xspeed']
        point['y'] += point['yspeed']
    return points


def part1(points):
    i = 0
    with open('output.txt', 'w') as output_file:
        best = calculate_points(points)
        for i in range(100_000):
            result = calculate_points(points)
            if result is not None:
                best = result
            else:
                break
            points = move_points(points)
        draw_sparse_grid(best['minx'], best['maxx'], best['miny'], best['maxy'], best['grid'], output_file)
    return i - 1


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()


input_points = []
for line in input_lines:
    posx = int(line[10:16])
    posy = int(line[18:24])
    speedx = int(line[36:38])
    speedy = int(line[40:42])
    input_points.append({'x': posx, 'y': posy, 'xspeed': speedx, 'yspeed': speedy})

print(part1(deepcopy(input_points)))
