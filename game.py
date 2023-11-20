import pygame
from pygame.locals import *

pygame.init()
white = (255, 255, 255)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('game_name')

font = pygame.font.Font(None, 36)


class Button:
    def __init__(self, text, position, name):
        self.text = text
        self.position = position
        self.name = name
        self.rendered_text = font.render(self.text, True, white)
        self.rect = self.rendered_text.get_rect(topleft=position)

    def render(self, screen):
        screen.blit(self.rendered_text, self.position)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

def menu():
    image = pygame.image.load('Assets/space.png')
    image = pygame.transform.scale(image, (640, 480))

    buttons = [
        Button("START", (10, 10), "START"),
        Button("PLAY", (100, 10), "PLAY"),
        Button("STOP", (200, 10), "STOP")
    ]
    while True:
        screen.blit(image, (0, 0))

        for button in buttons:
            button.render(screen)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(event.pos):
                        if button.name == "START":
                            game()
                        else:
                            print(f'Clicked {button.text}')

def game():
    image = pygame.image.load('Assets/space.png')
    image = pygame.transform.scale(image, (640, 480))
    # player_rect = pygame.Rect(50, 50, 50, 50)
    player = pygame.image.load('Assets/spaceship_red.png')
    player = pygame.transform.rotozoom(player,0,0.1)
    player = pygame.transform.rotate(player, -90)
    player_pos = pygame.Vector2(50, 325)
    bgx = 0
    player_speed = 5
    # add key states for continuous movement when holding down key
    x = 100
    y = 100

    while True:
        screen.blit(image, (bgx-640, 0))
        screen.blit(image, (bgx, 0))
        screen.blit(image, (bgx+640, 0))

        bgx = bgx - 2
        if bgx <= -640 or bgx >= 640:
            bgx=0

        screen.blit(player, (x, y))

        # pygame.draw.rect(screen, (255, 0, 5), player_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         print('jump')
            #     if event.key == pygame.K_LEFT:
            #         x -= player_speed
            #     if event.key == pygame.K_RIGHT:
            #         x += player_speed
            #     if event.key == pygame.K_UP:
            #         y -= player_speed
            #     if event.key == pygame.K_DOWN:
            #         y += player_speed

            # Storing the key pressed in a
        # new variable using key.get_pressed()
        # method
        key_pressed_is = pygame.key.get_pressed()

        # Changing the coordinates
        # of the player
        if key_pressed_is[K_LEFT]:
            x -= 8
        if key_pressed_is[K_RIGHT]:
            x += 8
        if key_pressed_is[K_UP]:
            y -= 8
        if key_pressed_is[K_DOWN]:
            y += 8

        # Draws the surface object to the screen.
        pygame.display.update()

        pygame.time.Clock().tick(60)

menu()