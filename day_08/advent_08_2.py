# Advent of Code 2024
# Day 8
# Part 2

def file_to_grid(filename):
    arr = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            chars = list(line)
            arr.append(chars)
    return arr


def main() -> int:
    antinode_locations = 0
    grid = file_to_grid("input_day_08.txt")
    grid_rows = len(grid)
    grid_columns = len(grid[0])

    # Create dictionary containing a list of coordinate pairs for each
    # frequency (character) found
    antenna_chars = set()
    antenna_dict = dict()
    for row in range(grid_rows):
        for column in range(grid_columns):
            char = grid[row][column]
            if char == '.':
                continue
            coords = [row, column]
            if char in antenna_chars:
                locations = antenna_dict.get(char)
                locations.append(coords)
                antenna_dict.update({char: locations})
            else:
                antenna_chars.add(char)
                antenna_dict.update({char: [coords]})

    # Find the antinodes for each pair of antennas of the same frequency (char)
    for c in antenna_chars:
        locations = antenna_dict.get(c)
        num_spots = len(locations)
        # need more than one antenna of a particular frequency to get antinodes
        if num_spots == 1:
            continue
        for first in range(num_spots - 1):
            for second in range(first + 1, num_spots):
                pt1_row = locations[first][0]
                pt1_col = locations[first][1]
                pt2_row = locations[second][0]
                pt2_col = locations[second][1]
                delta_row = pt2_row - pt1_row
                delta_col = pt2_col - pt1_col
                # find the max possible antinodes based on grid size
                steps = max(grid_rows // delta_row, grid_columns // delta_col)
                # create all possible antinode locations and mark grid if legal
                for step in range(-steps, steps + 1):
                    antinode_row = pt1_row + (step * delta_row)
                    antinode_col = pt1_col + (step * delta_col)
                    if antinode_row >= 0 and antinode_row < grid_rows:
                        if antinode_col >= 0 and antinode_col < grid_columns:
                            grid[antinode_row][antinode_col] = '#'

    # Count up all the unique antinodes in the grid
    for row in range(grid_rows):
        for column in range(grid_columns):
            if grid[row][column] == '#':
                antinode_locations += 1

    return antinode_locations


if __name__ == "__main__":
    print(f"The number of unique antinode locations is : {main()}")
