#!/usr/bin/python
# -*- coding:utf-8 -*-

import sh1106 as SH1106
import time
import datetime

from PIL import Image, ImageDraw, ImageFont

try:
    disp = SH1106.SH1106()

    print("\r1.3inch OLED")
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    # Create blank image for drawing.
    font = ImageFont.truetype('Font.ttf', 20)
    font10 = ImageFont.truetype('Font.ttf', 13)
    today_last_time = "Unknown"
    while True:
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        draw.line([(0, 0), (127, 0)], fill=0)
        draw.line([(0, 0), (0, 63)], fill=0)
        draw.line([(0, 63), (127, 63)], fill=0)
        draw.line([(127, 0), (127, 63)], fill=0)
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")
        if today_time != today_last_time:
            today_last_time = today_time
            draw.text((30, 0), today_date, font=font10, fill=0)
            draw.text((28, 20), today_time, font=font, fill=0)
            disp.ShowImage(disp.getbuffer(image1))
        time.sleep(0.1)

except IOError as e:
    print(e)

except KeyboardInterrupt:
    print("ctrl + c:")
    exit()
