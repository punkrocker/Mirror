from yeelight import discover_bulbs, Bulb
import random

lights = discover_bulbs()


def turn_on(ip):
    bulb = Bulb(ip)
    bulb.turn_on()
    bulb.set_name("床头")
    # bulb.set_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
print(lights)

