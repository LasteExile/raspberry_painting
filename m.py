for i in range(0, 16):
    print('<div class="row">')
    for j in range(0, 16):
        print(f'<div class="pixel y{i}x{j}" onclick="setPixelColor(this, \'{i} {j}\')"></div>')
    print('</div>')

