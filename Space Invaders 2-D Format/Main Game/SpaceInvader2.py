import pygame
import random
import math
from pygame import mixer
import time
import os

# Game Screen Initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Loading Images
icon = pygame.image.load('spaceship.png').convert_alpha()
game_background = pygame.image.load('space.png').convert_alpha()
home_screen_img = pygame.image.load('home_screen.png').convert_alpha()
bullet = pygame.image.load('ammunition.png').convert_alpha()
alien_img = pygame.image.load('alien.png').convert_alpha()
alien_img2 = pygame.image.load('alien2.png').convert_alpha()
player_img = pygame.image.load('player.png').convert_alpha()
settings_img = pygame.image.load('settings.png').convert_alpha()
controls_img = pygame.image.load('controls.png').convert_alpha()
game_over_img = pygame.image.load('game_over.png').convert_alpha()

# Loading sounds
mixer.music.load('background.wav')
mixer.music.play(-1)

bullet_sound = mixer.Sound('laser.wav')
explosion_sound = mixer.Sound('explosion.wav')

# Title and Icon
pygame.display.set_caption('Space Invader')
pygame.display.set_icon(icon)

# Bullet variables
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 2
bullet_state = 'ready'

# Player variables
player_x = 370
player_y = 480
player_x_change = 0

# Enemy variables
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 10

# Creating 10 enemy objects
for i in range(num_of_enemies):

    enemy_img.append(random.choice([alien_img, alien_img2]))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(0.5)
    enemy_y_change.append(30)

# Score variables
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 24)
over_font = pygame.font.Font('freesansbold.ttf', 80)

text_X = 10
text_y = 10

# Game Functions
def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (165,240,67))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render('GAME OVER!', True, (255, 0, 0))
    screen.blit(over_text, (160, 250))

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

# Button colors and fonts
color = (0, 0, 0)
color_light = (100,149,237)
color_dark = (138,43,226)

# Fonts
game_name_font = pygame.font.SysFont("Chiller", 140)
btn_font = pygame.font.SysFont('Corbel Bold', 34)
random_font = pygame.font.SysFont('Arial', 60)
info_btn = pygame.font.SysFont('Century Gothic', 24)
controls_font = pygame.font.SysFont('Consolas', 15)
credits_btn = pygame.font.SysFont('Consolas', 18)

# Texts
game_text = game_name_font.render('Space Invaders!', True, (255,255,0))
play_text = btn_font.render('Play Game', True, color)
controls_text = btn_font.render('Controls', True, color)
credits_text = btn_font.render('Credits', True, color)
settings_text = btn_font.render('Settings', True, color)
quit_text = btn_font.render('Quit Game', True, color)
version_text = btn_font.render('Version 2.8', True, (255, 255, 255))
back_text = btn_font.render('Go Back', True, color)
under_development_text = random_font.render('This area is under development', True, (0, 0, 0))

# Controls text
controls_1 = controls_font.render('Left Arrow   :   Spaceship moves Left', True, (124, 252, 0))
controls_2 = controls_font.render('Right Arrow  :  Spaceship moves Right', True, (124, 252, 0))
controls_3 = controls_font.render('Spacebar     :         Shoots bullets', True, (124, 252, 0))

# Credits text
credits_line_1 = credits_btn.render("The games first version was made while learning from the pygame video", True, (255, 255, 255))
credits_line_2 = credits_btn.render("of FreeCodeCamp.org. The successive updates in version 1 and 2 are", True, (255, 255, 255))
credits_line_3 = credits_btn.render("made by Armaan Barak. No external code was copied. But help was taken", True, (255, 255, 255))
credits_line_4 = credits_btn.render("from google. Images and icons shown this game are taken from freepik.com", True, (255, 255, 255))
credits_line_5 = credits_btn.render("and flaticon.com respectively. The images were resized from", True, (255, 255, 255))
credits_line_6 = credits_btn.render("reduceimages.com and the sounds are imported from github account of", True, (255, 255, 255))
credits_line_7 = credits_btn.render("Mr. Attreya Bhatt. Direct Link to repository:", True, (255, 255, 255))
credits_line_8 = credits_btn.render("https://github.com/attreyabhatt/Space-Invaders-Pygame.", True, (255, 255, 255))
credits_line_9 = credits_btn.render("This game is free and open-source. User is independent for", True, (255, 255, 255))
credits_line_10 = credits_btn.render("manipulating code but it's encouraged that you avoid cheating.", True, (255, 255, 255))
credits_line_11 = credits_btn.render("Creator and Developer: Armaan Barak", True, (255, 255, 255))

# Game loop variables
running = True
home_screen = True
settings = False
controls = False
game_screen = False
credits_screen = False
game_over_screen = False

while running:

    mouse = pygame.mouse.get_pos()

    # To loop through events untill event is QUIT
    for event in pygame.event.get():

        # QUIT Button
        if event.type == pygame.QUIT:
            running = False

        # Mouse key controls
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            # Game is Over
            if game_over_screen:
                
                if 250 <= mouse[0] <= 385 and 520 <= mouse[1] <= 560:
                    home_screen = True
                    settings = False
                    controls = False
                    game_screen = False
                    credits_screen = False
                    game_over_screen = False

                    for i in range(num_of_enemies):
                        enemy_y[i] = random.randint(50, 200)
                    
                    player_y = 480
                    bullet_y = 480

                if 420 <= mouse[0] <= 560 and 520 <= mouse[1] <= 560:
                    quit()

            # Play button clicked
            if 230 <= mouse[0] <= 370 and 270 <= mouse[1] <= 310:
                home_screen = False
                settings = False
                controls = False
                game_screen = True
                credits_screen = False

            # Instructions button clicked
            if 400 <= mouse[0] <= 540 and 270 <= mouse[1] <= 310:
                home_screen = False
                settings = False
                controls = True
                game_screen = False
                credits_screen = False

            # Settings button clicked
            if 230 <= mouse[0] <= 370 and 350 <= mouse[1] <= 390:
                home_screen = False
                settings = True
                controls = False
                game_screen = False
                credits_screen = False
            
            # Credits button clicked
            if 400 <= mouse[0] <= 540 and 350 <= mouse[1] <= 390:
                home_screen = False
                settings = False
                controls = False
                game_screen = False
                credits_screen = True

            # Quit button clicked
            if 315 <= mouse[0] <= 455 and 430 <= mouse[1] <= 470:
                quit()

            if settings or controls or credits_screen:

                if 50 <= mouse[0] <= 165 and 30 <= mouse[1] <= 70:
                    home_screen = True
                    settings = False
                    controls = False
                    game_screen = False
                    credits_screen = False

        # KeyBoard Controls
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_x_change = -.8

            if event.key == pygame.K_RIGHT:
                player_x_change = .8
            
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    
                    bullet_sound.play()
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        # Reseting player's x axis speed when left or right key is lifted
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               player_x_change = 0
    
    # Home Screen
    if home_screen:
        
        # Displaying main screen
        screen.blit(home_screen_img, (0,0))

        # Getting Mouse Position
        mouse = pygame.mouse.get_pos()

        # Changing color of text boxes on the basis of cursor position
        # play game text
        if 230 <= mouse[0] <= 370 and 270 <= mouse[1] <= 310:
            pygame.draw.rect(screen, color_light, [230, 270, 140, 40])
        
        else:
            pygame.draw.rect(screen, color_dark,[230,270,140,40])

        # instructions text
        if 400 <= mouse[0] <= 540 and 270 <= mouse[1] <= 310:
            pygame.draw.rect(screen, color_light, [400, 270, 140, 40])
        
        else:
            pygame.draw.rect(screen, color_dark, [400, 270, 140, 40])

        # settings text
        if 230 <= mouse[0] <= 370 and 350 <= mouse[1] <= 390:
            pygame.draw.rect(screen, color_light, [230, 350, 140, 40])
        
        else:
            pygame.draw.rect(screen, color_dark, [230, 350, 140, 40])

        # credits text
        if 400 <= mouse[0] <= 540 and 350 <= mouse[1] <= 390:
            pygame.draw.rect(screen, color_light, [400, 350, 140, 40])
        
        else:
            pygame.draw.rect(screen, color_dark, [400, 350, 140, 40])

        # quit game text
        if 315 <= mouse[0] <= 455 and 430 <= mouse[1] <= 470:
            pygame.draw.rect(screen, color_light, [315, 430, 140, 40])
        
        else:
            pygame.draw.rect(screen, color_dark, [315, 430, 140, 40])

        # Displaying text
        screen.blit(game_text, (90, 100))

        # Displaying buttons
        screen.blit(play_text, (240, 280))

        screen.blit(controls_text, (421, 280))

        screen.blit(settings_text, (253, 360))

        screen.blit(credits_text, (427, 360))

        screen.blit(quit_text, (325, 440))

        # Version Display
        screen.blit(version_text, (325, 580))

        # Updating Screen
        pygame.display.update()

    # Settings Screen
    elif settings:

        screen.blit(settings_img, (0, 0))

        mouse = pygame.mouse.get_pos()

        if 50 <= mouse[0] <= 165 and 30 <= mouse[1] <= 70:
            pygame.draw.rect(screen, color_light, [50, 30, 115, 40])
        else:
            pygame.draw.rect(screen, color_dark, [50, 30, 115, 40])

        screen.blit(back_text, (60, 40))

        screen.blit(under_development_text, (60, 250))

        pygame.display.update()
    
    # Controls Screen
    elif controls:
        
        screen.blit(controls_img, (0, 0))

        mouse = pygame.mouse.get_pos()

        if 50 <= mouse[0] <= 165 and 30 <= mouse[1] <= 70:
            pygame.draw.rect(screen, color_light, [50, 30, 115, 40])
        else:
            pygame.draw.rect(screen, color_dark, [50, 30, 115, 40])

        screen.blit(back_text, (60, 40))

        screen.blit(controls_1, (255, 240))
        screen.blit(controls_2, (255, 290))
        screen.blit(controls_3, (255, 340))

        pygame.display.update()

    # Credits Screen
    elif credits_screen:

        screen.fill((85, 107, 47))

        mouse = pygame.mouse.get_pos()

        if 50 <= mouse[0] <= 165 and 30 <= mouse[1] <= 70:
            pygame.draw.rect(screen, color_light, [50, 30, 115, 40])
        else:
            pygame.draw.rect(screen, color_dark, [50, 30, 115, 40])

        screen.blit(back_text, (60, 40))

        screen.blit(credits_line_1, (40, 150))
        screen.blit(credits_line_2, (40, 180))
        screen.blit(credits_line_3, (40, 210))
        screen.blit(credits_line_4, (40, 240))
        screen.blit(credits_line_5, (40, 270))
        screen.blit(credits_line_6, (40, 300))
        screen.blit(credits_line_7, (40, 330))
        screen.blit(credits_line_8, (40, 360))
        screen.blit(credits_line_9, (40, 390))
        screen.blit(credits_line_10, (40, 420))
        screen.blit(credits_line_11, (40, 450))

        pygame.display.update()

    # Game Screen
    else:

        # Adding background image
        screen.blit(game_background, (0,0))

        # Player Movement
        player_x += player_x_change

        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736

        # Handling movement of enemies
        for i in range(num_of_enemies):

            # Game Over
            if enemy_y[i] > 450:
                
                game_over_screen = True

                # Hiding Characters
                for j in range(num_of_enemies):
                    enemy_y[j] = 2000

                player_y = -2000
                bullet_y = -4000

                screen.blit(game_over_img, (0, 0))
                
                # Back button
                if 250 <= mouse[0] <= 385 and 520 <= mouse[1] <= 560:
                    pygame.draw.rect(screen, color_light, [250, 520, 140, 40])
                else:
                    pygame.draw.rect(screen, color_dark, [250, 520, 140, 40])

                # Quit Button
                if 420 <= mouse[0] <= 560 and 520 <= mouse[1] <= 560:
                    pygame.draw.rect(screen, color_light, [420, 520, 140, 40])
                else:
                    pygame.draw.rect(screen, color_dark, [420, 520, 140, 40])

                mouse = pygame.mouse.get_pos()

                screen.blit(back_text, (270, 530))

                screen.blit(quit_text, (430, 530))

            # Enemy Movement
            enemy_x[i] += enemy_x_change[i]

            if enemy_x[i] <= 0:
                enemy_x_change[i] = .5
                enemy_y[i] += enemy_y_change[i]
            elif enemy_x[i] >= 736:
                enemy_x_change[i] = -.5
                enemy_y[i] += enemy_y_change[i]

            # Collision control
            collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)

            if collision:
                
                explosion_sound.play()
                bullet_y = 480
                bullet_state = 'ready'
                score_value += 1
                enemy_x[i] = random.randint(0, 735)
                enemy_y[i] = random.randint(50, 200)

            # drawing enemy
            enemy(enemy_x[i], enemy_y[i], i)
        
        # Bullet Movement
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = 'ready'

        if bullet_state == "fire":
            fire_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change

        # drawing player
        player(player_x, player_y)

        # Version Display
        screen.blit(version_text, (325, 580))

        # drawing score card
        show_score(text_X, text_y)

        # Updates screen
        pygame.display.update()