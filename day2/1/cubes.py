game_round = open('input.txt').read()
round_list = game_round.split('\n')

impossible = 0
for index, content in enumerate(round_list):
    split = [x.split(';') for x in content.split(':')]
    split.pop(0)
    
    flattened = [item for row in split for item in row]
    
    for handful in flattened:
        set = handful.split(',')

        def list_to_dict(xs):
            tup = xs.strip().split(' ')
            return [tup[-1], int(tup[0])]

        tups = [list_to_dict(x) for x in set]
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
