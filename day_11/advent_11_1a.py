# Advent of Code 2024
# Day 11
# Part 1

import re

def file_to_list(filename):
    with open(filename, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            numbers = re.findall("[0-9]+", line)
    return numbers


def main() -> int:
    stone_count = 0
    stones = file_to_list("input_day_11.txt")
    # stones is now a list of "numbers" held as strings

    num_blinks = 25
    for blinks in range(num_blinks):
        temp = []
        for stone in stones:
            # Apply the rules, appending to temp as we go
            value = int(stone)
            # Change any "0" to a "1"
            if value == 0:
                temp.append("1")
                continue
            # Split any number with an even number of digits, and compress
            # any string of '0' characters to a single '0'
            width = len(stone)
            if width % 2 == 0:
                half = width // 2
                temp.append(str(int(stone[:half])))
                temp.append(str(int(stone[half:])))
                continue
            value = value * 2024
            temp.append(str(value))
        stones = temp

    return len(stones)


if __name__ == "__main__":
    print(f"The number of stones after 25 blinks is : {main()}")
