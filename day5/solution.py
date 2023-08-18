from collections import Counter


def process_line(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    to_int = lambda num: int(num)

    start, _, end = line.split()

    start_x, start_y = map(to_int, start.split(","))
    end_x, end_y = map(to_int, end.split(","))

    return (start_x, start_y), (end_x, end_y)


def are_on_same_axis(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[0] == b[0] or a[1] == b[1]


def get_points_in_between(
    a: tuple[int, int], b: tuple[int, int]
) -> list[tuple[int, int]]:
    points = []

    if a[0] == b[0]:
        for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
            points.append((a[0], y))

        return points

    if a[1] == b[1]:
        for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            points.append((x, a[1]))

        return points

    length = abs(a[0] - b[0])
    dir_x = 1 if a[0] < b[0] else -1
    dir_y = 1 if a[1] < b[1] else -1

    for i in range(length + 1):
        points.append((a[0] + i * dir_x, a[1] + i * dir_y))

    return points


def part_one(input_file: str) -> int:
    with open(input_file) as input:
        lines = map(lambda line: line.strip(), input.readlines())

    points = []

    for line in lines:
        start, end = process_line(line)

        if are_on_same_axis(start, end):
            points += get_points_in_between(start, end)

    counter = Counter(points)
    overlaps = [point[0] for point in counter.items() if point[1] > 1]

    return len(overlaps)


def part_two(input_file: str) -> int:
    with open(input_file) as input:
        lines = map(lambda line: line.strip(), input.readlines())

    points = []

    for line in lines:
        start, end = process_line(line)

        points += get_points_in_between(start, end)

    counter = Counter(points)
    overlaps = [point[0] for point in counter.items() if point[1] > 1]

    return len(overlaps)
