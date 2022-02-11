while True:
    #moves = input("Enter cells: ").upper()
    #if len(moves) != 9:
    #    continue
    #if not all(x in ['X', 'O', '_'] for x in moves):
    #    continue
    board = [[' ' for row in range(3)] for col in range(3)]
    break

print(f"""
---------
| {board[0][0]} {board[0][1]} {board[0][2]} |
| {board[1][0]} {board[1][1]} {board[1][2]} |
| {board[2][0]} {board[2][1]} {board[2][2]} |
---------
""")

game_state = None
x_wins = False
o_wins = False
player = 'X'

#print(game_state)

while game_state not in ('O wins', 'X wins', 'Draw'):
    try:
        coords = tuple([int(x) for x in input("Enter the coordinates: ").split()])
    except ValueError:
        print("You should enter numbers!")
        continue

    if coords[0] not in (1, 2, 3) or coords[1] not in (1, 2, 3):
        print("Coordinates should be from 1 to 3!")
        continue
    if coords == (1, 1):
        if board[0][0] == ' ':
            if player != 'O':
                board[0][0] = 'X'
                player = 'O'
            else:
                board[0][0] = 'O'
                player = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif coords == (1, 2):
        if board[0][1] == ' ':
            if player != 'O':
                board[0][1] = 'X'
                player = 'O'
            else:
                board[0][1] = 'O'
                player = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif coords == (1, 3):
        if board[0][2] == ' ':
            if player != 'O':
                board[0][2] = 'X'
                player = 'O'
            else:
                board[0][2] = 'O'
                player = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif coords == (2, 1):
        if board[1][0] == ' ':
            if player != 'O':
                board[1][0] = 'X'
                player = 'O'
            else:
                board[1][0] = 'O'
                player = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif coords == (2, 2):
        if board[1][1] == ' ':
            if player != 'O':
                board[1][1] = 'X'
                player = 'O'
            else:
                board[1][1] = 'O'
                player = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif coords == (2, 3):
        if board[1][2] == ' ':
            if player != 'O':
                board[1][2] = 'X'
                player = 'O'
            else:
                board[1][2] = 'O'
                player = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif coords == (3, 1):
        if board[2][0] == ' ':
            if player != 'O':
                board[2][0] = 'X'
                player = 'O'
            else:
                board[2][0] = 'O'
                player = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif coords == (3, 2):
        if board[2][1] == ' ':
            if player != 'O':
                board[2][1] = 'X'
                player = 'O'
            else:
                board[2][1] = 'O'
                player = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif coords == (3, 3):
        if board[2][2] == ' ':
            if player != 'O':
                board[2][2] = 'X'
                player = 'O'
            else:
                board[2][2] = 'O'
                player = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            continue

    print(f"""
---------
| {board[0][0]} {board[0][1]} {board[0][2]} |
| {board[1][0]} {board[1][1]} {board[1][2]} |
| {board[2][0]} {board[2][1]} {board[2][2]} |
---------
""")

    if abs(board.count('X') - board.count('O')) >= 2:
        game_state = 'Impossible'
    if board[0][:3] == ['X', 'X', 'X']:
        game_state = 'X wins'
        x_wins = True
    if board[0][:3] == ['O', 'O', 'O']:
        game_state = 'O wins'
        o_wins = True
    if board[1][:3] == ['X', 'X', 'X']:
        game_state = 'X wins'
        x_wins = True
    if board[1][:3] == ['O', 'O', 'O']:
        game_state = 'O wins'
        o_wins = True
    if board[2][:3] == ['X', 'X', 'X']:
        game_state = 'X wins'
        x_wins = True
    if board[2][:3] == ['O', 'O', 'O']:
        game_state = 'O wins'
        o_wins = True
    if [board[0][0], board[1][1], board[2][2]] == ['X', 'X', 'X']:
        game_state = 'X wins'
        x_wins = True
    if [board[0][0], board[1][1], board[2][2]] == ['O', 'O', 'O']:
        game_state = 'O wins'
        o_wins = True
    if board[:3][0] == ['X', 'X', 'X']:
        game_state = 'X wins'
        x_wins = True
    if board[:3][0] == ['O', 'O', 'O']:
        game_state = 'O wins'
        o_wins = True
    if board[:3][1] == ['X', 'X', 'X']:
        game_state = 'X wins'
        x_wins = True
    if board[:3][1] == ['O', 'O', 'O']:
        game_state = 'O wins'
        o_wins = True
    if board[:3][2] == ['X', 'X', 'X']:
        game_state = 'X wins'
        x_wins = True
    if board[:3][2] == ['O', 'O', 'O']:
        game_state = 'O wins'
        o_wins = True
    if [board[0][2], board[1][1], board[2][0]] == ['X', 'X', 'X']:
        game_state = 'X wins'
        x_wins = True
    if [board[0][2], board[1][1], board[2][0]] == ['O', 'O', 'O']:
        game_state = 'O wins'
        o_wins = True

    if x_wins and o_wins:
        game_state = 'Impossible'
    if game_state in ('X wins', 'O wins'):
        print(game_state)
        break
    if any(x == ' ' for y in board for x in y):
        game_state = 'Game not finished'
    else:
        game_state = 'Draw'
        print(game_state)
        break

    if game_state in ('X wins', 'O wins'):
        print(game_state)
        break
