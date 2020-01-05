from yeelight import discover_bulbs, Bulb
import time
import random

# print(discover_bulbs())
bulb = Bulb("10.0.0.20")
bulb.turn_on()
while True:
    bulb.set_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    time.sleep(5)
