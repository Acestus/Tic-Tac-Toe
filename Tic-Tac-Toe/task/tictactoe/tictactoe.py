# write your code here
elements = input('Enter cells: ')
straights = [elements[:3], elements[3:6], elements[6:], elements[0:9:3], elements[1:9:3],
             elements[2:9:3], elements[0:9:4], elements[2:7:2]]
print('---------')
print('|', ' '.join(elements[:3]), '|')
print('|', ' '.join(elements[3:6]), '|')
print('|', ' '.join(elements[6:]), '|')
print('---------')
if abs(elements.count('X') - elements.count('O')) > 1 or ('XXX' in straights and 'OOO' in straights):
    print('Impossible')
elif 'XXX' in straights:
    print('X wins')
elif 'OOO' in straights:
    print('O wins')
elif elements.count('_') > 0:
    print('Game not finished')
elif elements.count('_') == 0:
    print('Draw')
