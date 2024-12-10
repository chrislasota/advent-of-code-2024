# Advent of Code 2024
# Day 9
# Part 2

def file_to_diskmap(filename):
    arr = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            arr = list(line.strip())
    return arr


def main() -> int:
    checksum = 0
#    diskmap = file_to_diskmap("input_day_09.txt")
    diskmap = file_to_diskmap("test.txt")
    diskmap_length = len(diskmap)

    # convert diskmap to layout
    layout = []
    file_id = 0
    index = 0
    while index < diskmap_length:
        block_size = int(diskmap[index])
        if index % 2 == 0:
            for block in range(block_size):
                layout.append(str(int(file_id)))
            file_id += 1
        else:
            for block in range(block_size):
                layout.append('.')
        index += 1

    print(layout)

    # ALGORITHM FOR COMPRESSION
    # need to walk backward through layout
    # find groups of identical file ids, getting their size
    # once a size is found
    # walk forward from beginning of layout to find a gap of suitable size
    # if possible, overwrite the blanks with the file ids.
    # continue the backward walk finding groups of identical file ids

    backward_index = len(layout) - 1
    counting_blocks = False
    while backward_index > 0:
        block = layout[backward_index]
        if block == '.' and counting_blocks == False:
            # skip past empty blocks
            backward_index -= 1
            continue
        if block != '.' and counting_blocks == False:
            # we just found the right end of a file
            file_id = block
            counting_blocks = True
            block_count = 1
            backward_index -= 1
            continue
        if block == file_id and counting_blocks == True:
            # continue counting blocks for this file
            block_count += 1
            backward_index -= 1
            continue
        if block != file_id and counting_blocks == True:
            # we found the full file size
            # Now scan from left for a blank gap of suitable size
            file_size = block_count
            blank_count = 0
            counting_blocks = False
            for k in range(backward_index):
                if layout[k] == '.':
                    blank_count += 1
                    if blank_count == file_size:
                        # we found a gap for the file, so write it in the gap
                        # and erase it from the previous position in layout
                        for j in range(file_size):
                            layout[k - j] = file_id
                            layout[backward_index + j + 1] = '.'
                        break
                else:
                    blank_count = 0

    print(layout)
    # compute checksum
    for k in range(len(layout)):
        if layout[k] == '.':
            continue
        checksum += k * int(layout[k])

    return checksum


if __name__ == "__main__":
    print(f"The checksum is : {main()}")
