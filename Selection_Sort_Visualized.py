import pygame as py
import random
import numpy as np


py.init()

length, height = 1200, 600
size = (length, height)
screen = py.display.set_mode(size)
py.display.set_caption("Selection Sort")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

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
        index = k
        for j in range(k+1, length):
            if values[index] > values[j]:
                index = j
        values[k], values[index] = values[index], values[k]
    k += 1

    for i in range(length):
        py.draw.line(screen, WHITE, [i, height], [i, height - values[i]])
    py.display.update()
