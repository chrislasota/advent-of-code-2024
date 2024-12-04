# Advent of Code 2024
# Day 4
# Part 1

import re

def count_xmas_or_samx(input_string) -> int:
    match_list_forward = re.findall("XMAS", input_string)
    match_list_backward = re.findall("SAMX", input_string)
    return len(match_list_forward) + len(match_list_backward)

def main() -> int:
    xmas_count = 0
    char_array = []
    with open("input_day_04.txt", 'r') as input_file:
        for line in input_file:
            char_array.append(re.findall("[XMAS]", line))

    rows = len(char_array)
    columns = len(char_array[0])

    # check horizontally
    for row in range(rows):
        for col in range(columns - 3):
            temp_string = ""
            for k in range(4):
                temp_string = temp_string + char_array[row][col + k]
            xmas_count += count_xmas_or_samx(temp_string)

    # check vertically
    for col in range(columns):
        for row in range(rows - 3):
            temp_string = ""
            for k in range(4):
                temp_string = temp_string + char_array[row + k][col]
            xmas_count += count_xmas_or_samx(temp_string)

    # check diagonally NW-SE
    for row in range(rows - 3):
        for col in range(columns - 3):
            temp_string = ""
            for k in range(4):
                temp_string = temp_string + char_array[row + k][col + k]
            xmas_count += count_xmas_or_samx(temp_string)

    # check diagonally SW-NE
    for row in range(rows - 3):
        for col in range(3, columns):
            temp_string = ""
            for k in range(4):
                temp_string = temp_string + char_array[row + k][col - k]
            xmas_count += count_xmas_or_samx(temp_string)

    return xmas_count


if __name__ == "__main__":
    print(f"The number of time XMAS appears is : {main()}")
