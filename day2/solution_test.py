import solution

INPUT_FILE = "day2/input_test.txt"


def test_part_one():
    assert solution.part_one(INPUT_FILE) == 150


def test_part_two():
    assert solution.part_two(INPUT_FILE) == 900
