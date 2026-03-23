from PIL import Image
from keyboard import add_hotkey
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from pb.select import select
from pb.load import load_image
from pb.fill import fill, calc_padding

PATH = 'pb.png'

add_hotkey('Ctrl+C', lambda: quit())

accounts = [select(f'select account {i}') for i in range(int(input('accounts: ')))]
pil_image = Image.open(PATH)
image = load_image(pil_image, *pil_image.size)
left = select('select top left pixel')
right = select('select top right pixel')

fill(left, pil_image.size[0], image, accounts, calc_padding(pil_image.size[0], left, right))