import random
import re

# List of winning patterns for the game
WINNING_PATTERNS = ["!!!......", "...!!!...", "......!!!", "!..!..!..", ".!..!..!.", "..!..!..!", "!...!...!", "..!.!.!.."]

# Initialize the super board and the individual boards
super_board = ['-' for _ in range(9)]
boards = [['-' for _ in range(9)] for _ in range(9)]

# Variables to keep track of the current game and the previous game
current_board, previous_board = -1, -1

# Function to print the super board
def print_super_board():
    main_grid = [[boards[0], boards[1], boards[2]], 
                [boards[3], boards[4], boards[5]], 
                [boards[6], boards[7], boards[8]]]
    
    row_separator = "=" * (len(main_grid[0][0]) * 3 + 2)  # Separator line between main grid rows
    col_separator = " | "  # Separator between individual grids within a row

    for row_index, outer_grid_row in enumerate(main_grid):
        for inner_row_index in range(3):
            row = ''
            for col_index, inner_grid in enumerate(outer_grid_row):
                row += ' ' + ' '.join(inner_grid[inner_row_index * 3:inner_row_index * 3 + 3]) + ' '
                if col_index < 2:
                    row += col_separator
            print(row)
        if row_index < 2:
            print(row_separator)

# Function to check if a player has won
def check_winner(board, player):
    for pattern in WINNING_PATTERNS:
        if re.match(pattern.replace("!", player), "".join(board)):
            return True
    return False

# Function to check if a board is full
def is_full(board):
    return all(cell != '-' for cell in board)

# Function for a player's move
def player_move(player):
    global current_board, previous_board
    while True:
        try:
            grid_num = int(input(f"Enter the grid number for player '{player}' (active game = '{current_board + 1}'): ")) - 1
            if 0 <= grid_num <= 8 and boards[current_board][grid_num] == '-':
                boards[current_board][grid_num] = player
                previous_board = current_board
                if super_board[grid_num] == '-':
                    current_board = grid_num
                else:
                    current_board = -1
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid move. Try again.")

# Main game loop
def main():
    players = ['X', 'O']
    global super_board, current_board
    current_player = random.choice(players)

    print("Welcome to Super Tic-Tac-Toe!")
    print_super_board()

    while True:
        if current_board == -1:
            while True:
                current_board = int(input(f"Select the grid for player '{current_player}' (1-9): ")) - 1
                if 0 <= current_board <= 8 and super_board[current_board] == '-':
                    break
                else:
                    print("Invalid move. Try again.")
        player_move(current_player)

        print_super_board()

        if check_winner(boards[previous_board], current_player):
            super_board[previous_board] = current_player
        elif is_full(boards[previous_board]):
            super_board[previous_board] = "*"
        if check_winner(super_board, current_player):
            print(f"Player '{current_player}' wins!")
            break
        elif is_full(super_board):
            print("It's a draw!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    main()

