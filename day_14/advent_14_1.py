# Advent of Code 2024
# Day 14
# Part 1

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


def compute_safety_factor(position_list, floor_width, floor_height) -> int:
    # counts is a 4-element list holding number of robots in each quadrant
    counts = [0, 0, 0, 0]
    middle_x = floor_width // 2
    middle_y = floor_height // 2
    how_many = len(position_list)
    for robot in range(how_many):
        x, y = position_list[robot][0], position_list[robot][1]
        if x == middle_x or y == middle_y:
            continue
        if x < middle_x:
            if y < middle_y:
                counts[0] += 1
            else:
                counts[2] += 1
        else:
            if y < middle_y:
                counts[1] += 1
            else:
                counts[3] += 1

    return counts[0] * counts[1] * counts[2] * counts[3]


def main() -> int:
    safety_factor = 0
    position_list = []
    velocity_list = []
    with open("input_day_14.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            text_data = re.findall("([-]?[0-9]+)", line)
            position_list.append([ int(text_data[0]), int(text_data[1]) ])
            velocity_list.append([ int(text_data[2]), int(text_data[3]) ])

    num_robots = len(position_list)
    width, height = 101, 103
    num_seconds = 100
    position_list = move_all_robots(position_list, velocity_list, num_seconds, width, height)
    safety_factor = compute_safety_factor(position_list, width, height)
    return safety_factor


if __name__ == "__main__":
    print(f"The safety factor is : {main()}")
