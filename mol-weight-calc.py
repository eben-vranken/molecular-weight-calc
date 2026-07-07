from argparse import ArgumentParser

from src import parser, calculator

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("-f", "--formula", help="The formula for which the weight must be calculated")
    parser.add_argument("-v", "--verbose", action="store_true" ,help="Print a verbose table of the molecules weight")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    elements = parser.parse_formula(args.formula)
    weight = calculator.calculate_weight(elements)

    if args.verbose:
        print("Table!")

    print(f"%.3fg" % weight)