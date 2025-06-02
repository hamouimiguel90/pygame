import pygame

class SpaceShip:
    def __init__(self, icon_path: str , x_position: int = 0, y_position: int = 0, change_x: int = 0, change_y: int = 0.1):
        self.icon = pygame.image.load(icon_path)
        self.x_position = x_position
        self.y_position = y_position
        self.change_x = change_x
        self.change_y = change_y
        self.speed = 300 # base velocity in pixels per second


    def position(self, pantalla):
        """Set the position of the spaceship in screen."""
        pantalla.blit(self.icon,(self.x_position,self.y_position))

    def x_move(self, dt):
        """Move the spaceship by change_x."""
        self.x_position += self.change_x * dt * self.speed
        self.x_position = max(0, min(self.x_position, 736))

    def y_move(self, dt):
        self.y_position += self.change_y * dt * self.speed
        # self.y_position = max(0, min(self.y_position, 736))
