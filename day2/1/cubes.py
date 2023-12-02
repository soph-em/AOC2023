import time
start_time = time.time()
game_round = open('input.txt').read()
#Split to list of individual rounds
round_list = game_round.split('\n')

impossible = 0
for index, content in enumerate(round_list):
    #gives rounds but into a nested list - after this it's [['game a'],['x colour, y colour', 'z colour...']]
    split = [x.split(';') for x in content.split(':')]
    #remove ['game xyz']
    split.pop(0)
    
    #stops it being a nested list, now ['number colour', 'number colour', 'number colour']
    flattened = [item for row in split for item in row]
    # print (flattened)
    
    for handful in flattened:
        #list of individual colours ['x green', 'y red'...]
        set = handful.split(',')
        # print(set)

        def list_to_dict(xs):
            tup = xs.strip().split(' ')
            return [tup[-1], int(tup[0])]

        tups = [list_to_dict(x) for x in set]
        #converted to {'red': 2, 'green': 1, 'blue': 5}
        d = dict(tups)

        if d.get('green'):
            if d.get('green') > 13:
                impossible += index + 1
                break
        
        if d.get('red'):
            if d.get('red') > 12:
                impossible += index + 1
                break
        if d.get('blue'):
            if d.get('blue') > 14:
                impossible += index + 1
                break

#5050 is sum 1-100
print(5050 - impossible)
