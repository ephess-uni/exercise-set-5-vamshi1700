""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser


if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    import argparse
    import numpy as np


    def process_data(infile, outfile):
        # Load the data from the file
        data = np.loadtxt(infile)

        # Modify the input data so that it has a mean of 0
        data -= np.mean(data)

        # Modify the zero mean data so that it has a standard deviation of 1
        data /= np.std(data)

        # Save the processed data to a file
        np.savetxt(outfile, data)


    def main():
        # Create an ArgumentParser object
        parser = argparse.ArgumentParser(
            description="This program applies a standard scale transform to the data in infile and writes it to outfile.")

        # Add positional arguments for infile and outfile
        parser.add_argument("infile", help="Input data filename")
        parser.add_argument("outfile", help="Output data filename")

        # Parse the command-line arguments
        args = parser.parse_args()

        # Call the process_data function with the provided infile and outfile
        process_data(args.infile, args.outfile)
