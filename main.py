"""
TO DO:
- end the game when a player successfully reaches a side
- implement swap rule
- implement algorithm to play against a player (solver)
- clean up code and find bugs
"""

# constants
EMPTY = 0
BLACK = 1
WHITE = 2
MAX_ROWS = 99
MAX_COLUMNS = 26

class HexBoard:

    def __init__(self, rows, columns):
        """
        parameters: int rows and int columns
        attributes: int rows, int columns and 2D array containing ints,
        1D array containing tuples of ints
        """
        self.rows = rows
        self.columns = columns
        self.board_array = list()
        self.history = list()  # (y, x, stone_color)

        # create 2D array from rows and columns
        row_array = list()
        for x in range(self.columns):  # fill initial row with 0s
            row_array.append(EMPTY)
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

    def display_board(self):  # TO DO: clean up loops and use less if statements
        """
        displays the board into a more readable hex style board with a letter
        margin and a number margin, but uses angled squares instead of hexagons
        """
        spacing_offset = 0  # progressive spacing
        print()
        for y in range(self.rows + 2):  # accounts for letter axis (+2)
            # spacing for rows
            if y < 1:  # first row
                print(end=" ")
            if 9 < y <= self.rows:  # double digit row (excluding last row)
                print(end=" " * (y - 1))
            else:  # single digit row
                print(end=" " * y)
            for x in range(self.columns + 2):  # accounts for number axis (+2)
                if y < 1 or y > self.rows:  # first or last row
                    print(" ", end=chr(x + ord("A")))  # print letter axis
                    if x > self.columns - 2:  # letters won't exceed number of columns
                        break
                elif x < 1:  # first column
                    print(end=str(y))  # print number axis
                elif x > self.columns:  # last column
                    print("\\", end=str(y))
                else:  # position is on the board
                    if self.board_array[y - 1][x - 1] == BLACK:
                        print(end="\\x")  # print black tile
                    elif self.board_array[y - 1][x - 1] == WHITE:
                        print(end="\\o")  # print white tile
                    else:
                        print(end="\\_")  # print empty tile
            print("\n", end=" " * spacing_offset)  # adds progressive spacing
            spacing_offset += 1  # increase progressive spacing

    def place_stone(self, row, column, stone):
        """
        parameters: int row, int column, int stone
        places an int at the specified location, black is 1 and white is 2
        """
        self.board_array[row][column] = stone
        self.history.append((row, column, stone))

    def undo_placement(self):
        """
        replaces the last position in history with an empty stone
        """
        row, column, stone = self.history[-1]
        self.board_array[row][column] = EMPTY
        self.history.pop()

    def valid_placement(self, row, column):
        """
        parameters: int row, int column
        checks if specified location on the board is empty and within bounds
        """
        if 0 <= row < self.rows and 0 <= column < self.columns \
                and self.board_array[row][column] == EMPTY:
            return True
        return False


def input_dimension(dimension_name, max_dimension):
    """
    parameters: string dimension_name, int max_dimension
    general use function to get the input of a dimension
    """
    dimension = input("Enter # of " + dimension_name \
                      + " (max " + str(max_dimension) + "): ")
    while not (dimension.isdigit() and 0 < int(dimension) <= max_dimension):
        dimension = input("Enter # of " + dimension_name \
                          + " (max " + str(max_dimension) + "): ")
    return int(dimension)


def display_guide():
    """
    prints a guide for the colors and their axis
    """
    print("\n===========================")
    print("_ : Empty")
    print("x : Black (Letter Axis)")
    print("o : White (Number Axis)")
    print("===========================")


def display_help():
    print('\n"help" = display a list of available commands')
    print('"undo" = undo the last placement')
    print('"quit" = terminate the program\n')


def input_command(current_turn, board):  # TO DO: reformat this into a cleaner while loop
    """
    parameters: int current_turn, 2D int array board
    - takes a command and checks if its in the format A00 (LETTER NUMBER)
    then it converts the format into a position (y, x) and places a
    stone at that location
    - the color of the stone depends on whose turn it is
    - typing "quit" will exit the program
    """
    if current_turn == BLACK:
        print("Black's turn.")
    else:
        print("White's turn.")

    while True:
        command = input('Enter a position (ex: "B3") or a command (ex: "help"): ').upper()
        if command == "QUIT":
            return "QUIT"
        if command == "HELP":
            display_help()
        if command == "UNDO" and len(board.history) > 0:
            board.undo_placement()
            break
        # format: A00 (LETTER NUMBER)
        if not (len(command) > 1 and command[0].isalpha() and command[1:].isdigit()):
            continue  # wrong format
        row = int(command[1:]) - 1  # 00 to row
        column = ord(command[0]) - ord("A")  # A to column
        if not board.valid_placement(row, column):
            continue  # position is occupied
        board.place_stone(row, column, current_turn)
        break

    if current_turn == BLACK:  # alternate turns
        return WHITE
    return BLACK


if __name__ == "__main__":
    print("\nMinimum requirement: Python 3.0")
    rows = input_dimension("rows", MAX_ROWS)
    columns = input_dimension("columns", MAX_COLUMNS)
    board = HexBoard(rows, columns)

    # alternate turns and loop
    current_turn = BLACK
    while current_turn != "QUIT":
        board.display_board()
        display_guide()
        current_turn = input_command(current_turn, board)
    print("Quitting program...\n")
