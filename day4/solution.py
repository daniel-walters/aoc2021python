from typing import Deque, Tuple
from collections import deque
from itertools import product


class Square:
    def __init__(self, num: int):
        self.num = num
        self.marked = False

    def mark_square(self):
        self.marked = True


class Bingo:
    def __init__(self, board: list[str]):
        self.board = self.__generate_board(board)
        self.finished = False

    def mark_board_and_check_win(self, num: int) -> bool:
        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                if square.num == num:
                    square.mark_square()
                    return self.__check_win((i, j))

        return False

    def count_unmarked(self) -> int:
        count = 0

        for row in self.board:
            for square in row:
                if not square.marked:
                    count += square.num

        return count

    def __generate_board(self, board_str: list[str]) -> list[list[Square]]:
        board: list[list[Square]] = []

        for row in board_str:
            nums = row.strip().split()
            board.append([Square(int(num)) for num in nums])

        return board

    def __check_win(self, recently_marked: Tuple[int, int]) -> bool:
        row, col = recently_marked
        full_row = True
        full_col = True

        for i in range(5):
            if not self.board[row][i].marked:
                full_row = False
                break

        for i in range(5):
            if not self.board[i][col].marked:
                full_col = False
                break

        if full_row or full_col:
            self.finished = True

        return full_row or full_col


def split_board_strings(board: list[str]) -> list[list[str]]:
    filtered = list(filter(lambda line: not line.startswith("\n"), board))

    boards: list[list[str]] = []

    for i in range(len(filtered) // 5):
        offset = i * 5
        boards.append(filtered[offset : offset + 5])

    return boards


def part_one(input_file: str) -> int:
    with open(input_file) as input:
        lines = input.readlines()

    bingo_nums: Deque[int] = deque()
    bingo_boards: list[Bingo] = []

    for i in lines[0].strip().split(","):
        bingo_nums.append(int(i))

    split_boards = split_board_strings(lines[1:])

    for board in split_boards:
        bingo_boards.append(Bingo(board))

    score = 0

    for num, board in product(bingo_nums, bingo_boards):
        game_over = board.mark_board_and_check_win(num)
        if game_over:
            unmarked_total = board.count_unmarked()
            score = unmarked_total * num
            break

    return score


def part_two(input_file: str) -> int:
    with open(input_file) as input:
        lines = input.readlines()

    bingo_nums: Deque[int] = deque()
    bingo_boards: list[Bingo] = []

    for i in lines[0].strip().split(","):
        bingo_nums.append(int(i))

    split_boards = split_board_strings(lines[1:])

    for board in split_boards:
        bingo_boards.append(Bingo(board))

    score = 0
    num_boards = len(bingo_boards)
    boards_won = 0

    for num, board in product(bingo_nums, bingo_boards):
        if board.finished:
            continue

        game_over = board.mark_board_and_check_win(num)
        if game_over:
            boards_won += 1
            if boards_won == num_boards:
                unmarked_total = board.count_unmarked()
                score = unmarked_total * num
                break

    return score
