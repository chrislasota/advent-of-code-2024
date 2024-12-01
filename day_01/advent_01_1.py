# Advent of Code 2024
# Day 1 (Dec 1st)
# Problem 1

def main():
    sum = 0
    input_file = open("input_day_01.txt", 'r')
    lines = input_file.readlines()
    first_list = []
    second_list = []
    for line in lines:
        nums = line.split()
        first_list.append(int(nums[0]))
        second_list.append(int(nums[1]))

    first_list.sort()
    second_list.sort()
    N = len(first_list)
    for i in range(N):
        sum = sum + abs(first_list[i] - second_list[i])

    input_file.close()
    return sum


if __name__ == "__main__":
    print(f"The sum is : {main()}")
