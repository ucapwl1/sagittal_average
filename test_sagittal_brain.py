#!/usr/bin/env python3
"""
Automated test for sagittal_average repository.
Exit code 0 if test passes (good commit), non-zero otherwise (bad commit).
"""

import numpy as np
import sys
from sagittal_brain import run_averages

def make_test_input(filename="brain_sample_bug.csv"):
    # create a 20×20 array, 0 except last row is 1
    data_input = np.zeros((20, 20), dtype=int)
    data_input[-1, :] = 1
    np.savetxt(filename, data_input, fmt='%d', delimiter=',')
    return filename

def load_output(filename="brain_average.csv"):
    # load the averaged row vector from output file
    return np.loadtxt(filename, delimiter=',')

def main():
    input_fname = make_test_input("brain_sample_bug.csv")
    output_fname = "brain_average.csv"
    try:
        run_averages(input_fname, output_fname)
    except Exception as e:
        print("Error when running run_averages:", e, file=sys.stderr)
        sys.exit(1)

    result = load_output(output_fname)
    # We expect each average value to equal 1/20 = 0.05
    expected_value = 1.0 / 20.0
    expected = np.full(result.shape, expected_value)

    if not np.allclose(result, expected, atol=1e-6):
        print("Test failed: result =", result, "expected =", expected, file=sys.stderr)
        sys.exit(1)

    # If we get here, it passed.
    print("Test passed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
