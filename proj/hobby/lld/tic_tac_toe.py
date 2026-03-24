from random import randrange

def display_board(board):
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print("|    ",end="")
        print("  |    ".join(str(board[i][j]) for j in range(3)), end ="")
        print("  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    free = free_moves_on_board(board)
    while True:
        try:
            move = int(input("Please enter a valid move in 1-9: " ))
            if move < 1 or move > 9:
                print("choose a valid move in range 1-9: ")
                continue
            move -= 1
            row = move // 3
            col = move % 3
            if (row, col) not in free:
                print("Your choice is already selected, Select a new move.")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Invalid Input. Please enter a valid move in 1-9: ")

def free_moves_on_board(board):
    free=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                free.append((i,j))
    return free

def victory_for(board, sign):
    # check rows, cols
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or \
                all(board[j][i] == sign for j in range(3)):
            return True
    # check diagonals
    if all(board[i][i] == sign for i in range(3)) or \
            all(board[i][2-i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    free = free_moves_on_board(board)
    if free:
        move = free[randrange(len(free))]
        board[move[0]][move[1]] = 'X'

board = [[1,2,3],[4,'X',6],[7,8,9]]

while True:
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer Won!")
        break
    if not free_moves_on_board(board):
        print("Draw!")
        break

    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You Won!")
        break
    if not free_moves_on_board:
        print("Draw!")
        break

    draw_move(board)
