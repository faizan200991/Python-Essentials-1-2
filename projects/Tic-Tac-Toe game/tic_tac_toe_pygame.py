import pygame
import sys
import math

# --- Game Constants ---
WIDTH, HEIGHT = 400, 400
LINE_WIDTH = 8
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 8
CROSS_WIDTH = 8
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe (AI: O)')
font = pygame.font.SysFont(None, 48)

# --- Board ---
def create_board():
    return [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
            elif board[row][col] == 'O':
                center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)


# Returns (winner, winning_cells) where winning_cells is a list of (row, col) tuples
def check_winner(board):
    for i in range(BOARD_ROWS):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0], [(i,0),(i,1),(i,2)]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i], [(0,i),(1,i),(2,i)]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0], [(0,0),(1,1),(2,2)]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2], [(0,2),(1,1),(2,0)]
    return None, []

def is_draw(board):
    return all(board[row][col] != ' ' for row in range(BOARD_ROWS) for col in range(BOARD_COLS))

def minimax(board, is_max):
    winner, _ = check_winner(board)
    if winner == 'O':
        return 1
    if winner == 'X':
        return -1
    if is_draw(board):
        return 0
    if is_max:
        best = -math.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, False)
                    board[row][col] = ' '
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, True)
                    board[row][col] = ' '
                    best = min(best, score)
        return best

def best_move(board):
    best_score = -math.inf
    move = None
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                score = minimax(board, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def draw_status(message, submessage=None):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((255,255,255,180))
    screen.blit(overlay, (0,0))
    main_font = pygame.font.SysFont(None, 38)
    sub_font = pygame.font.SysFont(None, 26)
    text = main_font.render(message, True, (40, 40, 40))
    rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 - 10))
    screen.blit(text, rect)
    if submessage:
        subtext = sub_font.render(submessage, True, (120, 0, 0))
        subrect = subtext.get_rect(center=(WIDTH//2, HEIGHT//2 + 28))
        screen.blit(subtext, subrect)
    pygame.display.update()

def highlight_winner(cells):
    for (row, col) in cells:
        x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        y = row * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.circle(screen, (255,0,0), (x, y), SQUARE_SIZE//3, 6)

def main():
    board = create_board()
    player_turn = True
    running = True
    game_over = False
    screen.fill(BG_COLOR)
    draw_lines()
    winner = None
    winning_cells = []
    invalid_move = False
    after_game_click = False
    final_message = None
    final_submessage = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not game_over and player_turn and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // SQUARE_SIZE
                col = x // SQUARE_SIZE
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    winner, winning_cells = check_winner(board)
                    if winner or is_draw(board):
                        game_over = True
                        if winner == 'X':
                            final_message = 'You win!'
                        elif winner == 'O':
                            final_message = 'AI wins!'
                        else:
                            final_message = 'Draw!'
                        final_submessage = 'Press R to replay, or close to exit.'
                    else:
                        player_turn = False
                    invalid_move = False
                else:
                    invalid_move = True
            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                after_game_click = True
            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board = create_board()
                    player_turn = True
                    game_over = False
                    screen.fill(BG_COLOR)
                    draw_lines()
                    winner = None
                    winning_cells = []
                    invalid_move = False
                    after_game_click = False
                    final_message = None
                    final_submessage = None
        if not game_over and not player_turn:
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = 'O'
            winner, winning_cells = check_winner(board)
            if winner or is_draw(board):
                game_over = True
                if winner == 'X':
                    final_message = 'You win!'
                elif winner == 'O':
                    final_message = 'AI wins!'
                else:
                    final_message = 'Draw!'
                final_submessage = 'Press R to replay, or close to exit.'
            else:
                player_turn = True
        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures(board)
        if winner and winning_cells:
            highlight_winner(winning_cells)
        if game_over and final_message:
            draw_status(final_message, final_submessage)
        elif invalid_move:
            draw_status('Invalid move!', 'Pick an empty cell.')
        pygame.display.update()

if __name__ == "__main__":
    main()
