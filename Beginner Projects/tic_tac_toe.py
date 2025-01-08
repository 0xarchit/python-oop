def print_board(lst):
    st = '''
{}|{}|{}
------
{}|{}|{}
------
{}|{}|{}
'''.format(*lst)
    print(st)

# main Code
choices = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print('Welcome to the Tic Tac Toe')
print_board(choices)
turns = 'X'

while 1:
    mv = int(input(f'Its your Turn {turns}, Your Move [0-9]'))
    if choices[mv] == ' ':
        choices[mv] = turns

    print_board(choices)
    if ((choices[0] == choices[1] == choices[2] != ' ') or (choices[3] == choices[4] == choices[5] != ' ') or (choices[6] == choices[7] == choices[8] != ' ') or (choices[0] == choices[3] == choices[6] != ' ') or (choices[1] == choices[4] == choices[7] != ' ') or (choices[2] == choices[5] == choices[8] != ' ') or (choices[0] == choices[4] == choices[8] != ' ') or (choices[0] == choices[4] == choices[6] != ' ')):
        print(f'You Won {turns}')
        break
    else:
        print("Its a draw")



    turns = 'X' if turns == '0' else '0'