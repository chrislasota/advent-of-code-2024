# Advent of Code 2024
# Day 7
# Part 2

import re

def create_operator_combo(value, width):
    # Here we convert an integer into a string of '+', '*', and '|' chars, as
    # if it were a ternary representation, but counting down, and we return it
    # as a list.  We also prepend an extra "+" as the first operator.  All
    # that truly matters is that there's a 1-to-1 map between values and
    # unique lists of '+', '*', and '|' characters
    str = '+'
    while value > 0:
        if (value % 3) == 0:
            str = str +'+'
        if (value % 3) == 1:
            str = str + '*'
        if (value % 3) == 2:
            str = str + '|'
        value = value // 3
    while len(str) <= width:
        str = str + '+'
    return list(str)


def the_math_works(operands, operators, result):
    sum = 0
    num_operands = len(operands)
    for k in range(num_operands):
        if operators[k] == '+':
            sum = sum + operands[k]
        if operators[k] == '*':
            sum = sum * operands[k]
        if operators[k] == '|':
            sum = sum * (10**(len(str(operands[k])))) + operands[k]
    if sum == result:
        return True
    else:
        return False


def main() -> int:
    total_calibration_result = 0
    equations = []
    with open("input_day_07.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            equations.append(line.split(': '))

    # Now loop through each equation, and see if it can be made "correct"
    # using some combination of the '+', '*', and '|' operators
    for eq in equations:
        # convert target result to an integer
        result = int(eq[0])
        # grab the list of stringy operands
        operands = re.findall("[0-9]+", eq[1])
        # convert stringy operands to a list of integers
        for op_index in range(len(operands)):
            operands[op_index] = int(operands[op_index])
        # figure out how many situations we might have to try
        number_of_operators = len(operands) - 1
        number_of_combos = 3**(number_of_operators)
        # loop over each possible combination of operators
        for combo in range(number_of_combos):
            operators = create_operator_combo(combo, number_of_operators)
            if the_math_works(operands, operators, result):
                total_calibration_result += result
                break

    return total_calibration_result


if __name__ == "__main__":
    print(f"The total calibration result is : {main()}")
