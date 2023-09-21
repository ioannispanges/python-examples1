def print_board(board):
    for row in board:
        print(" | ".join(row))
        # print(" - " * 4)


def check_winner(board, player):
    
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Fix the board initialization
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Play {current_player}, enter row (0, 1, or 2):"))
        col = int(input(f"Play {current_player}, enter column (0, 1, or 2):"))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
