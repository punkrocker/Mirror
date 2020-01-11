from yeelight import discover_bulbs, Bulb
import random


def turn_on():
    # print(discover_bulbs())
    bulb = Bulb("10.0.0.20")
    bulb.turn_on()
    bulb.set_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
