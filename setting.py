import os

WIDTH = 800
HEIGHT = 600
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# assets path
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "assets/graphics")
sound_folder = os.path.join(game_folder, "assets/sounds")
fonts_folder = os.path.join(game_folder, "assets/fonts")
