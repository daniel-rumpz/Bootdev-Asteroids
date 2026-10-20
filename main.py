import sys
import pygame, constants, player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")

	clock = pygame.time.Clock()
	dt = 0.0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	Shot.containers = (shots, updatable, drawable)

	player_x = SCREEN_WIDTH / 2
	player_y = SCREEN_HEIGHT / 2
	player = Player(player_x, player_y)

	while True:
		log_state()
		for event in pygame.event.get():
			pass

		updatable.update(dt)
		screen.fill("black")
		
		for drawing in drawable:
			drawing.draw(screen)
	
		pygame.display.flip()

		for asteroid in asteroids:
			if asteroid.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				sys.exit()

		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collides_with(shot):
					log_event("asteroid_shot")
					shot.kill()
					asteroid.split()

		dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
