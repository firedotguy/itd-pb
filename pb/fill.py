from pyautogui import (
    click, Point, moveTo as move_to, locateCenterOnScreen as locate_on_screen,
    pixel as get_pixel_color, ImageNotFoundException, press
)
from time import sleep


PALETTE_PADDING = 55
PIXEL_PADDING = 22


pallete = {}
x = base_x = 1610
y = 360
row = 0

for color in [
    '#ffffff', '#e4e4e4', '#888888', '#222222', '#000000', '#5a301d', '#a06a42', '#ffc48c',
    '#6d001a', '#be0039', '#e50000', '#ff3881', '#ffa7d1', '#de107f', '#e59500', '#ffa800',
    '#e5d900', '#fff8b8', '#005f39', '#02be01', '#94e044', '#0000ea', '#0083c7', '#3690ea',
    '#00d3dd', '#51e9f4', '#493ac1', '#6a5cff', '#b44ac0', '#811e9f', '#2b2d42'
]:
    pallete[color] = Point(x, y)
    x += PALETTE_PADDING
    row += 1
    if row == 5:
        x = base_x
        y += PALETTE_PADDING
        row = 0


def test_pallete():
    sleep(3)
    for point in pallete.values():
        move_to(*point)
        sleep(0.1)

def test_pixels(pos: Point):
    sleep(3)
    move_to(pos.x, pos.y)
    for i in range(0, 32):
        move_to(pos.x + (i * PIXEL_PADDING))
        sleep(0.15)

    move_to(pos.x, pos.y)
    for i in range(0, 32):
        move_to(y=pos.y + (i * PIXEL_PADDING))
        sleep(0.15)

# euclid diff made by claude, i am not so clever
def _color_dist(c1: str, c2: str) -> int:
    r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
    r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
    return (r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2

def snap_to_palette(color: str) -> str:
    return min(pallete.keys(), key=lambda c: _color_dist(c, color))


def set_color(color: str):
    if color not in pallete:
        raise ValueError(f'{color} not in color list')
    click(*pallete[color])


def fill(pos: Point, width: int, image: list[str]):
    sleep(3)
    move_to(pos.x, pos.y)
    current_pos = [pos.x, pos.y] # cant use Point cuz it is read only
    row = 0
    for pixel in image:
        press('esc') # reset last pixel selection
        sleep(0.2)

        r, g, b = get_pixel_color(*current_pos)
        screen_pixel = f'#{r:02x}{g:02x}{b:02x}'
        move_to(current_pos)

        # print(f'it is {snap_to_palette(screen_pixel)}')
        sleep(0.1)

        if _color_dist(screen_pixel, pixel) > 1200:
            set_color(pixel)
            print(f'fill ({current_pos[0]}, {current_pos[1]}) to {pixel} (was {screen_pixel})')
            click(current_pos)
            sleep(0.3)

            try:
                # move_to(current_pos[0] + 200, current_pos[1] - 100)
                # sleep(0.3)
                # move_to(current_pos[0] + 350, current_pos[1] + 50)

                cross = locate_on_screen('cross.png', region=(current_pos[0] + 150, current_pos[1] - 150, 300, 150), confidence=0.7, grayscale=True)
                assert cross #675 520  940 470
                click(*cross) # close pixel info

            except ImageNotFoundException:
                print('no cross')

            finally:
                sleep(0.1)
                click(1720, 780) # "ПОСТАВИТЬ"
                print('set')
                sleep(30)
        else:
            print(f'skip (pixel already {pixel})')

        current_pos[0] += PIXEL_PADDING
        row += 1
        if row == width:
            print('move down')
            row = 0
            current_pos = [pos.x, current_pos[1] + PIXEL_PADDING]