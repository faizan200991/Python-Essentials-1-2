package main

// Board represents the Tic-Tac-Toe board and its operations.
type Board struct {
	cells [3][3]rune // 'X', 'O', or ' '
}


// NewBoard initializes a new empty board.
func NewBoard() *Board {
	b := &Board{}
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			b.cells[i][j] = ' '
		}
	}
	return b
}

// Display prints the board to the console.
func (b *Board) Display() {
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if j > 0 {
				print(" | ")
			}
			if b.cells[i][j] == ' ' {
				print(" ")
			} else {
				print(string(b.cells[i][j]))
			}
		}
		println()
		if i < 2 {
			println("---------")
		}
	}
}

// IsValidMove checks if a move is valid (cell is empty and in range).
func (b *Board) IsValidMove(row, col int) bool {
	return row >= 0 && row < 3 && col >= 0 && col < 3 && b.cells[row][col] == ' '
}

// MakeMove places a mark ('X' or 'O') on the board if valid.
func (b *Board) MakeMove(row, col int, mark rune) bool {
	if b.IsValidMove(row, col) {
		b.cells[row][col] = mark
		return true
	}
	return false
}
