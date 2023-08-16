import solution

INPUT_FILE = "day1/input_test.txt"


def test_part_one():
    assert solution.part_one(INPUT_FILE) == 7


def test_part_two():
    assert solution.part_two(INPUT_FILE) == 5


def test_sliding_window():
    test_list = ["123", "234", "345", "456", "567"]
    assert solution.sliding_window(test_list, 3) == [
        [123, 234, 345],
        [234, 345, 456],
        [345, 456, 567],
    ]
