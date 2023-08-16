from math import inf


def part_one(input_file: str) -> int:
    with open(input_file) as input:
        lines = input.readlines()

    prev = inf
    higher = 0

    for line in lines:
        depth = int(line.strip())

        if depth > prev:
            higher += 1

        prev = depth

    return higher


def sliding_window(data: list[str], size: int) -> list[list[int]]:
    windows = []

    for i in range(len(data) - size + 1):
        window = []
        for j in range(3):
            depth = int(data[i + j].strip())
            window.append(depth)
        windows.append(window)

    return windows


def part_two(input_file: str) -> int:
    with open(input_file) as input:
        lines = input.readlines()

    windows = sliding_window(lines, 3)
    higher = 0
    prev = inf

    for window in windows:
        depth_sum = sum(window)
        if depth_sum > prev:
            higher += 1
        prev = depth_sum

    return higher
