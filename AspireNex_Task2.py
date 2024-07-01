import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif is_board_full(board):
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI
def find_best_move(board):
    best_move = None
    best_value = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_value = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move

# Function to get the player's move
def get_player_move(board):
    while True:
        move = input("Enter your move (row and column): ").split()
        if len(move) != 2:
            print("Invalid input. Enter row and column separated by a space.")
            continue
        row, col = move
        if not (row.isdigit() and col.isdigit()):
            print("Invalid input. Enter numbers for row and column.")
            continue
        row, col = int(row), int(col)
        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Invalid move. Row and column must be between 1 and 3.")
            continue
        if board[row-1][col-1] != " ":
            print("Invalid move. Cell already occupied.")
            continue
        return row-1, col-1

# Main function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X' and the AI is 'O'.")
    
    while True:
        print_board(board)
        if check_winner(board) or is_board_full(board):
            break
        # Player's move
        row, col = get_player_move(board)
        board[row][col] = "X"
        
        if check_winner(board) or is_board_full(board):
            break
        # AI's move
        ai_move = find_best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"
    
    print_board(board)
    winner = check_winner(board)
    if winner == "X":
        print("Congratulations! You won!")
    elif winner == "O":
        print("AI wins! Better luck next time.")
    else:
        print("It's a tie!")

# Start the game
play_game()
