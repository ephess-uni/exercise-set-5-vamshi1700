"""ex_5_1.py"""
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename argument from the command line
    # pass this argument to the main function above
    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    import argparse
    from ex_5_0 import line_count


    def main():
        # Create an ArgumentParser object
        parser = argparse.ArgumentParser(description="This program prints the number of lines in infile.")

        # Add a positional argument for infile
        parser.add_argument("infile", help="Input file name")

        # Parse the command-line arguments
        args = parser.parse_args()

        # Call the line_count function with the infile argument
        line_count(args.infile)
