# Advent of Code 2024
# Day 11
# Parts 1 and 2

# After some initial experimentation, I realized that as more and more
# blinks occurred, the initial set of numbers converges to a not-so-large
# set of values, meaning that we only need to keep track of how many of each
# value shows up after each blink.  This is FAR FAR more efficient than any
# kind of recursive algortihm or brute force method that would exhaust memory

import re

def file_to_list(filename) -> list:
    with open(filename, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            number_list = re.findall("[0-9]+", line)
    numbers = []
    for num_str in number_list:
        numbers.append(int(num_str))
    return numbers


def process_number(value) -> list:
    # Performs an update on input integer, producing a 1- or 2-element list
    if value == 0:
        return [1]
    digit_string = str(value)
    digit_width = len(digit_string)
    if digit_width % 2 == 0:
        left_part = digit_string[:(digit_width // 2)]
        right_part = digit_string[(digit_width // 2):]
        return [int(left_part), int(right_part)]
    else:
        return [value * 2024]


def create_histogram_from_list(input_list) -> dict:
    histogram = {}
    for k in range(len(input_list)):
        value = input_list[k]
        add_to_histogram(histogram, value, 1)
    return histogram


def add_to_histogram(histogram, value, how_many):
        histogram_key_list = list(histogram.keys())
        if value not in histogram_key_list:
            histogram.update({value: how_many})
        else:
            current_count = histogram.get(value)
            histogram.update({value: current_count + how_many})


def blink(histogram) -> dict:
    # creates a new histogram from the current one, and returns it
    new_histogram = dict()
    histogram_keys_list = list(histogram.keys())
    for value in histogram_keys_list:
        new_values = process_number(value)
        previous_count = histogram.get(value)
        add_to_histogram(new_histogram, new_values[0], previous_count)
        if len(new_values) == 2:
            add_to_histogram(new_histogram, new_values[1], previous_count)
    return new_histogram


def sum_histogram_values(histogram) -> int:
    count = 0
    histogram_keys_list = list(histogram.keys())
    for key in histogram_keys_list:
        count += histogram.get(key)
    return count



def main(how_many_blinks) -> int:
    stones = file_to_list("input_day_11.txt")
    stone_histogram = create_histogram_from_list(stones)
    for b in range(how_many_blinks):
        stone_histogram = blink(stone_histogram)
    stone_count = sum_histogram_values(stone_histogram)
    return stone_count


if __name__ == "__main__":
    total_blinks = 75
    print(f"The number of stones after {total_blinks} blinks is : {main(total_blinks)}")
