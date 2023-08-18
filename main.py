import argparse
import day1.solution as day1
import day2.solution as day2
import day3.solution as day3
import day4.solution as day4
import day5.solution as day5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--day", required=True, help="The day to run")
    args = ap.parse_args()

    solution_fn_a = None
    solution_fn_b = None
    input_file = ""

    match int(args.day):
        case 1:
            solution_fn_a = day1.part_one
            solution_fn_b = day1.part_two
        case 2:
            solution_fn_a = day2.part_one
            solution_fn_b = day2.part_two
        case 3:
            solution_fn_a = day3.part_one
            solution_fn_b = day3.part_two
        case 4:
            solution_fn_a = day4.part_one
            solution_fn_b = day4.part_two
        case 5:
            solution_fn_a = day5.part_one
            solution_fn_b = day5.part_two
        case day:
            raise ValueError("Day {} not implemented".format(day))

    input_file = "day{}/input.txt".format(args.day)

    print(
        "Part A: {}\nPart B: {}".format(
            solution_fn_a(input_file), solution_fn_b(input_file)
        )
    )


main()
