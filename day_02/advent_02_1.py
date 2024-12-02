# Advent of Code 2024
# Day 2 (Dec 2nd)
# Problem 1

def main():
    safe_report_count = 0
    input_file = open("input_day_02.txt", 'r')
    lines = input_file.readlines()
    for line in lines:
        text_levels = line.split()
        levels = [int(x) for x in text_levels]
        how_many_levels = len(levels)
        diff = levels[1] - levels[0]
        good_record = True
        if diff > 3 or diff < -3 or diff == 0:
            # bad record, skip to next record immediately
            continue
        if diff > 0:
            direction = "increasing"
        if diff < 0:
            direction = "decreasing"
        for index in range(1, how_many_levels - 1):
            diff = levels[index + 1] - levels[index]
            if direction == "increasing" and diff <= 0:
                # bad record
                good_record = False
                break
            if direction == "increasing" and diff > 3:
                # bad record
                good_record = False
                break
            if direction == "decreasing" and diff >= 0:
                # bad record
                good_record = False
                break
            if direction == "decreasing" and diff < -3:
                # bad record
                good_record = False
                break

        if good_record:
            safe_report_count += 1

    input_file.close()
    return safe_report_count


if __name__ == "__main__":
    print(f"The number of safe reports is : {main()}")
