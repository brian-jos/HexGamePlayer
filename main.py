def displayLegend():
  print("\n===========================")
  print("_ : Empty")
  print("x : Black (Letter Axis)")
  print("o : White (Number Axis)")
  print("===========================")

def inputDimensions():
  rows = int(input("Enter # of rows (max 99): "))
  columns = int(input("Enter # of columns (max 26): "))
  return rows, columns

def generateBoard(rows, columns):
  row = list()
  for i in range(columns):
    row.append(0) # represents empty cell

  board = list()
  for i in range(rows):
    board.append(list(row)) # new list instead of reference
  return board

def displayBoard(board, rows, columns):
  print()
  for y in range(rows + 2): # considers letter axis (+2)
    if (y < 1 or y > rows): # first or last row
      print("  ", end = "")
    if (y < 10): # single digit row
      print(" " * y, end = "")
    else: # double digit row
      print(" " * (y - 1), end = "")
    letterAxis = "A" # starting letter of letter axis
    for x in range(columns + 2): # considers number axis (+2)
      if (y < 1 or y > rows): # first or last row
        print(letterAxis, end = " ") # print letter axis
        letterAxis = chr(ord(letterAxis) + 1)
        if (x > columns - 2): # letters won't exceed number of columns
          break
      # print number axis
      elif (x < 1): # first column
        print(y, end = "")
      elif (x > columns): # last column
        print("\\" + str(y), end = "")
      else: # position is on the board
        if (board[y - 1][x - 1] == 1):
          print("\\x", end = "") # display black
        elif (board[y - 1][x - 1] == 2):
          print("\\o", end = "") # display white
        else:
          print("\\_", end = "") # display empty
    print()

def enterCommand(currentTurn, board):
  if (currentTurn == 0):
    displayLegend()
    command = input("Black's turn to move: ").upper()
  else:
    displayLegend()
    command = input("White's turn to move: ").upper()

  row = ord(command[0]) - 65
  column = int(command[1:]) - 1

  if (currentTurn == 0):
    board[column][row] = 1
  else:
    board[column][row] = 2

  return board

if __name__ == '__main__':
    rows, columns = inputDimensions()

    board = generateBoard(rows, columns)

    currentTurn = 0
    while 1:
        displayBoard(board, rows, columns)
        board = enterCommand(currentTurn, board)
        currentTurn = (currentTurn + 1) % 2;