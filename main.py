def display_legend():
    print("\n===========================")
    print("_ : Empty")
    print("x : Black (Letter Axis)")
    print("o : White (Number Axis)")
    print("===========================")


def input_dimensions():
    rows = int(input("Enter # of rows (max 99): "))
    columns = int(input("Enter # of columns (max 26): "))
    return rows, columns


def generate_board(rows, columns):
    row = list()
    for i in range(columns):
        row.append(0)  # represents empty cell

    board = list()
    for i in range(rows):
        board.append(list(row))  # new list instead of reference
    return board


def display_board(board, rows, columns):
    print()
    for y in range(rows + 2):  # considers letter axis (+2)
        if y < 1 or y > rows:  # first or last row
            print("  ", end="")
        if y < 10:  # single digit row
            print(" " * y, end="")
        else:  # double digit row
            print(" " * (y - 1), end="")
        letter_axis = "A"  # starting letter of letter axis
        for x in range(columns + 2):  # considers number axis (+2)
            if y < 1 or y > rows:  # first or last row
                print(letter_axis, end=" ")  # print letter axis
                letter_axis = chr(ord(letter_axis) + 1)
                if x > columns - 2:  # letters won't exceed number of columns
                    break
            # print number axis
            elif x < 1:  # first column
                print(y, end="")
            elif x > columns:  # last column
                print("\\" + str(y), end="")
            else:  # position is on the board
                if board[y - 1][x - 1] == 1:
                    print("\\x", end="")  # display black
                elif board[y - 1][x - 1] == 2:
                    print("\\o", end="")  # display white
                else:
                    print("\\_", end="")  # display empty
        print()


def enter_command(current_turn, board):
    if current_turn == 0:
        display_legend()
        command = input("Black's turn to move: ").upper()
    else:
        display_legend()
        command = input("White's turn to move: ").upper()

    row = ord(command[0]) - 65
    column = int(command[1:]) - 1

    if current_turn == 0:
        board[column][row] = 1
    else:
        board[column][row] = 2

    return board


if __name__ == '__main__':
    rows, columns = input_dimensions()

    board = generate_board(rows, columns)

    currentTurn = 0
    while 1:
        display_board(board, rows, columns)
        board = enter_command(currentTurn, board)
        currentTurn = (currentTurn + 1) % 2
