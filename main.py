import sys
import constants

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
        row.append(constants.EMPTY)

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
                if board[y - 1][x - 1] == constants.BLACK:
                    print("\\x", end="")  # display black
                elif board[y - 1][x - 1] == constants.WHITE:
                    print("\\o", end="")  # display white
                else:
                    print("\\_", end="")  # display empty
        print()


def validate_command(command):
    if command[0].isalpha() and command[1:].isdigit():
        return True
    return False


def validate_position(command):
    row = ord(command[0]) - ord("A")
    column = int(command[1:]) - 1
    return False


def enter_command(current_turn, board):
    display_legend()
    if current_turn == constants.BLACK:
        print("Black's turn to move.")
    else:
        print("White's turn to move.")

    command = input("Enter a position or command: ").upper()
    while not validate_command(command):
        if command == "QUIT":
            sys.exit(0)
        command = input("Enter a position or command: ").upper()

    row = ord(command[0]) - ord("A")
    column = int(command[1:]) - 1

    if current_turn == constants.BLACK:
        board[column][row] = constants.BLACK
        current_turn = constants.WHITE
    else:
        board[column][row] = constants.WHITE
        current_turn = constants.BLACK

    return board, current_turn


if __name__ == "__main__":
    rows, columns = input_dimensions()

    board = generate_board(rows, columns)

    current_turn = constants.BLACK
    while True:
        display_board(board, rows, columns)
        board, current_turn = enter_command(current_turn, board)
