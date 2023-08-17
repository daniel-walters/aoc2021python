import solution
import pytest

INPUT_FILE = "day3/input_test.txt"


def test_part_one():
    assert solution.part_one(INPUT_FILE) == 198


class TestInvertBinary:
    def test_valid(self):
        assert solution.invert_binary("10010") == "01101"

    def test_invalid(self):
        with pytest.raises(ValueError):
            solution.invert_binary("100210")


def test_part_two():
    assert solution.part_two(INPUT_FILE) == 230
