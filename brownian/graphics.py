# import pygame
# from .config import WIDTH, HEIGHT, WHITE, RED, ROBOT_RADIUS, FRAME_DELAY
# from .simulation import Robot

# def run_simulation():
#     """Runs the Pygame simulation with the Brownian motion robot."""
#     pygame.init()

#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("Brownian Motion - Robot Simulation")

#     robot = Robot()
#     running = True

#     while running:
#         pygame.time.delay(FRAME_DELAY)  # Control simulation speed
#         screen.fill(WHITE)  # Clear screen

#         # Move robot
#         robot.move()
#         x, y = robot.get_position()

#         # Draw robot
#         pygame.draw.circle(screen, RED, (x, y), ROBOT_RADIUS)

#         # Update display
#         pygame.display.update()

#         # Handle quit event
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#     pygame.quit()


import pygame
from .config import WIDTH, HEIGHT, WHITE, BLACK, RED, ROBOT_RADIUS, FRAME_DELAY
from .simulation import Robot

def run_simulation():
    """Runs the Pygame simulation with the Brownian motion robot."""
    pygame.init()

    screen = pygame.display.set_mode((WIDTH+100, HEIGHT+100))
    pygame.display.set_caption("Brownian Motion - Robot Simulation")

    robot = Robot()
    running = True

    while running:
        pygame.time.delay(FRAME_DELAY)  # Control simulation speed
        screen.fill(WHITE)  # Clear screen

        # Draw black boundary
        pygame.draw.rect(screen, BLACK, (50, 50, WIDTH, HEIGHT), 5)  # 5px border

        # Move robot
        robot.move()
        x, y = robot.get_position()

        # Draw robot
        pygame.draw.circle(screen, RED, (x, y), ROBOT_RADIUS)

        # Update display
        pygame.display.update()

        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

