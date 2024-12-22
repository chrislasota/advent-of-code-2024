# Advent of Code 2024
# Day 21
# Part 1

import re


def main() -> int:
    complexity_sum = 0
    codes = []
    with open("test.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            codes.append(list(line))

    print(codes)

    return complexity_sum


if __name__ == "__main__":
    print(f"The sum of the complexities of the five codes is : {main()}")
