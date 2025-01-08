
def print_board(lst):
    st = '''
{}|{}|{}
-----
{}|{}|{}
-----
{}|{}|{}
'''.format(*lst)
    print(st)



# main Code 
choices = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print('Welcome to Tic Tac Toe ')
print_board(choices)
turns = 'X'
flag = True
while flag:
    while ' ' in choices:
        mv = int(input(f'Its your Turn {turns}, Your Moves [0-8] '))
        if choices[mv] == ' ':
            choices[mv] = turns
        print_board(choices)

        if choices[0] == choices[1] == choices[2] != ' ':
            print(f'-----You Won {turns} -------')
            break

        turns = 'X' if turns == '0' else '0'
    else:
        pass
    if input('Do You want to continue Y/N') == 'Y':
        choices = [' ']*9
    else:
        flag = False
else:
    print('The End')
        


