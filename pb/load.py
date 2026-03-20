from PIL import Image


def load_image(pil_image: Image.Image, width: int, height: int) -> list[str]:
    image = pil_image.load()
    assert image

    pixels = []
    for y in range(0, height, 1):
        for x in range(0, width, 1):
            r, g, b, *_ = image[x, y]
            pixels.append(f'#{r:02x}{g:02x}{b:02x}')

    return pixels
