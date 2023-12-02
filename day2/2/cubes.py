game_round = open('input.txt').read()
round_list = game_round.split('\n')
impossible = 0
powered_sum = 0
for index, content in enumerate(round_list):
    cubes_dictionary = {'red': 0, 'green': 0, 'blue': 0}
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
            if d.get('green') > cubes_dictionary.get('green'):
                cubes_dictionary['green'] = d.get('green')

        if d.get('red'):
            if d.get('red') >  cubes_dictionary.get('red'):
                cubes_dictionary['red'] = d.get('red')
                
        if d.get('blue'):
            if d.get('blue') > cubes_dictionary.get('blue'):
                cubes_dictionary['blue'] = d.get('blue')
                
    squared = cubes_dictionary.get('blue') * cubes_dictionary.get('red') * cubes_dictionary.get('green')
    powered_sum += squared
    print(cubes_dictionary)
print(powered_sum)