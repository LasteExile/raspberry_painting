import board
import neopixel
import logging


logging.basicConfig(level=logging.WARNING)
pixels = neopixel.NeoPixel(board.D18, 256, auto_write=True)


def render(color=0, coord=[]):
    if not coord == []:
        if coord[1] % 2 == 0:
            z = 16 * coord[1] + coord[0]
        else:
            z = 16 * coord[1] + (15 - coord[0])
        pixels[z] = color
    else:
        pixels.fill((0, 0, 0))


def get_color(max_color, color):
    color = list(map(int, color.split(', ')))
    if color[0] == color[1] == color[2] == 255:
        color = (0, 0, 0)
    else:
        for i in range(0, 3):
            if color[i] == 255:
                color[i] = max_color
    return tuple(color)
