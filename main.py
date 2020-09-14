import constants
import sys

"""
TO DO:
- end the game when a player successfully reaches a side
- implement a history system (and undo)
- implement algorithm to play against a player (solver)
- clean up code and find bugs
"""


class HexBoard:

    def __init__(self, rows=0, columns=0):
        """
        parameters: int rows (default 0) and int columns (default 0)
        attributes: int rows, int columns and 2D array containing ints
        """
        self.rows = rows
        self.columns = columns
        self.board_array = list()

        # create 2D array from rows and columns
        row_array = list()
        for x in range(self.columns):  # fill initial row with 0s
            row_array.append(constants.EMPTY)
        for y in range(self.rows):  # fill board_array with rows
            # list(row_array) uses new list instead of a reference
            self.board_array.append(list(row_array))

    def __str__(self):
        """
        displays the board in an 2D array style when using print()
        """
        for row_array in range(self.rows):
            print(self.board_array[row_array])
        return ""  # requires a string to be returned

    def display_board(self):  # TO DO: clean up messy code
        """
        displays the board into a more readable hex style board with a letter
        margin and a number margin, but uses tilted squares instead of hexagons
        """
        print()
        for y in range(self.rows + 2):  # accounts for letter axis (+2)
            # spacing for rows
            if y < 1 or y > self.rows:  # first or last row
                print("  ", end="")
            if y < 10:  # single digit row
                print(" " * y, end="")
            else:  # double digit row
                print(" " * (y - 1), end="")
            letter_axis = "A"  # starting letter of letter axis
            for x in range(self.columns + 2):  # accounts for number axis (+2)
                if y < 1 or y > self.rows:  # first or last row
                    print(letter_axis, end=" ")  # print letter axis
                    letter_axis = chr(ord(letter_axis) + 1)  # increment letter
                    if x > self.columns - 2:  # letters won't exceed number of columns
                        break
                # print number axis
                elif x < 1:  # first column
                    print(y, end="")
                elif x > self.columns:  # last column
                    print("\\" + str(y), end="")
                else:  # position is on the board
                    if self.board_array[y - 1][x - 1] == constants.BLACK:
                        print("\\x", end="")  # print black tile
                    elif self.board_array[y - 1][x - 1] == constants.WHITE:
                        print("\\o", end="")  # print white tile
                    else:
                        print("\\_", end="")  # print empty tile
            print()

    def place_stone(self, row, column, stone):
        """
        parameters: int row, int column, int stone
        places an int at the specified location, black is 1 and white is 2
        """
        self.board_array[row][column] = stone

    def valid_placement(self, row, column):
        """
        parameters: int row, int column
        checks if specified location on the board is empty and within bounds
        """
        if 0 <= row < self.rows and 0 <= column < self.columns \
                and self.board_array[row][column] == constants.EMPTY:
            return True
        return False


def input_dimension(dimension_name, max_dimension):
    """
    parameters: string dimension_name, int max_dimension
    general use function to get the input of a dimension
    """
    dimension = input(f"Enter # of {dimension_name} (max {max_dimension}): ")
    while not (dimension.isdigit() and 0 < int(dimension) <= max_dimension):
        dimension = input(f"Enter # of {dimension_name} (max {max_dimension}): ")
    return int(dimension)


def display_help():
    """
    prints a guide for the colors and their axis
    """
    print("\n===========================")
    print("_ : Empty")
    print("x : Black (Letter Axis)")
    print("o : White (Number Axis)")
    print("===========================")


def input_command(current_turn, board):
    """
    parameters: int current_turn, 2D int array board
    - takes a command and checks if its in the format A00 (LETTER NUMBER)
    then it converts the format into a position (y, x) and places a
    stone at that location
    - the color of the stone depends on whose turn it is
    - typing "quit" will exit the program
    """
    if current_turn == constants.BLACK:
        print("Black's turn.")
    else:
        print("White's turn.")

    while True:  # TO DO: reformat this into a cleaner while loop
        command = input('Enter a position (ex: B3) or type "quit" to terminate: ').upper()
        if command == "QUIT":
            print("Quitting program...")
            sys.exit(0)
        # format: A00 (LETTER NUMBER)
        if not (len(command) > 1 and command[0].isalpha() and command[1:].isdigit()):
            continue  # wrong format
        row = int(command[1:]) - 1  # 00 to row
        column = ord(command[0]) - ord("A")  # A to column
        if not board.valid_placement(row, column):
            continue  # position is occupied
        board.place_stone(row, column, current_turn)
        break

    # alternate turns
    if current_turn == constants.BLACK:
        return constants.WHITE
    return constants.BLACK


if __name__ == "__main__":
    print("Written on Python 3.8.6\nMinimum requirement: Python 3.6\n")
    rows = input_dimension("rows", constants.MAX_ROWS)
    columns = input_dimension("columns", constants.MAX_COLUMNS)
    board = HexBoard(rows, columns)

    # alternate turns and loop
    current_turn = constants.BLACK
    while True:
        board.display_board()
        display_help()
        current_turn = input_command(current_turn, board)
