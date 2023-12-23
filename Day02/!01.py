# --- Day 2 FAILED ATTEMPT ---
def findColour(color, string, max):
    print(color)
    if color in string:
        return findColor(string, max)
    else:
         pass


def findColor(string, max):
        num_col = string.split(' ')
        if int(num_col[1]) > max:
            return True
        else:
            return False


file = open('day2data.txt', 'r')
games = file.readlines()
max_red = 12
max_green = 13
max_blue = 14
sum = 0

for game in games:
    split = game.split(':')
    game_numstr = split[0].split(' ')
    game_num = int(game_numstr[1])
    print(f'Game {game_num}:')
    batches = split[1].split(';')
    for batch in batches:
        colornums = batch.split(',')
        for colornum in colornums:
            red = findColour('red', colornum, max_red)
            blue = findColour('blue', colornum, max_blue)
            green = findColour('green', colornum, max_green)
            # if any([red, blue, green]):
            #      print(game_num)

