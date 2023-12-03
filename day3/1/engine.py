import re
engine_schematic = open('test_input.txt').read().split('\n') # [[row], [row], [row]]
special_characters = '*#$/=%&-@+'

numbers = 0

# found_special_chars = {} #row_index: char_index

#finds special characters in the whole input
for row_index, row in enumerate(engine_schematic):
    for char_index, char in enumerate(row):
        if char in special_characters:
            print(numbers)
            # print(char)
            # print(re.search('[0-9]', row[char_index - 1]))
            # found_special_chars[int(row_index)] = int(char_index)

            #checks left after special character, on same row
            print(char)
            if re.match(r'[0-9]', row[char_index - 1]):
                # print(row[char_index - 3:char_index])

                number = re.search(r'(\d{1,3})', row[char_index - 3:char_index])
                # print(number)
                if number:
                    print(row + "backwards")
                    numbers += int(number.group(1))
                                    # number = '[0-9][0-9]?[0-9]?'.match(row[char_index-1:char_index-6])

            #checks right on special character, in same row
            # if 0 <= char_index < len(row) -1:
            if re.search(r'[0-9]', row[char_index + 1]):
                    # print(row)
                    number = re.search(r'(\d{1,3})', row[char_index:char_index + 3])
                    # print(number)
                    if number:
                        print(row + "forwards")
                        numbers += int(number.group(1))
            # print(engine_schematic[row_index-1])
            # print(engine_schematic[row_index-1][char_index -1])

            #checks diagnonally up and left
            if re.search(r'[0-9]', engine_schematic[row_index-1][char_index -1]):
                number = re.search(r'(\d{1,3})', engine_schematic[row_index-1][char_index - 3:char_index + 1])
                if number:
                    numbers += int(number.group(1))
                    print(row + "diagnonally up and left")
                    print(number)
            
            #checks diagonally up and right
            if re.search(r'[0-9]', engine_schematic[row_index-1][char_index +1]):
                number = re.search(r'(\d{1,3})', engine_schematic[row_index-1][char_index-2:char_index + 4])
                if number:
                    numbers += int(number.group(1))
                    print(row + "diagonally up and right")
                    print(number)

            #checks diagonally down and left
            if re.search(r'[0-9]', engine_schematic[row_index+1][char_index -1]):
                number = re.search(r'(\d{1,3})', engine_schematic[row_index+1][char_index - 3:char_index + 1])
                if number:
                    numbers += int(number.group(1))
                    print(row + "diagonally down and left")
                    print(number)

            #checks diagonally down and right
            if re.search(r'[0-9]', engine_schematic[row_index+1][char_index +1]):
                number = re.search(r'(\d{1,3})', engine_schematic[row_index+1][char_index-1:char_index + 3])
                if number:
                    numbers += int(number.group(1))
                    print(row + "diagonally down and right")
                    print(number)


print('\033[92m' + str(numbers))
# print(found_special_chars)

# for key, value in found_special_chars.items():
