PLAYER_1_PIECE = 'X'
PLAYER_2_PIECE = 'O'
BLANK_PIECE = '-'

COLUMN_SEPARATOR = '|'

BOARD_SIZE = 8
REQUIRED_WIN_LENGTH = 4

PLAYER_1_MOVE_MESSAGE = "Player 1 to move"
PLAYER_2_MOVE_MESSAGE = "Player 2 to move"
PLAYER_1_VICTORY_MESSAGE = "Player 1 wins!"
PLAYER_2_VICTORY_MESSAGE = "Player 2 wins!"
DRAW_MESSAGE = "Its a Draw!"

ENTER_COMMAND_MESSAGE = "Please enter action (h to see valid commands): "

INVALID_FORMAT_MESSAGE = "Invalid command. Enter 'h' for valid command format"
INVALID_COLUMN_MESSAGE = f"Invalid column, please enter a number between 1 and {BOARD_SIZE} inclusive"
FULL_COLUMN_MESSAGE = "You can't add a piece to a full column!"
EMPTY_COLUMN_MESSAGE = "You can't remove a piece from an empty column!"

HELP_MESSAGE = """Valid commands: 
- aX: Add piece to top of column X (X must be a valid integer)
- rX: Remove a piece from bottom of column X (X must be a valid integer)
- h: Display help text
- q: Quit current game\n"""

CONTINUE_MESSAGE = "Would you like to play again? (y/n): "