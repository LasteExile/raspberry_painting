def get_color(max_color, color):
    if color[0] == color[1] == color[2] == 255:
        color = (0, 0, 0)
    else:
        for i in range(0, 3):
            if color[i] == 255:
                color[i] = max_color
    return tuple(color)
