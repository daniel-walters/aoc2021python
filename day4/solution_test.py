import solution

INPUT_FILE = "day4/input_test.txt"


def test_part_one():
    assert solution.part_one(INPUT_FILE) == 4512


def test_part_two():
    assert solution.part_two(INPUT_FILE) == 1924
