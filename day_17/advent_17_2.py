# Advent of Code 2024
# Day 17
# Part 2

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


def run_program(program, registers):
    output = ''
    instruction_pointer = 0  # all programs start at 0
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
                output = output + out(registers, operand) + ','
            case 6:
                bdv(registers, operand)
            case 7:
                cdv(registers, operand)

        instruction_pointer += 2
        if instruction_pointer >= len(program):
            halted = True

    return output[:-1]   # omit the last comma


def main():
    initial_registers = [0, 0, 0]  ### [A, B, C]
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
                initial_registers[input_file_line_count] = int(line[0])
                input_file_line_count += 1
                continue
            for data in line:
                program.append(int(data))

    # create a string representing the program for comparison puposes
    program_string = ''
    for digit in program:
        program_string = program_string + str(digit) + ','
    program_string = program_string[:-1]   # omit last comma

    print(f"The program code  : {program}")
    print(f"Initial registers : {initial_registers}")

    # Loop over initial values for register A until the output matches the
    # program code itself.

    # OBSERVATIONS acquired by running the code with various starting A values
    # v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v
    # The length of the output string grows monotonically with the size
    # of the initial register A value.  Furthermore, the end of the output
    # string changes at a logarithmic-like pace depending on the size of the 
    # value for register A.  So in order to efficiently find the correct
    # value for register A, we will use an adapative step_size method

    # input program string is 31 characters: "2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0"

    # In order to get an output string having a length of 31 characters,
    # we need to start with a value for register A of roughly 351843000000000
    # but we cannot exceed a value of 281475000000000 as such values produce
    # an output that is too long.

    A_MIN = 35184300000000
    A_MAX = 281475100000000
    A = A_MIN
    # A = 236581108670061 is the solution for my given input file
    delta_A = 1
    while True:
        registers = initial_registers.copy()
        registers[0] = A
        output_string = run_program(program, registers)
        print(A)
        print(output_string)
        if output_string == program_string:
            print("SUCCESS!!!")
            break
        # Adjust delta_A by how much of the end of the output string matches
        # based ONLY on observations out this code's output
        if output_string[28:] != "3,0":
            delta_A = 100000000
        if output_string[26:] == "5,3,0":
            delta_A = 10000000
        if output_string[24:] == "5,5,3,0":
            delta_A = 1000000
        if output_string[22:] == "5,5,5,3,0":
            delta_A = 10000
        if output_string[20:] == "1,5,5,5,3,0":
            delta_A = 1000
        if output_string[18:] == "1,1,5,5,5,3,0":
            delta_A = 100
        if output_string[16:] == "4,1,1,5,5,5,3,0":
            delta_A = 1
        A = A + delta_A
        if A > A_MAX:
            print("SEARCH FAILED")
            break

    return f"The initial value of A register that produces the program itself is : {A}"


if __name__ == "__main__":
    print(main())
