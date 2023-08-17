def part_one(input_file: str) -> int:
    with open(input_file) as input:
        cols: list[list[str]] = []

        for i, line in enumerate(input.readlines()):
            for j, ch in enumerate(line.strip()):
                if i == 0:
                    cols.append([])

                cols[j].append(ch)

    gamma = ""

    for col in cols:
        gamma += "1" if col.count("1") > col.count("0") else "0"

    epsilon = invert_binary(gamma)

    return int(gamma, 2) * int(epsilon, 2)


def part_two(input_file: str) -> int:
    with open(input_file) as input:
        nums = input.readlines()

    o2 = nums.copy()
    dig = 0
    binary_length = len(nums[0])

    while len(o2) > 1 and dig < binary_length:
        nums_at_dig = []

        for bin in o2:
            nums_at_dig.append(bin[dig])

        if nums_at_dig.count("1") >= nums_at_dig.count("0"):
            o2 = list(filter(lambda x: x.startswith("1", dig), o2))
        else:
            o2 = list(filter(lambda x: x.startswith("0", dig), o2))

        dig += 1

    oxygen_generator_rating = int(o2[0].strip(), 2)

    co2 = nums.copy()
    dig = 0

    while len(co2) > 1 and dig < binary_length:
        nums_at_dig = []

        for bin in co2:
            nums_at_dig.append(bin[dig])

        if nums_at_dig.count("1") >= nums_at_dig.count("0"):
            co2 = list(filter(lambda x: x.startswith("0", dig), co2))
        else:
            co2 = list(filter(lambda x: x.startswith("1", dig), co2))

        dig += 1

    co2_scrubber_rating = int(co2[0].strip(), 2)
    print(co2)

    return oxygen_generator_rating * co2_scrubber_rating


def invert_binary(bin: str) -> str:
    inverted = ""

    for ch in bin:
        match ch:
            case "1":
                inverted += "0"
            case "0":
                inverted += "1"
            case other:
                raise ValueError("Invalid binary num: " + other)

    return inverted
