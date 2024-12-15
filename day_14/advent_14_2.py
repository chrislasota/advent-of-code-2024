# Advent of Code 2024
# Day 14
# Part 2

import subprocess
import time
import re


def move_all_robots(position_list, velocity_list, steps, floor_width, floor_height) -> list:
    num_robots = len(position_list)
    for robot in range(num_robots):
        x, y = position_list[robot][0], position_list[robot][1]
        vx, vy = velocity_list[robot][0], velocity_list[robot][1]
        for step in range(steps):
            x = (x + vx) % floor_width
            y = (y + vy) % floor_height
        position_list[robot][0] = x
        position_list[robot][1] = y
    return position_list


def display_robots(position_list, floor_width, floor_height) -> None:
    floor = []
    for y in range(floor_height):
        temp_list = []
        for x in range(floor_width):
            temp_list.append(0)
        floor.append(temp_list)
    for pos in position_list:
        x, y = pos[0], pos[1]
        row = floor[y]
        tile = row[x]
        if tile == 0:
            floor[y][x] = 1
        floor[y][x] = tile + 1
    screen = []
    for y in range(floor_height):
        line = ''
        for x in range(floor_width):
            if floor[y][x] == 0:
                line = line + '.'
            else:
                line = line + chr(floor[y][x] + 48)
        screen.append(line)
    for y in range(floor_height):
        print(screen[y])
    print()
    return


def main() -> None:
    position_list = []
    velocity_list = []
    with open("input_day_14.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            if line == '':
                continue
            text_data = re.findall("([-]?[0-9]+)", line)
            position_list.append([ int(text_data[0]), int(text_data[1]) ])
            velocity_list.append([ int(text_data[2]), int(text_data[3]) ])

    num_robots = len(position_list)
    width, height = 101, 103
    display_robots(position_list, width, height)

    # Given high/low clues from AoC, I was able to narrow down the answer had
    # to be between 6000 and 10000.  Then after running code and watching the
    # output, I determined that the Easter egg was revealed on time step 6668.

    # run 6660 steps before displaying anything
    ticks = 6660
    position_list = move_all_robots(position_list, velocity_list, ticks, width, height)

    # now run another 8 steps to get the Easter Egg
    while ticks < 6668:
        # first call to shell to clear the terminal display
        subprocess.call(["clear"])
        position_list = move_all_robots(position_list, velocity_list, 1, width, height)
        ticks += 1
        print(f"Positons after {ticks} steps")
        display_robots(position_list, width, height)
        time.sleep(0.1)

    return ticks


if __name__ == "__main__":
    print(f"The Easter Egg was found on time step : {main()}")
