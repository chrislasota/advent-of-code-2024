# Advent of Code 2024
# Day 4
# Part 2

import re

def count_mas_or_sam(input_string) -> int:
    match_list = re.findall("MAS|SAM", input_string)
    return len(match_list)


def main() -> int:
    x_mas_count = 0
    char_array = []
    with open("input_day_04.txt", 'r') as input_file:
        for line in input_file:
            char_array.append(re.findall("[XMAS]", line))

    rows = len(char_array)
    columns = len(char_array[0])

    for row in range(rows - 2):
        for col in range(columns - 2):
            if char_array[row+1][col+1] != 'A':
                continue
            frwd_slash = (char_array[row][col]
                         + char_array[row+1][col+1]
                         + char_array[row+2][col+2])

            back_slash = (char_array[row][col+2]
                         + char_array[row+1][col+1]
                         + char_array[row+2][col])

            x_mas_count += (count_mas_or_sam(frwd_slash)
                           * count_mas_or_sam(back_slash))
    return x_mas_count


if __name__ == "__main__":
    print(f"The number of X-MAS occurences is : {main()}")
