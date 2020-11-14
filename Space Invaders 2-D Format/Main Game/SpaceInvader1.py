import pygame 
import random
import math
from pygame import mixer

# Game Screen Initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Loading Required Images
icon = pygame.image.load('B:\\Portfolio\\Projects\\Python\\Self made projects\\Space Invader\\Images and Icons\\spaceship.png')
background = pygame.image.load('B:\\Portfolio\\Projects\\Python\\Self made projects\\Space Invader\\Images and Icons\\background.png')
bullet = pygame.image.load('B:\\Portfolio\\Projects\\Python\\Self made projects\\Space Invader\\Images and Icons\\ammunition.png')
player_img = pygame.image.load('B:\\Portfolio\\Projects\\Python\\Self made projects\\Space Invader\\Images and Icons\\player.png')
alien_img = pygame.image.load('B:\\Portfolio\\Projects\\Python\\Self made projects\\Space Invader\\Images and Icons\\alien.png')

# Loading Required Sounds
mixer.music.load('B:\\Portfolio\\Projects\\Python\\Self made projects\\Space Invader\\Sounds\\background.wav')
mixer.music.play(-1)
bullet_sound = mixer.Sound('B:\\Portfolio\\Projects\\Python\\Self made projects\\Space Invader\\Sounds\\laser.wav')
explosion_sound = mixer.Sound('B:\\Portfolio\\Projects\\Python\\Self made projects\\Space Invader\\Sounds\\explosion.wav')

# Setting up Icon 
pygame.display.set_icon(icon)
pygame.display.set_caption('Space Invader')

# Bullet Variables
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 4
bullet_state = 'ready'

# Player Variables
player_x = 370
player_y = 480
player_x_change = 0

# Enemy Variables
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 10

# Creating enemy objects
for i in range(num_of_enemies):

    enemy_img.append(alien_img)
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(1.3)
    enemy_y_change.append(40)

# Score Variables
score_value = 0
text_X = 10
text_y = 10

# Creating font objects
version_font = pygame.font.Font('freesansbold.ttf', 20)
version_text = version_font.render('Version 1.1', True, (255, 255, 255))

score_font = pygame.font.Font('freesansbold.ttf', 24)

over_font = pygame.font.Font('freesansbold.ttf', 80)

# Game Functions
def game_over_text():
    over_text = over_font.render('GAME OVER!', True, (255, 0, 0))
    screen.blit(over_text, (160, 250))

def show_score(x, y):
    score = score_font.render('Score: ' + str(score_value), True, (165,240,67))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    return distance < 27

if __name__ == '__main__':

    # Game loop
    running = True
    while running:

        # Adding background image
        screen.blit(background, (0,0))

        # To loop through events untill event is QUIT
        for event in pygame.event.get():

            # Quit Button
            if event.type == pygame.QUIT:
                running = False

            # Keyboard Controls
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    player_x_change = -1.5

                if event.key == pygame.K_RIGHT:
                    player_x_change = 1.5
                
                if event.key == pygame.K_SPACE:
                    if bullet_state == 'ready':
                        bullet_sound.play()
                        bullet_x = player_x
                        fire_bullet(bullet_x, bullet_y)

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0
        
        # Player Movement
        player_x += player_x_change

        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736

        # Loop for Enemy and Bullet controls
        for i in range(num_of_enemies):

            # Game Over
            if enemy_y[i] > 450:

                for j in range(num_of_enemies):
                    enemy_y[j] = 2000

                game_over_text()
                break

            # Enemy Movement
            enemy_x[i] += enemy_x_change[i]

            if enemy_x[i] <= 0:
                enemy_x_change[i] = 1.3
                enemy_y[i] += enemy_y_change[i]
            elif enemy_x[i] >= 736:
                enemy_x_change[i] = -1.3
                enemy_y[i] += enemy_y_change[i]

            # Bullet and Enemy Collision Control
            collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)

            if collision:
                explosion_sound.play()
                bullet_y = 480
                bullet_state = 'ready'
                score_value += 1
                enemy_x[i] = random.randint(0, 735)
                enemy_y[i] = random.randint(50, 200)

            # Drawing enemy image
            enemy(enemy_x[i], enemy_y[i], i)

        # Bullet Movement
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = 'ready'

        if bullet_state == "fire":
            fire_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change

        # Drawing final text and images
        screen.blit(version_text, (380, 0))
        player(player_x, player_y)
        show_score(text_X, text_y)

        # Updating screen
        pygame.display.update()