import RPi.GPIO as GPIO
import sys
import time


class Led():
    def __init__(self):
        self.led_pin = 25
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.output(self.led_pin, GPIO.LOW)

    def on(self):
        GPIO.output(self.led_pin, GPIO.HIGH)
        print('LED-ON')

    def off(self):
        GPIO.output(self.led_pin, GPIO.LOW)
        print('LED-OFF')


def main(status):
    led = Led()
    if status == 'on':
        led.on()
    elif status == 'off':
        led.off()


if __name__ == '__main__':
    main(sys.argv[1])
