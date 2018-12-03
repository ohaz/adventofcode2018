import re
from collections import namedtuple

Claim = namedtuple('Claim', ['id', 'left', 'top', 'width', 'height'])

repattern = re.compile('#(\d*)\s@\s(\d*),(\d*):\s(\d*)x(\d*)')


def calc_overlap(claims):
    points = {}
    for claim in claims:
        for x in range(claim.width):
            for y in range(claim.height):
                point = (claim.left + x, claim.top + y)
                points[point] = points.get(point, 0) + 1

    return points


def part1(claims):
    return len([True for element in calc_overlap(claims).values() if element > 1])


def part2(claims):
    all_claims = set()
    overlap_claims = set()
    overlap = calc_overlap(claims)
    for claim in claims:
        all_claims.add(claim.id)
        for x in range(claim.width):
            for y in range(claim.height):
                point = (claim.left + x, claim.top + y)
                if overlap[point] > 1:
                    overlap_claims.add(claim.id)
    return [cid for cid in all_claims - overlap_claims][0]


with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

read_claims = []
for line in lines:
    match = repattern.match(line)
    read_claims.append(Claim(
        id=int(match.group(1)),
        left=int(match.group(2)),
        top=int(match.group(3)),
        width=int(match.group(4)),
        height=int(match.group(5))
    ))

print(part1(read_claims))
print(part2(read_claims))