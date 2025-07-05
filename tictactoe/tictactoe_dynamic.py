##################################################
# Tic Tac Toe Game in Python                     #
# Developed By: Saanvi Patel                     #
# Date: 5th July 2025                            #           
#                                                #
##################################################

from random import randrange

# This function shows the current positions and state of the game
def display_board(board):
    line = "+-------+-------+-------+" # Makes the 3x3 Grid lines
    for row in board:
        print(line)
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |") # Displays the Grid and Numbers the rows and columns
        print("|       |       |       |")
    print(line)

def make_list_of_free_fields(board): # Returns a list of free fields in the board
    return [(i, j) for i in range(3) for j in range(3) if isinstance (board[i][j], int)] # isintance helps keep "X" in the center

def enter_move(board):# This function allows the user to enter their move
    free = make_list_of_free_fields(board) # If the board is full, then set the rows and colums to empty
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError
            row, col = divmod(move - 1, 3)
            if (row, col) not in free:
                print("This cell is already taken.")
            else:
                board[row][col] = 'O'
                break
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
        except:
            print("Something went wrong. Please try again.")

def victory_for(board, sign): # This function checks if a player has won the game
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)): # Check rows
            return True
        if all(board[j][i] == sign for j in range(3)): # Check columns
            return True
    if all(board[i][i] == sign for i in range(3)): # Check main diagonal
            return True
    if all(board[i][2 - i] == sign for i in range(3)): # Check secondary-diagonal
            return True
    return False

def draw_move(board): # This function makes the computer's move randomly using the imported randrage module
    free = make_list_of_free_fields(board)
    if free:
        move = free[randrange(len(free))] # Randomly selects an available field on the board
        board[move[0]][move[1]] = 'X'

def main(): # This is the main function that runs the game
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]] # Initializing the board with numbers and 'X' in the center
    display_board(board)

    try:

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
        print("\nGame interrupted. Exiting Now...")
    except Exception as e:
        print(f"An error occurred: {e}")  




      
main()
