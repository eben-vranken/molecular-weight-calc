from argparse import ArgumentParser

from src import parser, calculator

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("-f", "--formula", help="The formula for which the weight must be calculated")
    parser.add_argument("-v", "--verbose", action="store_true" ,help="Print a verbose table of the molecules weight")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    if not args.formula:
        print("Error: Please provide a formula using -f or --formula")
        exit(1)

    try:
        elements = parser.parse_formula(args.formula)
        weight = calculator.calculate_weight(elements)
    except calculator.UnknownElementError as e:
        print(f"Error: {e}")
        exit(1)
        
    if args.verbose:
        print(f"\nDetailed Breakdown for {args.formula}:")
        print("-" * 42)
        print("%-8s %6s %12s %12s" % ("Element", "Count", "Unit Mass", "Total Mass"))
        print("-" * 42)

        for elem, count in elements.items():
            unit_mass = calculator.atomic_weights.get(elem, 0.0)
            elem_total = unit_mass * count
            print("%-8s %6d %12.3f %12.3f" % (elem, count, unit_mass, elem_total))
    
        print("-" * 42)
        print(f"Total Molecular Weight: {weight:.3f}g\n")

    else:
        print(f"%.3fg" % weight)