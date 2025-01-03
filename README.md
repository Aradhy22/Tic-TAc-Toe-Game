## Tic Tac Toe Game:
A simple, interactive console-based Tic Tac Toe game built in Python. This two-player game allows users to compete against each other with features such as saving the game state and resuming it later.

## Features:

1- Interactive Gameplay: Players take turns marking their spots on the board.

2- Save and Load: The game state is saved after each turn, enabling players to resume at any time.

3- Winner Detection: Automatically detects when a player wins or if the game ends in a draw.

4- Enhanced Console Design: Clear and user-friendly interface with rows and columns labeled from 1 to 3.

5- Input Validation: Prevents invalid moves and handles errors gracefully.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Aradhy22/Tic-TAc-Toe-Game.git
   cd Tic-TAc-Toe-Game
  2. Run the game:
 ``` bash
python Tic Tac Toe Game .py
```
## Code Example

Here's a snippet of the core game logic for saving and loading the game state:
 ```bash
def save_game(board, current_player):
    """Saves the current game state to a file."""
    with open("game_state.txt", "w") as file:
        for row in board:
            file.write(" ".join(row) + "\\n")
        file.write(current_player + "\\n")

def load_game():
    """Loads the game state from a file if it exists."""
    if os.path.exists("game_state.txt"):
        with open("game_state.txt", "r") as file:
            lines = file.readlines()
            board = [line.strip().split(" ") for line in lines[:3]]
            current_player = lines[3].strip()
        return board, current_player
    return [[" " for _ in range(3)] for _ in range(3)], "X"
```
## How to Play

1-Each player takes turns choosing a row and column to place their marker (X or O).

2-The game ends when:

 A) One player successfully aligns three markers horizontally, vertically, or diagonally.
 
 B)All cells are filled, resulting in a draw.

3-The game state is automatically saved after each turn, and players can resume by simply running the script again.

## Requirements

Python 3.x

## Ideas that can be implemented

1- Add an option to play against an AI opponent.

2-Enable customization for board sizes (e.g., 4x4 or 5x5).

3-Implement a replay option after the game ends.



