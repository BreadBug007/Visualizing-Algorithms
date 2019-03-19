import pygame as py
import random
import numpy as np


def selection(arr, k):
    index = k
    for j in range(k + 1, length):
        if arr[index] > arr[j]:
            index = j
    arr[k], arr[index] = arr[index], arr[k]
    return display_arr(arr)


def display_arr(arr):
    for i in range(length):
        py.draw.line(screen, WHITE, [i, height], [i, height - arr[i]])


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
        selection(values, k)
    else:
        py.time.delay(1000)
        break
    k += 1

    py.display.update()
