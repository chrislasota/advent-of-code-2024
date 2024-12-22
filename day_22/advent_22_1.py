# Advent of Code 2024
# Day 22
# Part 1

def get_next_secret(secret):
    secret = (secret ^ (secret << 6))  & ((2 << 23) - 1)
    secret = (secret ^ (secret >> 5))  & ((2 << 23) - 1)
    secret = (secret ^ (secret << 11)) & ((2 << 23) - 1)
    return secret


def main():
    sum_of_2000th_secret = 0
    # read input file to acquire initial secret numbers
    with open("input_day_22.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            secret = int(line)
            for iter in range(2000):
                secret = get_next_secret(secret)
            sum_of_2000th_secret += secret

    return sum_of_2000th_secret


if __name__ == "__main__":
    print(f"The sum of the 2000th secret number for each buyer is : {main()}")
