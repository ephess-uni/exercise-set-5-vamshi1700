"""ex_5_4.py"""
import numpy as np
from pathlib import Path

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

# Use these predefined paths.  Note: automated tests expect these paths
# Changing these paths will cause tests to fail.

root_dir = get_repository_root()
data_dir = root_dir / "data"
output_dir = root_dir / "outputs"
input_file = data_dir / "ex_5_4-data.csv"
output_file = output_dir / "ex_5_4-processed.csv"

# Process the input data using numpy

# Save the result to output_file
import numpy as np
from pathlib import Path

def process_and_save_data(infile, outfile):
    # Load the array from the file
    data = np.loadtxt(infile)

    # Set any negative elements of the array to 0
    data[data < 0] = 0

    # Save the processed array to a file
    np.savetxt(outfile, data)

def main():
    # Get the root directory of the repository
    root_directory = Path(__file__).resolve().parent.parent  # Assumes ex_5_4.py is in the src directory

    # Define the input and output file paths
    infile = root_directory / 'data' / 'ex_5_4-data.csv'
    outfile = root_directory / 'outputs' / 'ex_5_4-processed.csv'

    # Call the process_and_save_data function with the provided infile and outfile
    process_and_save_data(infile, outfile)