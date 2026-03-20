from PIL import Image
from keyboard import add_hotkey
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from pb.select import get_coords
from pb.load import load_image
from pb.fill import fill

PATH = 'pb.png'

add_hotkey('Ctrl+C', lambda: quit())

pil_image = Image.open(PATH)
image = load_image(pil_image, *pil_image.size)
coords = get_coords()

fill(coords, pil_image.size[0], image)