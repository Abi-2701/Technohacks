# Define the board as a list
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
  for i in range(3):
    print(' | '.join(board[i*3:(i*3)+3]))
    if i != 2:
      print('-' * 5)

# Function to check for a win
def is_victory(mark):
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
  for condition in win_conditions:
    if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
      return True
  return False

# Function to check for a draw
def is_draw():
  return all(x != ' ' for x in board)

# Main game loop
current_player = 'X'
while True:
  print_board()
  # Get player move
  move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
  if board[move] == ' ':
    board[move] = current_player
  else:
    print("Invalid move. Try again.")
    continue

  # Check for win or draw
  if is_victory(current_player):
    print_board()
    print(f"Player {current_player} wins!")
    break
  elif is_draw():
    print_board()
    print("It's a draw!")
    break

  # Switch turns
  current_player = 'O' if current_player == 'X' else 'X'

print("Thanks for playing!")
