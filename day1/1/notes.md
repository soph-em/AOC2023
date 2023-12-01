**First solution**

```python
codes = open('input.txt').read().split('\n\n')
codes_to_list = codes[0].split('\n')
first_and_last_from_code = []
print(codes_to_list)
for code in codes_to_list:
    numbers = []
    for char in code:
        if char.isnumeric():
            numbers.append(char)
    first_and_last_from_code.append(int(numbers[0] + numbers[-1]))

answer = sum(first_and_last_from_code)
print(answer)
```

This is O(n^2), wanted a more efficient solution


**Second solution** 

```python
import re

codes = open('input.txt').read().split('\n\n')
codes_to_list = codes[0].split('\n')
first_and_last_from_code = []

for code in codes_to_list:
    numbers = re.sub('\D', '', code)
    first_and_last_from_code.append(int(numbers[0] + numbers[-1]))

answer = sum(first_and_last_from_code)
print(answer)
```

re.sub is O(m * n) where m is length of the RE pattern.
possibly worse

