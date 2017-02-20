import subprocess
import random
import json
import re

moves = ['F', 'U', 'R', 'L', 'B', 'D']

last_move = None
move = None
scrambles = {}
scramble_list = []
scramble_query = ''

num_cubes = 1000
num_moves_per_scramble = 100

for x in range(num_cubes):
    current_scramble = ''
    for i in range(num_moves_per_scramble):

        move = moves[random.randint(0,len(moves)-1)]
        while last_move == move:
            move = moves[random.randint(0,len(moves)-1)]

        last_move = move
        if random.random() > 0.5:
            move += '\''

        if current_scramble == '':
            current_scramble += move
        else:
            current_scramble += ' ' + move
    scramble_list.append(current_scramble)
    scramble_query += current_scramble + '\n'

for s in scramble_list:
    #print s
    p = subprocess.Popen(['./twist.out'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out = p.communicate(input=s.encode('utf-8'))[0]
    match = re.search(r'([FBUDLR][FBUDLR] ){12}([FBUDLR][FBUDLR][FBUDLR] ?){8}', out)
    if match:
        scrambles[match.group()] = {'solution': None}
    else:
        print 'no match'

with open('output/scrambles.json', 'w') as f:
    json.dump(scrambles, f)
