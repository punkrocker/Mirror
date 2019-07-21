from luma.core.render import canvas
from PIL import ImageFont
import time
from oled_setting import get_device


def stats(oled, content):
    font = ImageFont.load_default()
    with canvas(oled) as draw:
        draw.text((2, 5), content, font=font, fill=255)


def main():
    device = get_device()
    while True:
        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        stats(device, localtime)
        time.sleep(1)


if __name__ == "__main__":
    main()
