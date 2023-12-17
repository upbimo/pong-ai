import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong AI")

# Define the paddles and ball
player_paddle = pygame.Rect(WIDTH - PADDLE_WIDTH - 10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ai_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

# Define initial ball speed and AI speed
ball_speed = [5, 5]
ai_speed = 0  # Initialize AI speed

# Function to handle collisions with walls and paddles
def handle_collisions():
    # Ball and wall collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Ball and paddle collisions
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        ball_speed[0] = -ball_speed[0]

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= 5
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += 5

    # Advanced AI strategy: Predict the ball's position based on speed
    ai_target = ball.centery - (ai_paddle.width // 2)
    if ai_target < ai_paddle.y:
        ai_speed = -5
    elif ai_target > ai_paddle.y:
        ai_speed = 5
    else:
        ai_speed = 0

    # Move the AI paddle
    ai_paddle.y += ai_speed

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Handle collisions
    handle_collisions()

    # Draw everything on the screen
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, player_paddle)
    pygame.draw.rect(win, WHITE, ai_paddle)
    pygame.draw.ellipse(win, WHITE, ball)

    pygame.display.flip()
    clock.tick(FPS)
