import argparse
import day1.solution as day1
import day2.solution as day2


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
        case day:
            raise ValueError("Day {} not implemented".format(day))

    input_file = "day{}/input.txt".format(args.day)

    print(
        "Part A: {}\nPart B: {}".format(
            solution_fn_a(input_file), solution_fn_b(input_file)
        )
    )


main()
