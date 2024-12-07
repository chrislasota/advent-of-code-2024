# Advent of Code 2024
# Day 7
# Part 1

import re

def main() -> int:
    total_calibration_result = 0
    equations = []
    with open("test.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            equations.append(line.split(': '))

    print(equations)

    return total_calibration_result


if __name__ == "__main__":
    print(f"The total calibration result is : {main()}")
