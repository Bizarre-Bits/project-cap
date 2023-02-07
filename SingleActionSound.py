import pygame.mixer


class SingleActionSound:
    sound: pygame.mixer.Sound
    was_played: bool = False

    def __init__(self, sound_path):
        self.sound = pygame.mixer.Sound(sound_path)

    def play(self):
        if self.was_played == False:
            self.was_played = True
            self.sound.play()