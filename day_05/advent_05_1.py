# Advent of Code 2024
# Day 5
# Part 1

import re

def update_is_valid(page_order_rule_list, update) -> bool:
    update_length = len(update)
    for first in range(update_length - 1):
        for second in range(first + 1, update_length):
            test_pair = [update[first], update[second]]
            if test_pair not in page_order_rule_list:
                return False
    return True


def main() -> int:
    middle_page_sum = 0
    page_order_rule_list = []
    update_list = []
    reading_page_ordering_rules = True

    with open("input_day_05.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            if line == "":
                reading_page_ordering_rules = False
                continue
            page_numbers = re.findall("[0-9]+", line)
            temp_list = []
            for page in page_numbers:
                temp_list.append(int(page))
            if reading_page_ordering_rules:
                page_order_rule_list.append(temp_list)
            else:
                update_list.append(temp_list)

    for update in update_list:
        if update_is_valid(page_order_rule_list, update):
            middle_page = update[len(update) // 2]
            middle_page_sum += middle_page

    return middle_page_sum


if __name__ == "__main__":
    print(f"The sum of the middle page numbers is : {main()}")
