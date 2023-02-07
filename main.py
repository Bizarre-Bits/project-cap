import pygame
import random
import os
import setting
import math
import intros

player_img = pygame.image.load(os.path.join(setting.img_folder, "player.png"))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (setting.WIDTH / 2, setting.HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        self.rect.y = math.sin(self.rect.x) * 10 + 300
        if self.rect.left > setting.WIDTH:
            self.rect.right = 0




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

    ### update
    all_sprites.update()
    ### render

    screen.fill(setting.BLACK)
    all_sprites.draw(screen)
    ### After drawing everything, flip the screen
    pygame.display.flip()

pygame.quit()

# if __name__ == "__main__":
#     main()
