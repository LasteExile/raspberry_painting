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
