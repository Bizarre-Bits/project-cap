import pygame
import setting
import os
import SingleActionSound

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))

setting.intro_img = pygame.image.load(os.path.join(setting.img_folder, "intro_0.png"))
class Intro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = setting.intro_img
        self.rect = self.image.get_rect()
        self.rect.center = (setting.WIDTH/2, setting.HEIGHT)

    ywl = 10
    def update(self):

        self.rect.y -= self.ywl
        if self.rect.center[1] <= setting.HEIGHT/2 :
            self.ywl = 0


all_sprites = pygame.sprite.Group()
intro = Intro()
all_sprites.add(intro)
def introPlay():

    intro_sound = SingleActionSound.SingleActionSound(os.path.join(setting.sound_folder, "intro_s.wav"))
    playingintro = True

    while playingintro:
        clock.tick(setting.FPS)
        intro_sound.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playingintro = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    playingintro = False


        all_sprites.update()

        ### render

        screen.fill(setting.BLACK)
        all_sprites.draw(screen)
        ### flip the screen
        pygame.display.flip()

    if playingintro == False :
        all_sprites.remove(intro)
