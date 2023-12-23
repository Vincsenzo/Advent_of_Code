def firstNum(line):
    current_chars = ''

    for char in line:
        current_chars += char
        for word, number in translate.items():
            current_chars = current_chars.replace(word, str(number))

    numbers = [char for char in current_chars if char.isdigit()]
    return numbers[0]


def firstNumReverse(line):
    current_chars = ''

    for char in line[::-1]:
        current_chars = char + current_chars
        for word, number in translate.items():
            current_chars = current_chars.replace(word, str(number))

    numbers = [char for char in current_chars if char.isdigit()]
    return numbers[-1]


file = open('day1data.txt', 'r')
lines = file.readlines()
translate = {"zero": 0, "one": 1, "two":2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
solution = 0

for line in lines:
    solstr = firstNum(line) + firstNumReverse(line)
    solution += int(solstr)

print(solution)