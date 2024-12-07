# Advent of Code 2024
# Day 6
# Part 1

import re

def turn_right(current_direction) -> list:
    row_dir = current_direction[1]
    column_dir = -current_direction[0]
    return [row_dir, column_dir]


def main() -> int:
    distinct_positions = 0
    # the grid array will be [row, column] b/c of how chars are read from file
    grid = []
    possible_guard_chars = ['<','^','>','v']

    with open("input_day_06.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            grid_chars = re.findall("[.#<^>v]", line)
            grid.append(grid_chars)
    grid_rows = len(grid)
    grid_columns = len(grid[0])

    # Find the guard's initial position
    found_guard = False
    for row in range(grid_rows):
        for column in range(grid_columns):
            if grid[row][column] in possible_guard_chars:
                guard_char = grid[row][column]
                found_guard = True
                break
        if found_guard:
            break

    # Discern guard's initial direction from the guard's character
    # next line matches         <         ^       >       v
    guard_char_directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    guard_char_index = possible_guard_chars.index(guard_char)
    guard_direction = guard_char_directions[guard_char_index]

    # Now walk and turn, leaving trace, until guard leaves the grid
    while True:
        # leave trace
        grid[row][column] = 'X'
        # propose a step
        row_direction = guard_direction[0]
        column_direction = guard_direction[1]
        next_row = row + row_direction
        next_column = column + column_direction
        # if off grid, we're done
        if next_row < 0 or next_column < 0:
            break
        if next_row == grid_rows or next_column == grid_columns:
            break
        # if guard would hit obstacle, turn right
        if grid[next_row][next_column] == '#':
            guard_direction = turn_right(guard_direction)
        # else take the step
        else:
            row = next_row
            column = next_column

    # now total up all traces -- distinct positions
    for row in range(grid_rows):
        for column in range(grid_columns):
            if grid[row][column] == 'X':
                distinct_positions += 1
    return distinct_positions


if __name__ == "__main__":
    print(f"The number of distinct positions is : {main()}")
