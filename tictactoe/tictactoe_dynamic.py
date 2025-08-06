##################################################
# Tic Tac Toe Game in Python                     #
# Developed By: Saanvi Patel                     #
# Updated: Dynamic Board Size (Between 3-9)      #
# Date: 5th July 2025                            #           
##################################################

from random import randrange
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'  # Reset color to default
def get_board_size():
    try:
        size = int(input("Enter board size (e.g., 3 for 3x3): "))
        if size < 3:
            raise ValueError("Board must be at least 3x3.")
        return size
    except:
        raise Exception("Invalid board size. Must be a single number ≥ 3.")

# Displays the board dynamically
def display_board(board):
    size = len(board)
    line = "+-------" * size + "+"
    for row in board:
        print(line)
        print("|       " * size + "|")
        colored_row = []
        for cell in row:
            if cell == 'X':
                colored_cell = f"|   {Color.GREEN}X{Color.RESET}   "
            elif cell == 'O':
                colored_cell = f"|   {Color.RED}O{Color.RESET}   "
            else:
                colored_cell = f"|   {str(cell)}   "
            colored_row.append(colored_cell)
        print("".join(colored_row) + "|")
        print("|       " * size + "|")
    print(line)

# Returns a list of all empty fields
def make_list_of_free_fields(board):
    return [(i, j) for i in range(len(board)) for j in range(len(board)) if isinstance(board[i][j], int)]

# Allows the user to enter their move
def enter_move(board):
    free = make_list_of_free_fields(board)
    size = len(board)
    max_cell = size * size
    while True:
        try:
            move = int(input(f"Enter your move (1-{max_cell}): "))
            if move < 1 or move > max_cell:
                raise ValueError
            row, col = divmod(move - 1, size)
            if (row, col) not in free:
                print("This cell is already taken.")
            else:
                board[row][col] = 'O'
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except:
            print("Something went wrong. Please try again.")

# Checks for victory
def victory_for(board, sign):
    size = len(board)
    for i in range(size):
        if all(board[i][j] == sign for j in range(size)):  # Check rows
            return True
        if all(board[j][i] == sign for j in range(size)):  # Check columns
            return True
    if all(board[i][i] == sign for i in range(size)):      # Main diagonal
        return True
    if all(board[i][size - 1 - i] == sign for i in range(size)):  # Anti-diagonal
        return True
    return False

# Random computer move
def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        move = free[randrange(len(free))]
        board[move[0]][move[1]] = 'X'

# Main game loop
def main():
    try:
        size = get_board_size()
        board = [[i * size + j + 1 for j in range(size)] for i in range(size)]
        center = size // 2
        board[center][center] = 'X'  # Start with 'X' in the center
        display_board(board)

        while True:
            enter_move(board)
            display_board(board)
            if victory_for(board, 'O'):
                print("You won!") 
                break
            if not make_list_of_free_fields(board):
                print("It's a tie!")
                break
            draw_move(board)
            display_board(board)
            if victory_for(board, 'X'):
                print("Computer won!")
                break
            if not make_list_of_free_fields(board):
                print("It's a tie!")
                break
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting now...")
    except Exception as e:
        print(f"An error occurred: {e}")

main()
