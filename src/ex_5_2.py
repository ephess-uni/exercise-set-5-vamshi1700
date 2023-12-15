""" ex_5_2.py
This module contains an entry point that

- loads data from a file `ex_5_2-data.csv` into a numpy array
- shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called `ex_5_2-processed.csv`
"""
import numpy as np

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

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

if __name__ == "__main__":

    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    # Complete the data processing steps using numpy here.

    # Save the output to OUTFILE using numpy routines.
