#!/usr/bin/python
# -*- coding:utf-8 -*-

import sh1106 as SH1106
import time
import datetime
import math
from PIL import Image, ImageDraw, ImageFont


def position(angle, arm_length):
    dx = int(math.cos(math.radians(angle)) * arm_length)
    dy = int(math.sin(math.radians(angle)) * arm_length)
    return dx, dy


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
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")
        if today_time != today_last_time:
            today_last_time = today_time
            margin = 4
            cx = 30
            cy = 32

            left = cx - cy
            right = cx + cy

            hrs_angle = 270 + (30 * (now.hour + (now.minute / 60.0)))
            hrs = position(hrs_angle, cy - margin - 7)

            min_angle = 270 + (6 * now.minute)
            mins = position(min_angle, cy - margin - 2)

            sec_angle = 270 + (6 * now.second)
            secs = position(sec_angle, cy - margin - 2)

            draw.ellipse((left + margin, margin, right - margin, 64 - margin), outline=0)
            draw.line((cx, cy, cx + hrs[0], cy + hrs[1]), fill=0)
            draw.line((cx, cy, cx + mins[0], cy + mins[1]), fill=0)
            draw.line((cx, cy, cx + secs[0], cy + secs[1]), fill=0)
            draw.ellipse((cx - 2, cy - 2, cx + 2, cy + 2), fill=0, outline="white")
            draw.text((2 * (cx + margin), cy - 8), today_date, fill=0)
            draw.text((2 * (cx + margin), cy), today_time, fill=0)
            disp.ShowImage(disp.getbuffer(image1))
        time.sleep(0.1)

except IOError as e:
    print(e)

except KeyboardInterrupt:
    print("ctrl + c:")
    exit()
