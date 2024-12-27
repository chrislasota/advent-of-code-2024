# Advent of Code 2024
# Day 11
# Part 1

# This code uses a recursive strategy for Part 1

import re

def file_to_list(filename):
    with open(filename, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            numbers = re.findall("[0-9]+", line)
    return numbers


def split_or_grow(digit_string, depth) -> int:
    if depth == 0:
        return 1
    value = int(digit_string)
    if value == 0:
        return split_or_grow('1', depth - 1)
    else:
        digit_string = str(value)
    digit_width = len(digit_string)
    if digit_width % 2 == 0:
        left_part = digit_string[:(digit_width // 2)]
        right_part = digit_string[(digit_width // 2):]
        return split_or_grow(left_part, depth - 1) + split_or_grow(right_part, depth - 1)
    else:
        new_digit_string = str(value * 2024)
        return split_or_grow(new_digit_string, depth - 1)


def main(num_blinks) -> int:
    stones = file_to_list("input_day_11.txt")
    stone_count = 0
    for number_str in stones:
        stone_count += split_or_grow(number_str, num_blinks)
    return stone_count


if __name__ == "__main__":
    num_blinks = 25
    print(f"The number of stones after {num_blinks} blinks is : {main(num_blinks)}")
