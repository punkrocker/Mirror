from luma.core.interface.serial import i2c, spi
from luma.oled.device import sh1106

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)