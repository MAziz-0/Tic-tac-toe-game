import random
import sys
import time


#Creating a welcome screen

wlcm_scr = "Welcome to my Tic-tac-toe game!"
print(wlcm_scr)
time.sleep(1.5)
cred_msg = "\nThis is a 2 player game made by JZIREN. \n"
print(cred_msg)
time.sleep(1.5)

#Question
pl_request = input("Are you ready to play? ")
time.sleep(1.5)
#Response to question
pl_response = "yes" or "I'm ready"

#If the player responds with any given str within (pl_response)
#...one of the two statements below will be an output.
if pl_request == pl_response:
    print("\nLet's do a coin toss. \n")

elif pl_request == "no":
    print("\nThank you for playing! \n")
    time.sleep(2)
    print("\nENDING APPLICATION\n")
    time.sleep(1)
    print("       *")
    time.sleep(1)
    print("       *")
    time.sleep(1)
    print("       *")
    time.sleep(1)
    print("       *")
    time.sleep(2)
    sys.exit(0)
else:
    sys.exit(0)
# Coin flip to see who goes first
time.sleep(2)
playing = True

while playing == True:
# Loop to find random sides
    number = random.randint(1, 2)
    chosen_side = input("Player 1: Heads or Tails? ")
# Guessing Heads right or wrong
    if number == 1 and chosen_side == "heads":
        print("\nHeads! Player 1 will have the first move\n")

    elif number == 1 and chosen_side == "tails":
        print("\nHeads! Player 2 will have the first move.\n")
# Guessing Tails right or wrong
    elif number == 2 and chosen_side == "tails":
        print("\nTails! Player 1 will have the first move.\n")

    elif number == 2 and chosen_side == "heads":
        print("\nTails! Player 2 will have the first move.\n")
    else:
      continue

    pl_tutorial = input("Let's play Tic-tac-toe! Do you wish to hear the tutorial? ")

    if pl_tutorial == "yes":
      time.sleep(2)
      print("\n 1. The game is played on a grid that's 3 squares by 3 squares.\n")
      time.sleep(2)
      print("\n 2. You are X, your friend is O. Players take turns putting their marks in empty squares. \n")
      time.sleep(2)
      print("\n 3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n ")
      time.sleep(2)
      print("\n 4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie. \n")
      time.sleep(2)
      
    else:
      break

pl_continue = input("\nDo you wish to continue? \n")

if pl_continue == "yes" or "play game" or "Yes" or "continue":
  playing = False
    

time.sleep(2)
print("\nCreating Board\n")
time.sleep(1)
print("       *")
time.sleep(1)
print("       *")
time.sleep(1)
print("       *")
time.sleep(1)
print("       *")
time.sleep(2)

# --------- Global Variables -----------

# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"


# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():

  # Show the initial game board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_still_going:

    # Handle a turn
    handle_turn(current_player)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()
  
  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
    print("\nThank you for playing!\n")
  elif winner == None:
    print("\nIt's a draw! Thank you for playing!\n")


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  display_board()


# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check to see if somebody has won
def check_for_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  # Set global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or return None if there was no winner
  else:
    return None


# Check if there is a tie
def check_for_tie():
  # Set global variables
  global game_still_going
  # If board is full
  if "-" not in board:
    game_still_going = False
    return True
  # Else there is no tie
  else:
    return False


# Flip the current player from X to O, or O to X
def flip_player():
  # Global variables we need
  global current_player
  # If the current player was X, make it O
  if current_player == "X":
    current_player = "O"
  # Or if the current player was O, make it X
  elif current_player == "O":
    current_player = "X"


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()





# Welcome screen
# Choose who goes first     
# Board
# displayboard
# play game       
# Handle turns
# Check Win
# Check:
    # Row   
    # Column     
    # Diag     
# Check tie      
# Flip player