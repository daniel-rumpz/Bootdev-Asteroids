import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid (CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
	
	def update(self, dt: float) -> None:
		self.position += (self.velocity * dt)
	
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		
		log_event("asteroid_split")
		split_angle = random.uniform(20, 50)
		first_split = self.velocity.rotate(split_angle)
		second_split = self.velocity.rotate(-split_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		baby_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
		baby_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
		baby_asteroid1.velocity = first_split * 1.2
		baby_asteroid2.velocity = second_split * 1.2
			
