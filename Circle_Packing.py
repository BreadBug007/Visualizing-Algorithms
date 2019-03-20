import pygame as py
import random
import math


class Circle():
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.r = 2
        self.id = id
        self.active = True


# py.init()

w, h = 1920, 1080

# screen = py.display.set_mode((w,h))
black = (0, 0, 0)
white = (255, 255, 255)

circles = []

attempt = 0
max_attempts = 10000
finish = False

while True:
    while True:

        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)

        found_space = True

        for c in circles:
            dist = math.hypot((c.x - x), (c.y - y))
            if dist <= c.r + 2:
                found_space = False
                break
        if found_space: break
        attempt += 1
        if attempt >= max_attempts:
            finish = True
            break

    if finish: break
    circles.append(Circle(x, y, len(circles)))

    for c in circles:
        if not c.active:
            continue
        for C in circles:
            if c.id == C.id:
                continue
            distance = math.hypot((C.x-c.x), (C.y-c.y))
            total_radius = C.r + c.r
            if distance <= total_radius + 2:
                c.active = False
                C.active = False
                break
        if c.active:
            c.r += 1
        # py.draw.circle(screen, white, (c.x, c.y), c.r, 1)
        # py.display.update()

image = py.Surface((w,h))

for c in circles:
    py.draw.circle(image, white, (c.x, c.y), c.r, 1)

py.image.save(image, "Circle.png")
