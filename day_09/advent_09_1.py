# Advent of Code 2024
# Day 9
# Part 1

def file_to_diskmap(filename):
    arr = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            arr = list(line.strip())
    return arr


def main() -> int:
    checksum = 0
    diskmap = file_to_diskmap("input_day_09.txt")
    diskmap_length = len(diskmap)
    # interpret the diskmap, producing a layout list of characters from [.0-9]
    layout = []
    for file_id in range(0, diskmap_length, 2):
        file_size = int(diskmap[file_id])
        for block in range(file_size):
            layout.append(str(int(file_id / 2)))
        if file_id < diskmap_length - 2:
            gap_size = int(diskmap[file_id + 1])
            for block in range(gap_size):
                layout.append('.')

    # now compact the layout
    forward_index = 0
    backward_index = len(layout) - 1
    while forward_index != backward_index:
        if layout[forward_index] != '.':
            forward_index += 1
            continue
        else:
            while layout[backward_index] == '.':
                backward_index -= 1
                layout.pop()
            layout[forward_index] = layout[backward_index]
            backward_index -= 1
            layout.pop()

    # compute checksum
    for k in range(len(layout)):
        checksum += k * int(layout[k])

    return checksum


if __name__ == "__main__":
    print(f"The checksum is : {main()}")
