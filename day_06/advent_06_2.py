# Advent of Code 2024
# Day 6
# Part 2

import re

class History:
    def __init__(self):
        self.history = []

    def add(self, event):
        self.history.append(event)

    def clear(self):
        self.history = []

    def seen(self, e):
        found_it = False
        for event in self.history:
            if e == event:
                found_it = True
        return found_it


def turn_right(current_direction) -> list:
    # current_direction is a list : [row direction, column direction]
    #
    # Matrix multiply to rotate any [row, col] direction to the right 90 deg
    #    R     *   <  ^  >  v  =   ^  >  v  <
    # | 0  1 |   | 0 -1  0  1| = |-1  0  1  0|
    # |-1  0 | * |-1  0  1  0| = | 0  1  0 -1|
    return [current_direction[1], -current_direction[0]]


def main() -> int:
    obstruction_position_count = 0

    # the grid array will be [row, column] b/c of how chars are read from file
    grid = []
    with open("input_day_06.txt", 'r') as input_file:
        for line in input_file:
            grid_chars = re.findall("[.#<^>v]", line)
            grid.append(grid_chars)
    grid_rows = len(grid)
    grid_columns = len(grid[0])

    # Find the guard's initial position
    possible_guard_chars = ['<','^','>','v']
    found_guard = False
    for initial_row in range(grid_rows):
        for initial_column in range(grid_columns):
            if grid[initial_row][initial_column] in possible_guard_chars:
                guard_char = grid[initial_row][initial_column]
                found_guard = True
                break
        if found_guard:
            break

    # Discern guard's initial direction from the guard's character.
    # next line matches        <         ^       >       v
    guard_char_directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    guard_char_index = possible_guard_chars.index(guard_char)
    initial_guard_direction = guard_char_directions[guard_char_index]

    # Now we loop over all empty positions, and place a test obstacle to see
    # if it produces a loop walk for the guard, or if the guard exits the grid.
    for ob_row in range(grid_rows):
        for ob_column in range(grid_columns):
            # place a temporary obstacle only at empty grid locations
            if grid[ob_row][ob_column] != '.':
                continue
            grid[ob_row][ob_column] = '#'

            # Now move the guard until the guard leaves grid or until the
            # guard revisits a PREVIOUS position with the SAME direction.
            # NOTE:  Paths **CONVERGE** to loops (or go off the grid), and
            # and do not have to start out as part of a loop.

            # ***** OMG THIS IS SO INEFFICIENT, but it works *****

            # Create an object to track the path history for this obstacle
            trajectory = History()
            # start from initial position and direction
            row, column = initial_row, initial_column
            guard_direction = initial_guard_direction
            while True:
                # propose a step
                next_row = row + guard_direction[0]
                next_column = column + guard_direction[1]
                # if off grid, we're done checking this temp obstacle
                if next_row < 0 or next_column < 0:
                    break
                if next_row == grid_rows or next_column == grid_columns:
                    break
                # if guard would hit obstacle, turn right
                if grid[next_row][next_column] == '#':
                    guard_direction = turn_right(guard_direction)
                    continue
                # else take the step
                row = next_row
                column = next_column
                # now check if we've been in this situation before
                event = [row, column, guard_direction[0], guard_direction[1]]
                if trajectory.seen(event):
                    obstruction_position_count += 1
                    break
                trajectory.add(event)

            # undo our temporary placement of an obstacle
            grid[ob_row][ob_column] = '.'
            # erase path history for this obstacle placement
            trajectory.clear()

    return obstruction_position_count


if __name__ == "__main__":
    print(f"The number of ideal positions for extra obstructions : {main()}")
