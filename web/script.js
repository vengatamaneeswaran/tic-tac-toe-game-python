// Step 3: Game Logic

// 1. Select the HTML elements we need to interact with
const cells = document.querySelectorAll('.cell');
const statusText = document.getElementById('statusText');
const resetButton = document.getElementById('resetButton');

// 2. Set up our game variables (just like our Python class!)
let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let isGameActive = true;

// The 8 winning conditions
const winConditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
    [0, 4, 8], [2, 4, 6]             // Diagonals
];

// 3. Add Event Listeners
// This is identical to Tkinter's 'command=' parameter!
// We loop through each cell and tell it to run handleCellClick when clicked.
cells.forEach(cell => cell.addEventListener('click', handleCellClick));
resetButton.addEventListener('click', resetGame);

// 4. The Human Turn
function handleCellClick() {
    // Get the index from the HTML data-index attribute we set in index.html
    const index = this.getAttribute('data-index');

    // If the cell is not empty, or the game is over, or it's not X's turn, do nothing!
    if (board[index] !== "" || !isGameActive || currentPlayer !== "X") {
        return;
    }

    // Otherwise, update the cell with "X"
    updateCell(this, index, "X");
    checkGameOver();
}

// 5. Updating the Cell
function updateCell(cellElement, index, player) {
    // Update our internal array
    board[index] = player;
    // Update the visual text on the screen
    cellElement.innerText = player;
    
    // Add CSS classes for styling and to disable hover effects
    cellElement.classList.add("taken");
    if (player === "X") {
        cellElement.classList.add("x");
    } else {
        cellElement.classList.add("o");
    }
}

// 6. Checking Win/Tie Conditions
function checkGameOver() {
    let roundWon = false;
    let winningCells = [];

    // Check for win
    for (let i = 0; i < winConditions.length; i++) {
        const condition = winConditions[i];
        const a = board[condition[0]];
        const b = board[condition[1]];
        const c = board[condition[2]];

        if (a === "" || b === "" || c === "") {
            continue;
        }

        if (a === b && b === c) {
            roundWon = true;
            winningCells = condition;
            break;
        }
    }

    if (roundWon) {
        statusText.innerText = `Player ${currentPlayer} Wins!`;
        isGameActive = false;
        
        // Add the "win" CSS class to highlight the winning cells green
        winningCells.forEach(index => {
            cells[index].classList.add("win");
        });
        return; // Exit function so the computer doesn't try to play
    }

    // Check for tie
    if (!board.includes("")) {
        statusText.innerText = "It's a Tie!";
        isGameActive = false;
        
        // Add the "tie" CSS class to highlight all cells orange
        cells.forEach(cell => cell.classList.add("tie"));
        return; // Exit function
    }

    // Switch turns
    if (currentPlayer === "X") {
        currentPlayer = "O";
        statusText.innerText = "Computer is thinking...";
        
        // Call the computer's turn after a 500ms delay (just like we did with Tkinter's .after())
        setTimeout(computerTurn, 500);
    } else {
        currentPlayer = "X";
        statusText.innerText = "Your Turn (X)";
    }
}

// 7. The Computer Turn
function computerTurn() {
    if (!isGameActive) return;

    // Find all empty spots
    let emptySpots = [];
    for (let i = 0; i < board.length; i++) {
        if (board[i] === "") {
            emptySpots.push(i);
        }
    }

    // Pick a random empty spot
    if (emptySpots.length > 0) {
        // Math.random() is JavaScript's version of the random library!
        const randomIndex = Math.floor(Math.random() * emptySpots.length);
        const chosenSpot = emptySpots[randomIndex];
        
        // Find the HTML element for the chosen spot
        const cellElement = document.querySelector(`.cell[data-index='${chosenSpot}']`);
        
        // Update it with "O"
        updateCell(cellElement, chosenSpot, "O");
        checkGameOver();
    }
}

// 8. Reset Game
function resetGame() {
    currentPlayer = "X";
    board = ["", "", "", "", "", "", "", "", ""];
    isGameActive = true;
    statusText.innerText = "Your Turn (X)";

    cells.forEach(cell => {
        cell.innerText = "";
        // Remove all the CSS classes we added during the game so the board is clean again
        cell.classList.remove("taken", "x", "o", "win", "tie");
    });
}
