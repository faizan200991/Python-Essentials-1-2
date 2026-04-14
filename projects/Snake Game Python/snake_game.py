
import pygame
import random
import sys
import os

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 7

# Colors (modern neon style)
WHITE = (245, 245, 245)
NEON_GREEN = (57, 255, 20)
NEON_PINK = (255, 20, 147)
NEON_BLUE = (0, 255, 255)
NEON_YELLOW = (255, 255, 85)
BLACK = (10, 10, 20)

# Directions
directions = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0)
}

def draw_snake(surface, snake):
    for i, segment in enumerate(snake):
        x, y = segment
        if i == 0:
            # Head: larger, with eyes and tongue
            pygame.draw.ellipse(surface, NEON_GREEN, (x, y, CELL_SIZE, CELL_SIZE))
            # Eyes
            eye_radius = CELL_SIZE // 7
            eye_offset_x = CELL_SIZE // 4
            eye_offset_y = CELL_SIZE // 4
            pygame.draw.circle(surface, WHITE, (x + eye_offset_x, y + eye_offset_y), eye_radius)
            pygame.draw.circle(surface, WHITE, (x + CELL_SIZE - eye_offset_x, y + eye_offset_y), eye_radius)
            pygame.draw.circle(surface, BLACK, (x + eye_offset_x, y + eye_offset_y), eye_radius // 2)
            pygame.draw.circle(surface, BLACK, (x + CELL_SIZE - eye_offset_x, y + eye_offset_y), eye_radius // 2)
            # Tongue
            tongue_width = CELL_SIZE // 7
            tongue_length = CELL_SIZE // 2
            pygame.draw.rect(surface, NEON_PINK, (x + CELL_SIZE // 2 - tongue_width // 2, y + CELL_SIZE, tongue_width, tongue_length))
        else:
            # Body: smaller, rounded
            pygame.draw.ellipse(surface, NEON_BLUE, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.ellipse(surface, WHITE, (x+2, y+2, CELL_SIZE-4, CELL_SIZE-4), width=1)

def draw_food(surface, food):
    pygame.draw.ellipse(surface, NEON_PINK, (*food, CELL_SIZE, CELL_SIZE))
    pygame.draw.ellipse(surface, NEON_YELLOW, (food[0]+4, food[1]+4, CELL_SIZE-8, CELL_SIZE-8))

def random_food(snake):

    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)

# High score helpers
def load_high_score(filename="highscore.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                return int(f.read())
            except ValueError:
                return 0
    return 0

def save_high_score(score, filename="highscore.txt"):
    with open(filename, "w") as f:
        f.write(str(score))

# Menu helpers
def show_menu(screen, clock):
    font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 32)
    while True:
        screen.fill(BLACK)
        title = font.render("Snake Game", True, NEON_GREEN)
        prompt = small_font.render("Press SPACE to Start", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        clock.tick(15)

def show_game_over(screen, clock, score, high_score):
    font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 32)
    while True:
        screen.fill(BLACK)
        over = font.render("Game Over!", True, NEON_PINK)
        score_text = small_font.render(f"Score: {score}", True, WHITE)
        high_score_text = small_font.render(f"High Score: {high_score}", True, NEON_GREEN)
        prompt = small_font.render("Press SPACE to Restart or ESC to Quit", True, WHITE)
        screen.blit(over, (WIDTH // 2 - over.get_width() // 2, HEIGHT // 3))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 30))
        screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2))
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 + 40))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False
        clock.tick(15)



if __name__ == '__main__':
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    high_score = load_high_score()

    while True:
        show_menu(screen, clock)

        snake = [(WIDTH // 2, HEIGHT // 2)]
        direction = 'RIGHT'
        food = random_food(snake)
        score = 0
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != 'DOWN':
                        direction = 'UP'
                    elif event.key == pygame.K_DOWN and direction != 'UP':
                        direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                        direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        direction = 'RIGHT'

            # Move snake
            dx, dy = directions[direction]
            head = (snake[0][0] + dx * CELL_SIZE, snake[0][1] + dy * CELL_SIZE)
            snake.insert(0, head)

            # Check collision with food
            if head == food:
                score += 1
                food = random_food(snake)
            else:
                snake.pop()

            # Check collision with walls or self
            if (
                head[0] < 0 or head[0] >= WIDTH or
                head[1] < 0 or head[1] >= HEIGHT or
                head in snake[1:]
            ):
                running = False

            # Draw everything
            # Draw a friendly gradient background (blue to purple)
            for y in range(0, HEIGHT, 2):
                r = 30 + int(80 * (y / HEIGHT))
                g = 60 + int(60 * (y / HEIGHT))
                b = 180 + int(50 * (y / HEIGHT))
                pygame.draw.rect(screen, (r, g, b), (0, y, WIDTH, 2))
            draw_snake(screen, snake)
            draw_food(screen, food)
            # Draw score
            font = pygame.font.SysFont(None, 32)
            score_text = font.render(f"Score: {score}", True, WHITE)
            high_score_text = font.render(f"High Score: {high_score}", True, NEON_GREEN)
            screen.blit(score_text, (10, 10))
            screen.blit(high_score_text, (10, 40))
            pygame.display.flip()
            clock.tick(FPS)

        if score > high_score:
            high_score = score
            save_high_score(high_score)

        restart = show_game_over(screen, clock, score, high_score)
        if not restart:
            break

    pygame.quit()
    sys.exit()
    main()
