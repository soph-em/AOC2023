import re

codes = open('input.txt').read().split('\n\n')
codes_to_list = codes[0].split('\n')
first_and_last_from_code = []

for code in codes_to_list:
    numbers = re.sub('\D', '', code)
    first_and_last_from_code.append(int(numbers[0] + numbers[-1]))

answer = sum(first_and_last_from_code)
print(answer)

