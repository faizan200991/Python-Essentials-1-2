package main

// Rule checker for win/draw detection.
// checkWinner returns 'X' or 'O' if there is a winner, or ' ' if no winner yet.
func checkWinner(board *Board) rune {
	// Check rows and columns
	for i := 0; i < 3; i++ {
		if board.cells[i][0] != ' ' && board.cells[i][0] == board.cells[i][1] && board.cells[i][1] == board.cells[i][2] {
			return board.cells[i][0]
		}
		if board.cells[0][i] != ' ' && board.cells[0][i] == board.cells[1][i] && board.cells[1][i] == board.cells[2][i] {
			return board.cells[0][i]
		}
	}

	// Check diagonals
	if board.cells[0][0] != ' ' && board.cells[0][0] == board.cells[1][1] && board.cells[1][1] == board.cells[2][2] {
		return board.cells[0][0]
	}
	if board.cells[0][2] != ' ' && board.cells[0][2] == board.cells[1][1] && board.cells[1][1] == board.cells[2][0] {
		return board.cells[0][2]
	}

	return ' '
}

// isDraw returns true if the board is full and there is no winner.
func isDraw(board *Board) bool {
	if checkWinner(board) != ' ' {
		return false
	}
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if board.cells[i][j] == ' ' {
				return false
			}
		}
	}
	return true
}
