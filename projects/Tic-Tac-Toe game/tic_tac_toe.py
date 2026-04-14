import random

def print_board(board):
    print("\n  1 2 3")
    for i, row in enumerate(board):
        print(f"{i+1} ", end="")
        print("|".join(row))
        if i < 2:
            print("  -----")
    print()

def check_winner(board):
    # Rows, columns, diagonals
    lines = board + [list(col) for col in zip(*board)]
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])
    for line in lines:
        if line[0] != ' ' and line.count(line[0]) == 3:
            return line[0]
    return None

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, is_max):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    if winner == 'X':
        return -1
    if is_draw(board):
        return 0
    if is_max:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best = max(best, score)
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best = min(best, score)
        return best

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        turn = 'X'
        while True:
            print_board(board)
            if turn == 'X':
                try:
                    move = input("Enter your move (row col): ").split()
                    if len(move) != 2:
                        raise ValueError
                    row, col = int(move[0])-1, int(move[1])-1
                    if not (0 <= row < 3 and 0 <= col < 3) or board[row][col] != ' ':
                        raise ValueError
                    board[row][col] = 'X'
                except ValueError:
                    print("Invalid move. Try again.")
                    continue
            else:
                print("AI is thinking...")
                move = best_move(board)
                if move:
                    board[move[0]][move[1]] = 'O'
                else:
                    # Should not happen
                    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
                    if empty:
                        i, j = random.choice(empty)
                        board[i][j] = 'O'
            winner = check_winner(board)
            if winner:
                print_board(board)
                if winner == 'X':
                    print("Congratulations! You win!")
                else:
                    print("AI wins! Better luck next time.")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            turn = 'O' if turn == 'X' else 'X'
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
