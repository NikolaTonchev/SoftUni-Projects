board = [[0 for x in range(7)] for i in range(6)]


class FullColumnError(Exception):
    pass


def print_board(board):
    for i in board:
        print(i)


def is_valid_position_on_board(board, col):
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player_num
            return row, col
    raise FullColumnError


print_board(board)
turn = 1
while True:
    win_condition = 0
    player_num = 1 if turn % 2 != 0 else 2
    try:
        selected_column = int(input(f'Player {player_num}, please choose a column: '))
    except ValueError:
        print("Please enter a valid number!(1 - 7)")
        continue

    if selected_column not in range(1, 8):
        print("Please enter a valid number!(1 - 7)")
        continue

    try:
        row, col = is_valid_position_on_board(board, selected_column - 1)
    except FullColumnError:
        print('This column is full! Try another one!')
        continue

    print_board(board)
    turn += 1

#row check for win
    for s in board[row]:
        if s == player_num:
            win_condition += 1
            if win_condition == 4:
                break
        else:
            win_condition = 0

    if win_condition == 4:
        break

# column check for win
    for d in board:
        if player_num == d[col]:
            win_condition += 1
            if win_condition == 4:
                break
        else:
            win_condition = 0

    if win_condition == 4:
        break

print(f'Congratulations Player {player_num} you win!!!')
