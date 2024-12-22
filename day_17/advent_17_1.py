# Advent of Code 2024
# Day 17
# Part 1

import re


def adv(regs, operand):
    # opcode = 0
    # divide A by a power of 2 -> A
    numerator = regs[0]
    match operand:
        case 0|1|2|3:
            denominator = 2 ** operand
        case 4|5|6:
            denominator = 2 ** regs[operand - 4]
    regs[0] = int(numerator / denominator)
    return


def bxl(regs, operand):
    # opcode = 1
    # bitwise XOR of B with literal value of operand -> B
    regs[1] = regs[1] ^ operand
    return


def bst(regs, operand):
    # opcode = 2
    # combo value of operand % 8 -> B
    match operand:
        case 0|1|2|3:
            regs[1] = operand
        case 4|5|6:
            regs[1] = regs[operand - 4] % 8
    return


def bxc(regs, operand):
    # opcode = 4
    # bitwise XOR of B and C -> B
    regs[1] = regs[1] ^ regs[2]
    return


def out(regs, operand):
    # opcode = 5
    # output value of combo operand
    # single digit from 0 to 7 is returned as a single character
    match operand:
        case 0|1|2|3:
            result = operand
        case 4|5|6:
            result = regs[operand - 4] % 8
    return str(result)


def bdv(regs, operand):
    # opcode = 6
    # divide A by a power of 2 -> B
    numerator = regs[0]
    match operand:
        case 0|1|2|3:
            denominator = 2 ** operand
        case 4|5|6:
            denominator = 2 ** regs[operand - 4]
    regs[1] = int(numerator / denominator)
    return


def cdv(regs, operand):
    # opcode = 7
    # divide A by a power of 2 -> C
    numerator = regs[0]
    match operand:
        case 0|1|2|3:
            denominator = 2 ** operand
        case 4|5|6:
            denominator = 2 ** regs[operand - 4]
    regs[2] = int(numerator / denominator)
    return


def main():
    output_string = ''
    registers = [0, 0, 0]  ### [A, B, C]
    instruction_pointer = 0
    input_file_line_count = 0
    program = []
    # read input file to acquire register values and program code
    with open("input_day_17.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            if line == '':
                continue
            line = re.findall("([-]?[0-9]+)", line)
            if input_file_line_count < 3:
                registers[input_file_line_count] = int(line[0])
                input_file_line_count += 1
                continue
            for data in line:
                program.append(int(data))
    print(f"The program code  : {program}")
    print(f"Initial registers : {registers}")

    halted = False
    while not halted:
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        match opcode:
            case 0:
                adv(registers, operand)
            case 1:
                bxl(registers, operand)
            case 2:
                bst(registers, operand)
            case 3:
                # do nothing if register A is zero
                if registers[0] != 0:
                    # jump, but substract 2 because we always add 2 down below
                    instruction_pointer = operand - 2
            case 4:
                bxc(registers, operand)
            case 5:
                output_string = output_string + out(registers, operand) + ','
            case 6:
                bdv(registers, operand)
            case 7:
                cdv(registers, operand)

        instruction_pointer += 2
        if instruction_pointer >= len(program):
            halted = True

    return output_string[:-1]   # omit the last comma


if __name__ == "__main__":
    print(f"The program output is : {main()}")
