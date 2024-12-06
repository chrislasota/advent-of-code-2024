# Advent of Code 2024
# Day 5
# Part 2

import re

def order_page_list(page_list, rule_list) -> list:
    while True:
        we_did_not_swap = True
        for rule in rule_list:
            if rule[0] not in page_list or rule[1] not in page_list:
                continue
            else:
                before_index = page_list.index(rule[0])
                after_index = page_list.index(rule[1])
                if before_index > after_index:
                    # we need to swap
                    temp = page_list[before_index]
                    page_list[before_index] = page_list[after_index]
                    page_list[after_index] = temp
                    we_did_not_swap = False
                    break
                    # after swapping re-check entire list
        if we_did_not_swap:
            break
    return page_list


def update_is_valid(rule_list, update) -> bool:
    update_length = len(update)
    for first in range(update_length - 1):
        for second in range(first + 1, update_length):
            test_pair = [update[first], update[second]]
            if test_pair not in rule_list:
                return False
    return True


def main() -> int:
    middle_page_sum = 0
    rule_list = []
    update_list = []
    reading_page_ordering_rules = True

    with open("input_day_05.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            if line == "":
                reading_page_ordering_rules = False
                continue
            temp_list = []
            page_numbers = re.findall("[0-9]+", line)
            for page in page_numbers:
                temp_list.append(int(page))
            if reading_page_ordering_rules:
                rule_list.append(temp_list)
            else:
                update_list.append(temp_list)

    for update in update_list:
        if update_is_valid(rule_list, update):
            continue
        update = order_page_list(update, rule_list)
        middle_page = update[len(update) // 2]
        middle_page_sum += middle_page

    return middle_page_sum


if __name__ == "__main__":
    print(f"The sum of the middle page numbers is : {main()}")
