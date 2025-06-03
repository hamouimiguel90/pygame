import pygame
from random import *
from models.bullets import Bullets
from models.screen import Screen
from models.sounds import Sounds
from models.spaceship import SpaceShip
from utils.util import calculate_collision


# Initialize Pygame
pygame.init()

# controll de velocity of the game
clock = pygame.time.Clock()

# Create a window sized 800x600, Icon and Background
screen = Screen((800,600),'Space Invaders','assets/icon.png', 'assets/fondo.jpg')
screen.set_icon()


# spaceship
space_ship = SpaceShip('assets/spaceship.png', 368, 500)  # Create an instance of SpaceShip

# ovni spaceship
ovni_qty = 8
ovni_instance = []
ovni_directions = [0.3 for _ in range(ovni_qty)]


# sounds
sound = Sounds()
sound.set_background_music('assets/musicafondo.mp3')


for e in range(ovni_qty):
    ovni_instance.append(SpaceShip('assets/ovni.png', randint(0,736), randint(50,200), 0, 0.1))  # Create an instance of Enemy SpaceShip

# bullets
bullets = []
# bullets = Bullets('assets/bala.png', space_ship.x_position, 500)

#score
score_points = 0

# Bucle del juego
running = True
game_over = False
gameover_sound = False

while running:
    # # Control FPS to normalize the game velocity
    # clock.tick(60)

    # using dt Delta Time
    dt = clock.tick(50) / 1000
     # background
    screen.set_background()

    # Event handling
    for evento in pygame.event.get(): # for every event in the event queue
        if evento.type == pygame.QUIT:
            running = False
        # event to handle action in KEYDOWN buttons
        if not game_over:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    space_ship.change_x = -1.7
                if evento.key == pygame.K_RIGHT:
                    space_ship.change_x = 1.7
                if evento.key == pygame.K_SPACE:
                    bullets.append(Bullets('assets/bala.png', space_ship.x_position, 500))
                    sound.bullet_sound('assets/disparo.mp3')

            # event to handle action in KEYUP buttons
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    space_ship.change_x = 0

    if not game_over:
        for i, bullet in enumerate(bullets):
            bullet.y_position += -5
            bullet.position(screen.window)
            if bullet.y_position < 0:
                bullets.remove(bullet)

    if not game_over:
        for i, ovni in enumerate(ovni_instance):
            if ovni.y_position >= 471:
                game_over = True
                if not gameover_sound:
                    sound.collision_sound('assets/gameover.mp3')
                    gameover_sound = True
                break

            # We setting a default moving beetwen the square of 0.3 for EACH enemy ship
            ovni.change_x += ovni_directions[i]
            # here we tell the ovni to move between square
            if ovni.x_position <= 0:
                ovni_directions[i] = 0.2
                ovni.y_move(dt)
             # 800px - 64px(ship) = 736px
            elif ovni.x_position >= 736:
                ovni_directions[i] = -0.2
                ovni.y_move(dt)

            # colision
            for i, bullet in enumerate(bullets):
                collision = calculate_collision(ovni.x_position, ovni.y_position, bullet.x_position, bullet.y_position)
                if collision:
                    sound.collision_sound('assets/golpe.mp3')
                    bullets.remove(bullet)
                    score_points += 1
                    ovni.x_position = randint(0,736)
                    ovni.y_position = randint(50,200)
                    break

            # player ship movement and position
            ovni.x_move(dt)
            ovni.position(screen.window)

            # show score
            screen.set_score('assets/freesansbold.ttf', 32 , {"x": 10, "y": 10 } , score_points)

        # # bullet movement
        # if bullets.visibility_bullet:
        #     bullets.position(screen.window)
        #     bullets.y_position -= bullets.change_y

        space_ship.x_move(dt)
        space_ship.position(screen.window)
    else:
        #show gameOver text
        screen.game_over('assets/freesansbold.ttf', 100)

    screen.update()  # Update the display
