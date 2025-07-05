from random import randrange

def display_board(board):
    line = "+-------+-------+-------+"
    for row in board:
        print(line)
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
    print(line)

def make_list_of_free_fields(board):
    return [(i, j) for i in range(3) for j in range(3) if isinstance (board[i][j], int)]

def enter_move(board):
    free = make_list_of_free_fields(board)
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

def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)):
            return True
        if all(board[j][i] == sign for j in range(3)): 
            return True
    if all(board[i][i] == sign for i in range(3)): 
            return True
    if all(board[i][2 - i] == sign for i in range(3)): 
            return True
    return False

def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        move = free[randrange(len(free))]
        board[move[0]][move[1]] = 'X'

def main():
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
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
        print("\nGame interrupted. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")  




      
main()
