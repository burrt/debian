import argparse

if __name__ == "__main__":

    # Create the parse object - description is the "Summary" in the Help
    # By default, it creates -h --help
    # We can override the default program name with argparse instead of sys.argv[0]
    # formatter_class for helper auto adds defaults to help information
    parser = argparse.ArgumentParser(prog="argparser",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description='Example to create an argument parser.',
                                     epilog='End of help page.')

    # Positional arguments, reads in numbers on cmd line
    # Stores the list into 'integers'
    parser.add_argument('integers',
                        nargs='+',
                        metavar='L',
                        type=int,
                        help='integers for the accumulator i.e. sum/max')

    # An accumalator which uses the list of integers and sums them
    parser.add_argument('-s', '--sum',
                        dest='sum',
                        action='store_const',
                        const=sum,
                        default=max,
                        help='sum or max the integers')

    # Basic argument to hold an int value
    # You can also use 'store_true' for Boolean values
    parser.add_argument('-v', '--var',
                        dest='var',
                        action='store', type=int,
                        help='variable to hold argument.')

    # We can accept files for input
    parser.add_argument('-i', '--stdin',
                        nargs='?',
                        type=argparse.FileType('r'),
                        help='input file to read.')

    # Parse all arguments
    # You can alternatively process partial args
    args = parser.parse_args()

    # Example use cases of the arguements
    print(args)

    # Below only works if arguments are entered
    if args.integers:
        print("Accumaltor:", args.sum(args.integers))
    if args.stdin:
        print("Reading from file:")
        print(args.stdin.readline())
