import re

codes = open('input.txt').read().split('\n\n')
codes_to_list = codes[0].split('\n')
first_and_last_from_code = []

numbers_dict = {"zero": "z0o", "one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine":"n9e" }

for code in codes_to_list:
    numbers = []
    for key, value in numbers_dict.items():
        code = code.replace(key, value)

    for char in code:
        if char.isnumeric():
            numbers.append(char)
    first_and_last_from_code.append(int(numbers[0] + numbers[-1]))

answer = sum(first_and_last_from_code)
print(answer)
