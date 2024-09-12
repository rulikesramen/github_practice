import random

def create_board():
  """Creates an empty Connect Four board."""
  board = []
  for _ in range(6):
    row = [' '] * 7
    board.append(row)
  return board

def print_board(board):
  """Prints the Connect Four board to the console."""
  print(" 1 2 3 4 5 6 7")
  for row in board:
    print("|".join(row))

def is_valid_move(board, col):
  """Checks if a move is valid (column not full)."""
  return board[0][col] == ' '

def get_next_open_row(board, col):
  """Finds the next available row in a given column."""
  for r in range(5, -1, -1):
    if board[r][col] == ' ':
      return r
  return None

def drop_piece(board, row, col, piece):
  """Drops a piece into the board."""
  board[row][col] = piece

def winning_move(board, piece):
  """Checks if the last move resulted in a win."""
  # Check horizontal
  for c in range(4):
    for r in range(6):
      if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
        return True

  # Check vertical
  for c in range(7):
    for r in range(3):
      if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
        return True

  # Check diagonals (positive slope)
  for c in range(4):
    for r in range(3):
      if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
        return True

  # Check diagonals (negative slope)
  for c in range(4):
    for r in range(3, 6):
      if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
        return True

  return False

def choose_first_player():
  """Randomly chooses the starting player."""
  if random.randint(0, 1) == 0:
    return 'X'
  else:
    return 'O'

def play_again():
  """Asks the player if they want to play again."""
  print("Do you want to play again? (y/n)")
  return input().lower() == 'y'

def player_move(board, piece):
  """Gets the player's move."""
  valid_move = False
  while not valid_move:
    print(f"Player {piece}, enter your move (1-7):")
    col = int(input()) - 1
    if is_valid_move(board, col):
      valid_move = True
    else:
      print("Invalid move. Column is full. Try again.")
  row = get_next_open_row(board, col)
  drop_piece(board, row, col, piece)

def main():
  """Main game loop."""
  board = create_board()
  game_over = False
  turn = choose_first_player()

  while not game_over:
    print_board(board)
    player_move(board, turn)
    if winning_move(board, turn):
      print_board(board)
      print(f"Player {turn} wins!")
      game_over = True
    else:
      turn = 'O' if turn == 'X' else 'X'

  if play_again():
    main()

if __name__ == "__main__":
  main()