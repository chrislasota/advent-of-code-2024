# Advent of Code 2024
# Day 3
# Part 1

import re

def main() -> int:
    big_sum = 0
    with open("input_day_03.txt", 'r') as input_file:
        match_pattern = "mul[(][0-9]+,[0-9]+[)]"
        for line in input_file:
            mul_list = re.findall(match_pattern, line)
            for operation in mul_list:
                numbers_str = re.findall("[0-9]+,[0-9]+", operation)
                operands = re.split(',', numbers_str[0])
                big_sum = big_sum + int(operands[0]) * int(operands[1])

    input_file.close()
    return big_sum


if __name__ == "__main__":
    print(f"The sum of all products is : {main()}")
