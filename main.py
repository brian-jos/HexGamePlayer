import constants
import sys


class HexBoard:
    def __init__(self, rows=0, columns=0):
        self.rows = rows
        self.columns = columns
        self.board_array = list()

        row_array = list()
        for x in range(self.columns):
            row_array.append(constants.EMPTY)
        for y in range(self.rows):
            self.board_array.append(list(row_array))

    def __str__(self):
        for row_array in range(self.rows):
            print(self.board_array[row_array])
        return ""

    def display_board(self):
        print()
        for y in range(self.rows + 2):  # considers letter axis (+2)
            if y < 1 or y > self.rows:  # first or last row
                print("  ", end="")
            if y < 10:  # single digit row
                print(" " * y, end="")
            else:  # double digit row
                print(" " * (y - 1), end="")
            letter_axis = "A"  # starting letter of letter axis
            for x in range(self.columns + 2):  # considers number axis (+2)
                if y < 1 or y > self.rows:  # first or last row
                    print(letter_axis, end=" ")  # print letter axis
                    letter_axis = chr(ord(letter_axis) + 1)
                    if x > self.columns - 2:  # letters won't exceed number of columns
                        break
                # print number axis
                elif x < 1:  # first column
                    print(y, end="")
                elif x > self.columns:  # last column
                    print("\\" + str(y), end="")
                else:  # position is on the board
                    if self.board_array[y - 1][x - 1] == constants.BLACK:
                        print("\\x", end="")  # display black
                    elif self.board_array[y - 1][x - 1] == constants.WHITE:
                        print("\\o", end="")  # display white
                    else:
                        print("\\_", end="")  # display empty
            print()

    def place_stone(self, row, column, stone):
        self.board_array[row][column] = stone

    def valid_placement(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns \
                and self.board_array[row][column] == constants.EMPTY:
            return True
        return False


def input_dimension(dimension_name, max_dimension):
    dimension = input(f"Enter # of {dimension_name} (max {max_dimension}): ")
    while not (dimension.isdigit() and 0 < int(dimension) <= max_dimension):
        dimension = input(f"Enter # of {dimension_name} (max {max_dimension}): ")
    return int(dimension)


def display_help():
    print("\n===========================")
    print("_ : Empty")
    print("x : Black (Letter Axis)")
    print("o : White (Number Axis)")
    print("===========================")


def input_command(current_turn, board):
    if current_turn == constants.BLACK:
        print("Black's turn.")
    else:
        print("White's turn.")

    while True:
        command = input('Enter a position or use "quit" to terminate: ').upper()
        if command == "QUIT":
            print("Quitting program...")
            sys.exit(0)
        if not (len(command) > 1 and command[0].isalpha() and command[1:].isdigit()):
            continue
        row = int(command[1:]) - 1
        column = ord(command[0]) - ord("A")
        if not board.valid_placement(row, column):
            continue
        board.place_stone(row, column, current_turn)
        break

    if current_turn == constants.BLACK:
        return constants.WHITE
    return constants.BLACK


if __name__ == "__main__":
    rows = input_dimension("rows", 99)
    columns = input_dimension("columns", 26)
    board = HexBoard(rows, columns)

    current_turn = constants.BLACK
    while True:
        board.display_board()
        display_help()
        current_turn = input_command(current_turn, board)
