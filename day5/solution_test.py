import solution

INPUT_FILE = "day5/input_test.txt"


def test_part_one():
    assert solution.part_one(INPUT_FILE) == 5


def test_part_two():
    assert solution.part_two(INPUT_FILE) == 12


def test_process_line():
    assert solution.process_line("1,2 -> 3,4") == ((1, 2), (3, 4))


class TestSameAxis:
    def test_on_x(self):
        assert solution.are_on_same_axis((1, 5), (1, 9)) == True

    def test_on_y(self):
        assert solution.are_on_same_axis((1, 5), (9, 5)) == True

    def test_not_on_axis(self):
        assert solution.are_on_same_axis((1, 5), (2, 3)) == False


class TestPointsInBetween:
    def test_horizontal(self):
        expected = [(1, 1), (2, 1), (3, 1)]
        actual = solution.get_points_in_between((1, 1), (3, 1))
        actual_reversed = solution.get_points_in_between((3, 1), (1, 1))

        assert expected.sort() == actual.sort()
        assert expected.sort() == actual_reversed.sort()

    def test_vertical(self):
        expected = [(1, 1), (1, 2), (1, 3)]
        actual = solution.get_points_in_between((1, 1), (1, 3))
        actual_reversed = solution.get_points_in_between((1, 3), (1, 1))

        assert expected.sort() == actual.sort()
        assert expected.sort() == actual_reversed.sort()

    def test_diagonal(self):
        expected = [(1, 1), (2, 2), (3, 3)]
        actual = solution.get_points_in_between((1, 1), (3, 3))
        actual_reversed = solution.get_points_in_between((3, 3), (1, 1))

        assert expected.sort() == actual.sort()
        assert expected.sort() == actual_reversed.sort()
