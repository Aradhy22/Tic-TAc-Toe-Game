import os

def print_board(board):
    """Displays the Tic Tac Toe board."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print("\n\t    TIC TAC TOE\n")
    print("\t   1   2   3")
    for idx, row in enumerate(board):
        print(f"\t{idx + 1}  " + " | ".join(row))
        if idx < 2:
            print("\t  ---+---+---")

def check_winner(board):
    """Checks if there is a winner on the board."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    """Checks if the board is full."""
    return all(cell != " " for row in board for cell in row)

def save_game(board, current_player):
    """Saves the current game state to a file."""
    with open("game_state.txt", "w") as file:
        for row in board:
            file.write(" ".join(row) + "\n")
        file.write(current_player + "\n")

def load_game():
    """Loads the game state from a file if it exists."""
    if os.path.exists("game_state.txt"):
        with open("game_state.txt", "r") as file:
            lines = file.readlines()
            board = [line.strip().split(" ") for line in lines[:3]]
            current_player = lines[3].strip()
        return board, current_player
    return [[" " for _ in range(3)] for _ in range(3)], "X"

def tic_tac_toe():
    """Main function to play the Tic Tac Toe game."""
    board, current_player = load_game()

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("\nEnter row (1, 2, 3): ")) - 1
            col = int(input("Enter column (1, 2, 3): ")) - 1

            if row not in range(3) or col not in range(3):
                print("\nInvalid input. Please enter a number between 1 and 3.")
                continue

            if board[row][col] != " ":
                print("\nCell already occupied. Choose a different cell.")
                continue

            board[row][col] = current_player
            save_game(board, current_player)

            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f"\nCongratulations! Player {winner} wins!")
                os.remove("game_state.txt")  # Remove saved game on completion
                break

            if is_full(board):
                print_board(board)
                print("\nIt's a draw!")
                os.remove("game_state.txt")  # Remove saved game on completion
                break

            current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):
            print("\nInvalid input. Please enter a valid row and column.")

if __name__ == "__main__":
    tic_tac_toe()
