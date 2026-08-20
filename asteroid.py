import pygame # type: ignore
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius: float = self.radius
        old_velocity: pygame.Vector2 = self.velocity
        old_position: pygame.Vector2 = self.position
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")
            angle: float = random.uniform(20, 50)
            new_velocity_1: pygame.Vector2 = old_velocity.rotate(angle)
            new_velocity_2: pygame.Vector2 = old_velocity.rotate(-angle)
            new_radius: float = old_radius - ASTEROID_MIN_RADIUS
            new_asteroid_1: Asteroid = Asteroid(old_position.x, old_position.y, new_radius)
            new_asteroid_1.velocity = new_velocity_1 * 1.2
            new_asteroid_2: Asteroid = Asteroid(old_position.x, old_position.y, new_radius)
            new_asteroid_2.velocity = new_velocity_2 * 1.2