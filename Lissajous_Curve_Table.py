import pygame as py
import math
from random import randint


class Curve:
    def __init__(self):
        self.path = []
        self.a = 0
        self.b = 0
        self.color = random_color()

    def add_point(self, a, b):
        self.a = a
        self.b = b
        self.path.append((a, b))

    def show(self, screen):
        if len(self.path) > 1:
            py.draw.lines(screen, self.color, False, self.path, 1)
            py.draw.circle(screen, white, (self.a, self.b), 3, 0)

    def reset(self):
        self.path = []
        self.color = random_color()


def random_color():
    return randint(50, 220), randint(50, 220), randint(50, 220)


py.init()

clock = py.time.Clock()

width, height = 1200, 700
screen = py.display.set_mode((width, height))

black = (0, 0, 0)
white = (255, 255, 255)
grey = (100, 100, 100)

w = 100
d = int(w - 0.2*w)
r = int(d/2)
cols = int(width / w)
rows = int(height / w)

curves = [[Curve() for i in range(rows)] for j in range(cols)]

angle = 0

while True:

    clock.tick(60)

    for event in py.event.get():
        if event.type == py.QUIT:
            quit()
        elif event.type == py.KEYDOWN:
            quit()

    screen.fill(black)

    for i in range(cols):
        cx1 = int(w + i * w + w/2)
        cy1 = int(w/2)
        py.draw.circle(screen, white, (cx1, cy1), r, 1)
        x1 = int(r * math.cos(angle * (i + 1) - math.pi/2))
        y1 = int(r * math.sin(angle * (i + 1) - math.pi/2))
        py.draw.circle(screen, white, (cx1 + x1, cy1 + y1), 4, 0)
        py.draw.line(screen, grey, (cx1 + x1, cy1 + y1 + 4), (cx1 + x1, height), 1)

        for j in range(rows):
            cy2 = int(w + j * w + w/2)
            cx2 = int(w/2)
            py.draw.circle(screen, white, (cx2, cy2), r, 1)
            x2 = int(r * math.cos(angle * (j + 1) - math.pi/2))
            y2 = int(r * math.sin(angle * (j + 1) - math.pi/2))
            py.draw.circle(screen, white, (cx2 + x2, cy2 + y2), 4, 0)
            py.draw.line(screen, grey, (cx2 + x2 + 4, cy2 + y2), (width, cy2 + y2), 1)

            curves[i][j].add_point(cx1 + x1, cy2 + y2)
            curves[i][j].show(screen)

    angle -= 0.01

    if angle < - 2 * math.pi:
        angle = 0
        img = screen.copy()
        for i in range(cols):
            for j in range(rows):

                curves[i][j].reset()

        py.image.save(img, 'Lissajous.png')
    py.display.update()
