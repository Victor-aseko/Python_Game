# DO NOT modify or add any import statements
from typing import Optional
from a1_support import *


# Write your classes and functions here

def num_hours()-> float:
    return 8.5  # Number of hours spent on the assignment

def generate_initial_board(board_size=BOARD_SIZE) -> list[str]:
    # Method to generate the initial game board filled with blank pieces
    return [[BLANK_PIECE for _ in range(board_size)] for _ in range(board_size)]

def print_board(board):
    for row in board:
        print(COLUMN_SEPARATOR + COLUMN_SEPARATOR.join(row) + COLUMN_SEPARATOR)
    print("-" * (2 * len(board) + 1))
    print(" ", end="")
    for col in range(1, len(board) + 1):
        print(col, end=" ")
    print()

def is_column_full(board, column:str) -> bool:    #A method checking if a column in the game board is full
    return BLANK_PIECE not in [row[column] for row in board]

def is_column_empty(board, column:str) -> bool:
    return all(row[column] == BLANK_PIECE for row in board)



def display_board(board: list[str]) -> None:
    print_board(board)

def check_input(action: str, board) -> bool:
     if len(action) < 2 or not action[1:].isdigit():
        print(INVALID_FORMAT_MESSAGE)
        return False

     column_index = int(action[1:]) - 1

     if column_index < 0 or column_index >= len(board):
        print(INVALID_COLUMN_MESSAGE)
        return False

     if action[0].lower() == 'a' and is_column_full(board, column_index):
        print(FULL_COLUMN_MESSAGE)
        return False

     if action[0].lower() == 'r' and is_column_empty(board, column_index):
        print(EMPTY_COLUMN_MESSAGE)
        return False

     return True

def get_action() -> str:      #A method displaying player's action, add or remove piece to or from the game board
    while True:
        command = input(ENTER_COMMAND_MESSAGE)
        if command.lower() == 'h':
            print(HELP_MESSAGE)
            continue
        elif command.lower() == 'q':
            return 'quit'
        elif not command[1:].isdigit():
            print(INVALID_FORMAT_MESSAGE)
            continue
        else:
            return command

def add_piece(board: list[str], piece:str, column_index:int) -> bool:
    if is_column_full(board, column_index):
        print(FULL_COLUMN_MESSAGE)
        return False
    else:
        for row in range(len(board) - 1, -1, -1):
            if board[row][column_index] == BLANK_PIECE:
                board[row][column_index] = piece
                return True

def remove_piece(board: list[str], column_index:int) -> bool:
    if is_column_empty(board, column_index):
        print(EMPTY_COLUMN_MESSAGE)
        return False
    else:
        for row in range(len(board) - 1, 0, -1):
            if board[row][column_index] != BLANK_PIECE:
                removed_piece = board[row][column_index]
                for shift_row in range(row, 0, -1):
                    board[shift_row][column_index] = board[shift_row - 1][column_index]
                board[0][column_index] = BLANK_PIECE
                return True
        board[0][column_index] = BLANK_PIECE
        return True

# Implementation below is win-checking logic for horizontal, vertical, and diagonal connections
# Also checks for a draw if all columns are full
# Returns the winning player's piece or BLANK_PIECE for a draw

def check_win(board: list[str]) -> Optional[str]:
    board_size = len(board)
    # Check horizontal
    for row in range(board_size):
        for col in range(board_size - REQUIRED_WIN_LENGTH + 1):
            if all(board[row][col + i] == board[row][col] != BLANK_PIECE for i in range(1, REQUIRED_WIN_LENGTH)):
                return board[row][col]

    # Check vertical
    for col in range(board_size):
        for row in range(board_size - REQUIRED_WIN_LENGTH + 1):
            if all(board[row + i][col] == board[row][col] != BLANK_PIECE for i in range(1, REQUIRED_WIN_LENGTH)):
                return board[row][col]

    # Check row diagonal
    for row in range(board_size - REQUIRED_WIN_LENGTH + 1):
        for col in range(board_size - REQUIRED_WIN_LENGTH + 1):
            if all(board[row + i][col + i] == board[row][col] != BLANK_PIECE for i in range(1, REQUIRED_WIN_LENGTH)):
                return board[row][col]

    # Check column diagonal
    for row in range(board_size - REQUIRED_WIN_LENGTH + 1):
        for col in range(board_size - 1, REQUIRED_WIN_LENGTH - 2, -1):
            if all(board[row + i][col - i] == board[row][col] != BLANK_PIECE for i in range(1, REQUIRED_WIN_LENGTH)):
                return board[row][col]

    # Check for a draw
    if all(all(cell != BLANK_PIECE for cell in row) for row in board):
        return BLANK_PIECE

    return None

def play_game() -> None:
    board = generate_initial_board()
    player1 = PLAYER_1_PIECE
    player2 = PLAYER_2_PIECE
    current_player = player1
    
    while True:
        display_board(board)
        player_name = {player1: PLAYER_1_MOVE_MESSAGE, player2: PLAYER_2_MOVE_MESSAGE}
        print(player_name[current_player])
        action = get_action()

        if action == 'quit':
            return 'quit'

        if not check_input(action, board):
            continue

        column = int(action[1:]) - 1

        if column < 0 or column >= len(board):
            print(INVALID_COLUMN_MESSAGE)
            continue

        if action[0].lower() == 'a':
            if not add_piece(board, current_player, column):
                continue
        elif action[0].lower() == 'r':
            if not remove_piece(board, column):
                continue

        winner = check_win(board)
        if winner:    
            display_board(board)            
            if winner == BLANK_PIECE:
                print(DRAW_MESSAGE)
            else:
                if winner == player1:
                    print(PLAYER_1_VICTORY_MESSAGE)
                else:
                    print(PLAYER_2_VICTORY_MESSAGE)
            return 'end_game'

        if all(is_column_full(board, col) for col in range(len(board))):                
            print(DRAW_MESSAGE)
            return 'end_game'

        current_player = player2 if current_player == player1 else player1  # Switch player

#Prompt the user to play again or exit based on the game result
def play_again_prompt():
    while True:
        play_again = input(CONTINUE_MESSAGE)
        if play_again.lower() == 'y':
            return True
        elif play_again.lower() == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' to continue or 'n' to quit.")

def main() -> None:
    while True:   
        result = play_game()
        if result == 'quit':    
            if play_again_prompt():
                continue
            else:
                break
        elif result == 'end_game':
            if play_again_prompt():
                continue
            else:
                break

if __name__ == "__main__":
    main()
