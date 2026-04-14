package main

// AI logic using Minimax algorithm
func getBestMove(board *Board) (int, int) {
	bestScore := -1000
	moveRow, moveCol := -1, -1

	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if board.cells[i][j] == ' ' {
				board.cells[i][j] = 'O'
				score := minimax(board, 0, false)
				board.cells[i][j] = ' '
				if score > bestScore {
					bestScore = score
					moveRow, moveCol = i, j
				}
			}
		}
	}
	return moveRow, moveCol
}

// minimax recursively evaluates all possible moves and returns the best score for the AI.
func minimax(board *Board, depth int, isMaximizing bool) int {
	winner := checkWinner(board)
	if winner == 'O' {
		return 10 - depth
	} else if winner == 'X' {
		return depth - 10
	} else if isDraw(board) {
		return 0
	}

	if isMaximizing {
		bestScore := -1000
		for i := 0; i < 3; i++ {
			for j := 0; j < 3; j++ {
				if board.cells[i][j] == ' ' {
					board.cells[i][j] = 'O'
					score := minimax(board, depth+1, false)
					board.cells[i][j] = ' '
					if score > bestScore {
						bestScore = score
					}
				}
			}
		}
		return bestScore
	} else {
		bestScore := 1000
		for i := 0; i < 3; i++ {
			for j := 0; j < 3; j++ {
				if board.cells[i][j] == ' ' {
					board.cells[i][j] = 'X'
					score := minimax(board, depth+1, true)
					board.cells[i][j] = ' '
					if score < bestScore {
						bestScore = score
					}
				}
			}
		}
		return bestScore
	}
}
