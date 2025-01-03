# Advent of Code 2024
# Day 2 (Dec 2nd)
# Problem 2

def validate_report(levels):
    # returns True if record is a safe one and False if not
    how_many_levels = len(levels)
    diff = levels[1] - levels[0]
    if diff > 3 or diff < -3 or diff == 0:
        # bad record, return immediately
        return False
    good_record = True
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
    return good_record


def main():
    safe_report_count = 0
    input_file = open("input_day_02.txt", 'r')
    lines = input_file.readlines()
    for line in lines:
        text_levels = line.split()
        levels = [int(x) for x in text_levels]
        # If this report is safe, count it.  If not, try removing single
        # elements, one at a time, and check to see if that produces a
        # safe report.  Stop checking when it makes a report safe.
        if validate_report(levels):
            safe_report_count += 1
        else:
            for i in range(len(levels)):
                edited_levels = levels[0:i] + levels[i+1:]
                if validate_report(edited_levels):
                    safe_report_count += 1
                    break

    input_file.close()
    return safe_report_count


if __name__ == "__main__":
    print(f"The number of safe reports is : {main()}")
