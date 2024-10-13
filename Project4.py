### Code snippet to buid a simple TICTACTOE game

# Function For Board Design
def print_board(board):
    for i , row in enumerate(board):
        row_str="  "
        for j , value in enumerate(row):
            row_str += value
            if j != len(row)-1:
                row_str += " | "
        print(row_str)
        if i != len(board)-1:
            print("------------")

# Function For Playing , Getting user input
def get_move(turn,board):
    while True:
        row=int(input("Row Number: "))
        col=int(input("Col Number : "))

        if row < 1 or row > len(board):
            print("invalid row number , try again...")
        elif col < 1 or col > len(board[row-1]):
            print("Invalid column number , try again...")
        elif board[row-1][col-1] != " ":
            print(" The space is already taken , try again...")
        else:
            break
    
    board[row-1][col-1] = turn

# Function to find the winner
def check_win(board,turn):
    lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for line in lines:
        win = True
        for pos in line:
            row, col = pos
            if board[row][col] != turn:
                win = False
                break

        if win:
            return True
    
    return False

# Main Function
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

turn = "X"
turn_number = 0
print_board(board)

while turn_number < 9:
    print()
    print("It is the", turn , "Players turn. Please select your move.")

    get_move(turn,board)

    print_board(board)

    winner = check_win(board,turn)

    if winner:
        break

    if turn == "X":
        turn = "O"
    else:
        turn ="X"
    
    turn_number += 1

if turn_number == 9:
    print("Game Tied...")
else:
    print("The winner is",turn)


# Below is a comment that should be noted...
"""
The below two lines serve very different purposes:

# board[row-1][col-1] = turn:

This line updates the game board at the specified row and column with the current player's symbol (either "X" or "O").
It effectively places the player's move on the board, modifying the board state.

# turn = board[row-1][col-1]:

This line attempts to set the turn variable to whatever value is currently in the specified cell of the board.
This is not what you want to do when a player makes a move; instead of changing the board, it would incorrectly change the player's turn to the value already present in that cell (which would typically be a space or the other player's symbol).

"""