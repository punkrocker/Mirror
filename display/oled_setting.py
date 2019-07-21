from luma.oled.device import sh1106
from luma.core.interface.serial import i2c


def get_device():
    serial = i2c(port=1, address=0x3C)
    device = sh1106(serial)
    return device
