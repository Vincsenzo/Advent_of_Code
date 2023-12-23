# --- Day 2, Part 2 (derived from version 2) ---
file = open('day2data.txt', 'r')
games = file.readlines()
sum = 0

for game in games:
    split = game.split(':')
    game_numstr = split[0].split(' ')
    game_num = int(game_numstr[1])
    batches = split[1].split(';')

    red_max = 0
    blue_max = 0
    green_max = 0

    for batch in batches:
        colornums = batch.split(',')
        for colornum in colornums:
            split2 = colornum.split(' ')
            split2_num = int(split2[1])
            if 'red' in colornum and split2_num > red_max:
                red_max = split2_num
            if 'blue' in colornum and split2_num > blue_max:
                blue_max = split2_num
            if 'green' in colornum and split2_num > green_max:
                green_max = split2_num

    power = red_max * green_max * blue_max
    sum += power

print(sum)