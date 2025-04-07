import random
import math
from .config import WIDTH, HEIGHT, SPEED

class Robot:
    def __init__(self):
        """Initialize robot in the middle of the arena with random movement direction."""
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = SPEED
        self.angle = random.uniform(0, 2 * math.pi)  # Random initial direction

    def move(self):
        """Computes the next position and handles boundary collisions."""
        new_x = self.x + self.speed * math.cos(self.angle)
        new_y = self.y + self.speed * math.sin(self.angle)

        # Check for boundary collisions
        if new_x - 10 <= 50 or new_x + 10 >= WIDTH+50:
            self.angle = random.uniform(0, 2 * math.pi)  # Random bounce
        elif new_y - 10 <= 50 or new_y + 10 >= HEIGHT+50:
            self.angle = random.uniform(0, 2 * math.pi)  # Random bounce
        else:
            self.x, self.y = new_x, new_y  # Update position

    def get_position(self):
        """Returns the current position of the robot."""
        return int(self.x), int(self.y)
