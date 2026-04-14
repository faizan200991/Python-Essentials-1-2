package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	for {
		board := NewBoard()
		currentPlayer := 'X'
		gameOver := false

		fmt.Println("Welcome to Tic-Tac-Toe!")

		for !gameOver {
			board.Display()

			if currentPlayer == 'X' {
				fmt.Print("Enter your move (row and column: 1 1 for top-left): ")
				input, _ := reader.ReadString('\n')
				input = strings.TrimSpace(input)
				parts := strings.Split(input, " ")
				if len(parts) != 2 {
					fmt.Println("Invalid input. Please enter row and column numbers (e.g., 1 1).")
					continue
				}
				row, err1 := strconv.Atoi(parts[0])
				col, err2 := strconv.Atoi(parts[1])
				if err1 != nil || err2 != nil || !board.IsValidMove(row-1, col-1) {
					fmt.Println("Invalid move. Try again.")
					continue
				}
				board.MakeMove(row-1, col-1, 'X')
			} else {
				fmt.Println("AI is making a move...")
				aiRow, aiCol := getBestMove(board)
				board.MakeMove(aiRow, aiCol, 'O')
			}

			winner := checkWinner(board)
			if winner != ' ' {
				board.Display()
				if winner == 'X' {
					fmt.Println("Congratulations! You win!")
				} else {
					fmt.Println("AI wins! Better luck next time.")
				}
				gameOver = true
			} else if isDraw(board) {
				board.Display()
				fmt.Println("It's a draw!")
				gameOver = true
			} else {
				if currentPlayer == 'X' {
					currentPlayer = 'O'
				} else {
					currentPlayer = 'X'
				}
			}
		}

		fmt.Print("Play again? (y/n): ")
		again, _ := reader.ReadString('\n')
		again = strings.TrimSpace(strings.ToLower(again))
		if again != "y" {
			fmt.Println("Thanks for playing!")
			break
		}
	}
}
