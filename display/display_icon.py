#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Display the Raspberry Pi logo (loads image as .png).
"""

import os.path
from PIL import Image
from oled_setting import get_device


def main():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            '../imgs', 'home.png'))
    logo = Image.open(img_path).convert("RGBA")
    fff = Image.new(logo.mode, logo.size, (0,) * 4)

    background = Image.new("RGBA", device.size, "black")
    posn = ((device.width - logo.width) // 2, 0)

    while True:
            img = Image.composite(logo, fff, logo)
            background.paste(img, posn)
            device.display(background.convert(device.mode))


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
