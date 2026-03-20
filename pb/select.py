from pyautogui import position
from keyboard import wait

def get_coords():
    print('select start pixel')
    wait('shift')
    pos = position()
    print(f'selected: ({pos.x}, {pos.y})')
    return pos