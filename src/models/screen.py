import pygame

class Screen:
    def __init__(self, size: tuple, title: str, icon_path: str, background_path: str):
        self.window = pygame.display.set_mode(size)
        self.title = pygame.display.set_caption(title)
        self.icon_path = pygame.image.load(icon_path)
        self.background_path = pygame.image.load(background_path)

    def set_icon(self):
        pygame.display.set_icon(self.icon_path)

    def set_color(self, color: tuple):
        self.window.fill(color)

    def set_background(self):
        self.window.blit(self.background_path, (0, 0))

    def set_score(self, type: str, size: int, position: object, value: str):
        x, y = position["x"], position["y"]
        font = pygame.font.Font(type, size)
        text = font.render(f"Score: {value}", True, (255,255,255) )
        self.window.blit(text, (x, y))

    def game_over(self, type, size):
        font = pygame.font.Font(type, size)
        text = font.render(f"Game Over", True, (255,255,255) )
        self.window.blit(text, (100, 200)) # almost the middle of the window screen


    def update(self):
        pygame.display.update()