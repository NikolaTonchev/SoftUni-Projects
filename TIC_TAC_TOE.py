from collections import deque

player_1 = "X"
player_2 = "O"

row, col = 3, 3

board = [[" "] * col for i in range(row)]

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (1, 1),
    (1, -1),
    (-1, 1)
)

for i in board:
    print(f"| {' | '.join(i)} |")

turn = deque([[1, player_1], [2, player_2]])

while True:
    possible_coordinates = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    coordinates = int(input("Choose a free position!: "))
    a = False
    if coordinates not in possible_coordinates:
        print("Please enter a valid number!(1 - 9)")
        continue
    for s in range(row):
        current_row = 0
        if a:
            break
        for ss in range(col):
            column = 0
            if a:
                break
            for sss in possible_coordinates:
                if column == 3:
                    current_row += 1
                    column = 0

                if sss == coordinates:
                    if board[current_row][column] == " ":
                        board[current_row][column] = turn[0][1]
                        a = True
                        break
                    else:
                        print("The space is not empty!")
                        a = True
                        turn.append(turn.popleft())
                        break
                column += 1

    for i in board:
        print(f"| {' | '.join(i)} |")

    for row in range(3):
        for col in range(3):
            if board[row][col] != turn[0][1]:
                continue

            for i in directions:
                r, c = row, col

                for w in range(2):
                    r, c = r + i[0], c + i[1]

                    if not (0 <= r < 3 and 0 <= c < 3):
                        break

                    if board[r][c] != turn[0][1]:
                        break
                else:

                    print(f"Player {turn[0][0]} won the game!")
                    raise SystemExit
    turn.append(turn.popleft())
