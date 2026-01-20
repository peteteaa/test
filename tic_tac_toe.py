"""
Tic Tac Toe Game in Python
Run this script from the command line to play.
"""

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter your move as row,col (1-3): ")
            row, col = map(int, move.strip().split(','))
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid input. Please enter numbers between 1 and 3.")
                continue
            if board[row-1][col-1] != ' ':
                print("Cell already taken. Try again.")
                continue
            return row-1, col-1
        except Exception:
            print("Invalid input format. Please enter as row,col (e.g., 1,3)")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
