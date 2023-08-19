from collections import Counter


def simulate_fish(fish: Counter[int], days: int) -> int:
    for _ in range(days):
        fish_to_add = fish[0]

        for k in fish.keys():
            num_fish = fish[k]

            if num_fish > 0:
                fish[k] = 0
                if k != 0:
                    fish[k - 1] += num_fish

        fish[8] += fish_to_add
        fish[6] += fish_to_add

    return fish.total()


def read_data(input: str) -> Counter[int]:
    counter = Counter({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0})
    fish = [int(num) for num in input.strip().split(",")]
    counter.update(fish)

    return counter


def part_one(input_file: str) -> int:
    with open(input_file) as input:
        fish_counter = read_data(input.readline())

    return simulate_fish(fish_counter, 80)


def part_two(input_file: str) -> int:
    with open(input_file) as input:
        fish_counter = read_data(input.readline())

    return simulate_fish(fish_counter, 256)
