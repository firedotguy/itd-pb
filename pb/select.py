from pyautogui import Point, position
from keyboard import wait

def select(info: str = 'select pixel') -> Point:
    print(info)
    wait('shift')
    pos = position()
    print(f'selected: ({pos.x}, {pos.y})')
    return pos