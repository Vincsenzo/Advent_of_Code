# --- Day 2 (version 2) WORKING ---
def validate(str, max):
    split = str.split(' ')
    num = int(split[1])
    if num > max:
        return True


file = open('day2data.txt', 'r')
games = file.readlines()
max_red = 12
max_green = 13
max_blue = 14
sum = 0

for game in games:
    is_possible = True
    split = game.split(':')
    game_numstr = split[0].split(' ')
    game_num = int(game_numstr[1])
    batches = split[1].split(';')
    for batch in batches:
        colornums = batch.split(',')
        red = False
        green = False
        blue = False
        for colornum in colornums:
            if 'red' in colornum:
                red = validate(colornum, max_red)
            elif 'green' in colornum:
                green = validate(colornum, max_green)
            elif 'blue' in colornum:
                blue = validate(colornum, max_blue)

        if red or green or blue is True:
            is_possible = False

    if is_possible is True:
        sum += game_num

print(sum)