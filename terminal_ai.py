import random
import time

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def handle_human_turn(player):
    print(f"Human ({player})'s turn.")
    valid_move = False
    while not valid_move:
        position = input("Choose a position from 1-9: ")
        if position in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = int(position) - 1
            if board[position] != "X" and board[position] != "O":
                board[position] = player
                valid_move = True
            else:
                print("That position is already taken. Try again!")
        else:
            print("Invalid input. Please choose a number from 1 to 9.")

def handle_computer_turn(player):
    print(f"Computer ({player}) is thinking...")
    # Add a small delay (1 second) so it feels like the computer is actually "thinking"
    time.sleep(1) 
    
    # 1. Find all empty spots on the board
    empty_spots = []
    for index in range(9):
        # If the spot is not an X or an O, it must be empty
        if board[index] != "X" and board[index] != "O":
            empty_spots.append(index) # Save the index of the empty spot
            
    # 2. Randomly pick one of the empty spots
    if empty_spots:
        chosen_spot = random.choice(empty_spots)
        board[chosen_spot] = player

def check_win():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            return board[condition[0]]
    return None

def check_tie():
    for spot in board:
        if spot in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
    return True

def play_game():
    current_player = "X"
    game_over = False
    
    print("Welcome to Tic-Tac-Toe: Human vs Computer!")
    print_board()
    
    while not game_over:
        # Check whose turn it is
        if current_player == "X":
            handle_human_turn(current_player)
        else:
            handle_computer_turn(current_player)
            
        print_board()
        
        winner = check_win()
        if winner:
            if winner == "X":
                print("Congratulations! You won!")
            else:
                print("The Computer won! Better luck next time.")
            game_over = True
        elif check_tie():
            print("It's a tie! Well played.")
            game_over = True
        else:
            # Switch turns
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
