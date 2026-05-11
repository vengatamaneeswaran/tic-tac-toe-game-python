# Tic-Tac-Toe Game

# Step 1: Representing the board
# We'll use a Python List of 9 strings to represent the 3x3 grid.
# We fill it with numbers 1 to 9 so the player knows which number to type for their move.
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Function to display the board
def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Step 2: Handling player input
def handle_turn(player):
    print(f"{player}'s turn.")
    valid_move = False
    
    while not valid_move:
        # We use input() to get the player's choice
        position = input("Choose a position from 1-9: ")
        
        # Check if the input is valid (a number from 1 to 9)
        if position in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            # Convert string to integer and subtract 1 to get the correct list index (0-8)
            position = int(position) - 1
            
            # Check if the spot is already taken
            if board[position] != "X" and board[position] != "O":
                board[position] = player
                valid_move = True
            else:
                print("That position is already taken. Try again!")
        else:
            print("Invalid input. Please choose a number from 1 to 9.")

# Step 3: Checking for a win or a tie
def check_win():
    # Define all 8 possible winning combinations (rows, columns, diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        # If all 3 spots in a condition have the same player ("X" or "O")
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            return board[condition[0]] # Return the winning player ("X" or "O")
    return None # No winner yet

def check_tie():
    # If there are no numbers left on the board (only "X" and "O") and no one has won
    for spot in board:
        if spot in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False # There is still an empty spot, so it's not a tie
    return True # The board is full, and since no one won, it's a tie

# Step 4: The Main Game Loop
def play_game():
    # Start the game with player X
    current_player = "X"
    game_over = False
    
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    # Keep looping until someone wins or it's a tie
    while not game_over:
        # 1. Take a turn
        handle_turn(current_player)
        
        # 2. Show the updated board
        print_board()
        
        # 3. Check for win
        winner = check_win()
        if winner:
            print(f"Congratulations! Player {winner} won the game!")
            game_over = True
            
        # 4. Check for tie
        elif check_tie():
            print("It's a tie! Well played.")
            game_over = True
            
        # 5. Switch turns (if game is not over)
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

# Start the game!
if __name__ == "__main__":
    play_game()
