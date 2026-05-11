import tkinter as tk
import random
from tkinter import messagebox 

class TicTacToeGUI:
    def __init__(self, root):
        """
        Initializes the Tic-Tac-Toe GUI window, sets up the game state,
        and creates the 3x3 grid of interactive buttons.
        """
        self.root = root
        self.root.title("Tic-Tac-Toe GUI")
        self.root.configure(bg='#333333') # Give the main window a nice dark background
        
        self.current_player = "X"
        self.buttons = []
        
        for i in range(9):
            # Added 'bold' to the font, and set a clean white background
            button = tk.Button(self.root, text="", font=('normal', 40, 'bold'), width=5, height=2,
                               bg='white',
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def button_click(self, index):
        """
        Handles the event when a human player clicks a button.
        Updates the board with 'X' and triggers the computer's turn if the game is not over.
        
        Args:
            index (int): The position (0-8) of the clicked button.
        """
        if self.buttons[index]['text'] == "" and self.current_player == "X":
            # Change the text to X and make it blue!
            self.buttons[index].config(text="X", fg="#0074D9")
            
            # Check if the human won BEFORE letting the computer play!
            if not self.check_game_over():
                self.current_player = "O"
                self.root.after(500, self.computer_turn)

    def computer_turn(self):
        """
        Executes the computer's turn by randomly selecting an available empty spot
        on the board and placing an 'O'.
        """
        empty_spots = []
        for i, button in enumerate(self.buttons):
            if button['text'] == "":
                empty_spots.append(i)
                
        if len(empty_spots) > 0:
            chosen_spot = random.choice(empty_spots)
            # Change the text to O and make it red!
            self.buttons[chosen_spot].config(text="O", fg="#FF4136")
            
            # Check if the computer won!
            if not self.check_game_over():
                self.current_player = "X"

    def check_game_over(self):
        """
        Checks the current state of the board against all possible win conditions
        and checks for a tie. Displays a message box if the game has ended.
        
        Returns:
            bool: True if the game is over (win or tie), False otherwise.
        """
        # The 8 winning combinations (just like our terminal version!)
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        
        # 1. Check for win
        for condition in win_conditions:
            # Get the text from the three buttons in this winning condition
            b1 = self.buttons[condition[0]]['text']
            b2 = self.buttons[condition[1]]['text']
            b3 = self.buttons[condition[2]]['text']
            
            # If all three have the same symbol AND they aren't empty
            if b1 == b2 == b3 and b1 != "":
                # Highlight the winning buttons in green!
                self.buttons[condition[0]].config(bg="#2ECC40")
                self.buttons[condition[1]].config(bg="#2ECC40")
                self.buttons[condition[2]].config(bg="#2ECC40")
                self.root.update() # Force the window to update colors before showing the pop-up
                
                # Show a pop-up dialog box!
                messagebox.showinfo("Game Over", f"Player {b1} wins!")
                self.reset_game()
                return True # Game is over
                
        # 2. Check for tie
        is_tie = True
        for button in self.buttons:
            # If we find even one empty button, it's not a tie yet
            if button['text'] == "":
                is_tie = False
                
        if is_tie:
            # Highlight all buttons in orange to indicate a tie!
            for button in self.buttons:
                button.config(bg="#FF851B")
            self.root.update() # Force update to show colors before popup
            
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
            return True # Game is over
            
        return False # Game is not over yet

    def reset_game(self):
        """
        Resets the game board and current player state to start a new round.
        Clears all text from the buttons.
        """
        # Clear the board so they can play again
        self.current_player = "X"
        for button in self.buttons:
            # Reset text and colors back to default
            button.config(text="", bg="white")

# Run Step 4
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
