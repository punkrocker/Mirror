from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont
import time


def stats(oled, content):
    font = ImageFont.load_default()
    with canvas(oled) as draw:
        draw.text((2, 5), content, font=font, fill=255)


def main():
    serial = i2c(port=1, address=0x3C)
    oled = sh1106(serial)
    while True:
        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        stats(oled, localtime)
        time.sleep(1)


if __name__ == "__main__":
    main()

