# Advent of Code 2024
# Day 13
# Part 2

import re

def solve(matrix, target):
    # assume transposed matrix = [[m11, m21], [m12, m22]] and target = [X, Y]
    m11 = matrix[0][0]
    m21 = matrix[0][1]
    m12 = matrix[1][0]
    m22 = matrix[1][1]
    X = target[0]
    Y = target[1]
    det = m11*m22 - m12*m21
    if det == 0:
        return [0, 0]
    else:
        return [ (m22*X - m12*Y) / det , (m11*Y - m21*X) / det ]


def main() -> int:
    total_tokens = 0
    # Each claw machine will be converted to a matrix problem
    # EXAMPLE:
    # Button A: X+94, Y+34
    # Button B: X+22, Y+67
    # Prize: X=8400, Y=5400
    # This would be converted into the matrix equation:
    # | 94  22 | A | = | 8400 |
    # | 34  67 | B | = | 5400 |
    # **** NOTE NOTE NOTE --- the matrix is transposed ***
    # "Solving" it means that...
    # A = (m22*X - m12*Y) / det(M) has an integer solution
    # B = (m11*Y - m21*X) / det(M) has an integer solution
    # A = (67*8400 - 22*5400) / (94*67 - 22*34) = 80
    # B = (94*5400 - 34*8400) / (94*67 - 22*34) = 40
    # Tokens for this machine = 3*A + B = 280

    which_line = 0
    matrix = []
    with open("input_day_13.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            if line == '':
                continue
            text_data = re.findall("[0-9]+", line)
            vector = [ int(text_data[0]), int(text_data[1]) ]
            # Python >= 3.10 can use match/case
            match which_line:
                case 0 | 1:
                    matrix.append(vector)
                    which_line += 1
                case 2:
                    vector[0] = vector[0] + 10000000000000
                    vector[1] = vector[1] + 10000000000000
                    solution = solve(matrix, vector)
                    which_line = 0
                    matrix = []
                    if solution[0].is_integer() and solution[1].is_integer():
                        A = int(solution[0])
                        B = int(solution[1])
                        total_tokens = total_tokens + 3*A + B

    return total_tokens


if __name__ == "__main__":
    print(f"The fewest tokens you need to spend is : {main()}")
