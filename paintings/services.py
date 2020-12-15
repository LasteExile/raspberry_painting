import neopixel
import board


pixels = neopixel.NeoPixel(board.D18, 256, auto_write=False)


def get_color(max_color, color):
    if color[0] == color[1] == color[2] == 255:
        color = (0, 0, 0)
    else:
        for i in range(0, 3):
            if color[i] == 255:
                color[i] = max_color
    return color




def render(array):
    for i in range(0, 16):
        for j in range(0, 16):
            if j % 2 == 0:
                z = 16 * j + i
            else:
                z = 16 * j + (15 - i)
            color = get_color(10, list(map(int, array[i][j][2].split(', '))))
            if pixels[z] != tuple(color):
                pixels[z] = tuple(color)
            else:
                print(pixels[z], tuple(color))
    else:
        pass
        #pixels.fill((0, 0, 0))
    pixels.show()
