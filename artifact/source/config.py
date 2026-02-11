import os

# screen constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

# dynamic path calculation
BASE_DIR = os.path.dirname(os.path.dirname(os.path.adspath(__file__)))
VISUALS_DIR = os.path.join(BASE_DIR, "visuals")