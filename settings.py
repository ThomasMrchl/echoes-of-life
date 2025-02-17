import pygame

#window settings
WIDTH = 1200
HEIGHT = 800
BACKGROUND_COLOR = (0, 0, 0)

#particle settings
NUM_PARTICLES = 500
ATTRACTION_RADIUS = 50
SPEED = 0.001
COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255)   # Cyan
]
ATTRACTION_MATRIX = [
    [0, -0.05, 0.1, -0.05, 0.1, -0.05],  # Red
    [-0.05, 0, -0.05, 0.1, -0.05, 0.1],  # Green
    [0.1, -0.05, 0, -0.05, 0.1, -0.05],  # Blue
    [-0.05, 0.1, -0.05, 0, -0.05, 0.1],  # Yellow
    [0.1, -0.05, 0.1, -0.05, 0, -0.05],  # Magenta
    [-0.05, 0.1, -0.05, 0.1, -0.05, 0]   # Cyan
]
#sound settings