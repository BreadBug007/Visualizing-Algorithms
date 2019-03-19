import pygame as py
import random
import numpy as np


py.init()

length, height = 1200, 600
size = (length, height)
screen = py.display.set_mode(size)
py.display.set_caption("Bubble Sort")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

values = np.zeros((length,))
for i in range(length):
    values[i] = random.random()*height

k = 0

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            break

    screen.fill(BLACK)

    if k < length:
        for j in range(length - k - 1):
            a, b = values[j], values[j+1]
            if a > b:
                a, b = b, a
                values[j] = a
                values[j+1] = b
    else:
        py.time.delay(1000)
        break
    k += 1

    for i in range(length):
        py.draw.line(screen, WHITE, [i, height], [i, height - values[i]])
    py.display.update()
