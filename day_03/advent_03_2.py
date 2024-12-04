# Advent of Code 2024
# Day 3
# Part 2

import re

def main() -> int:
    big_sum = 0
    with open("input_day_03.txt", 'r') as input_file:
        match_pattern = "mul[(][0-9]+,[0-9]+[)]|do[(][)]|don't[(][)]"
        multiply_enabled = True
        for line in input_file:
            mul_list = re.findall(match_pattern, line)
            for operation in mul_list:
                if operation == "do()":
                    multiply_enabled = True
                    continue
                if operation == "don't()":
                    multiply_enabled = False
                    continue
                numbers_str = re.findall("[0-9]+,[0-9]+", operation)
                operands = re.split(',', numbers_str[0])
                if multiply_enabled:
                    big_sum = big_sum + int(operands[0]) * int(operands[1])

    input_file.close()
    return big_sum


if __name__ == "__main__":
    print(f"The sum of all products is : {main()}")