from math import prod


def part_one(input_file: str) -> int:
    with open(input_file) as input:
        lines = input.readlines()

    position = [0, 0]  # x, y

    for line in lines:
        dir, amm = line.split()

        match dir:
            case "forward":
                position[0] += int(amm)
            case "up":
                position[1] -= int(amm)
            case "down":
                position[1] += int(amm)
            case s:
                raise ValueError("Cannot parse direction " + s)

    return prod(position)


def part_two(input_file: str) -> int:
    with open(input_file) as input:
        lines = input.readlines()

    position = [0, 0, 0]  # x, y, aim

    for line in lines:
        dir, amm = line.split()

        match dir:
            case "forward":
                position[0] += int(amm)
                position[1] += int(amm) * position[2]
            case "up":
                position[2] -= int(amm)
            case "down":
                position[2] += int(amm)
            case s:
                raise ValueError("Cannot parse direction " + s)

    return prod(position[:2])
