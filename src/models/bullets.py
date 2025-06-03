import pygame

class Bullets:
    visibility_bullet = False
    def __init__(self, bullet_path, x_position: int = 0, y_position: int = 500, change_x: int = 0, change_y: int = 10):
        self.bullet_path = pygame.image.load(bullet_path)
        self.x_position = x_position
        self.y_position = y_position
        self.change_x = change_x
        self.change_y = change_y
        self.speed = 400 # base velocity in pixels per second


    def position(self, pantalla):
        """Set the position of the spaceship in screen."""
        self.visibility_bullet = True
        pantalla.blit(self.bullet_path,(self.x_position + 16 ,self.y_position + 10))


    def x_move(self, dt):
        """Move the spaceship by change_x."""
        self.x_position += self.change_x * dt * self.speed
        self.x_position = max(0, min(self.x_position, 736))

    def y_move(self, dt):
        self.y_position += self.change_y * dt * self.speed
        # self.y_position = max(0, min(self.y_position, 736))
