import pygame
import random
import os
import setting
import math
import intros

player_img = pygame.image.load(os.path.join(setting.img_folder, "player.png"))
background = pygame.image.load(os.path.join(setting.img_folder, "BG_0.png"))
background_rect = background.get_rect()
embimus = pygame.mixer.music.load(os.path.join(setting.sound_folder, "emb_1.wav"))
pygame.mixer.music.set_volume(0.7)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (30, setting.HEIGHT / 2)
        self.rect = self.image.get_rect()
        self.rect.centerx = setting.WIDTH / 2
        self.rect.bottom = setting.HEIGHT - 21
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > setting.WIDTH:
            self.rect.right = setting.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    ### Create game and window


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))
pygame.display.set_caption("Project CAP")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

### play intro

intros.introPlay()

pygame.mixer.music.play(loops= -1)
### game cycle

running = True
while running:
    ### cycle speed correction
    clock.tick(setting.FPS)
    ### launch event
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedx = -8
            if event.key == pygame.K_RIGHT:
                player.speedx = 8

    ### update
    all_sprites.update()

    ### render

    screen.fill(setting.BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    ### After drawing everything, flip the screen
    pygame.display.flip()

pygame.quit()

# if __name__ == "__main__":
#     main()
