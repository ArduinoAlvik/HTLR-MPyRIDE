# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import sys
from arduino_alvik import ArduinoAlvik
from time import sleep_ms

def blink(alvik, color_on, color_off, time_ms):
    alvik.left_led.set_color(*color_on)
    alvik.right_led.set_color(*color_on)
    sleep_ms(time_ms)
    alvik.left_led.set_color(*color_off)
    alvik.right_led.set_color(*color_off)
    sleep_ms(time_ms)

ALVIK_NAME = "ALVIK24-03"
alvik = ArduinoAlvik()
alvik.begin()

alvik.left_led.set_color(1, 1, 0)  # GELB links
alvik.right_led.set_color(1, 1, 0) # GELB rechts
try:
    alvik.left_led.set_color(0, 1, 0)  # GRUEN links
    alvik.right_led.set_color(0, 1, 0)  # GRUEN rechts
    import ble_repl
    ble_repl.start(name=ALVIK_NAME)
except Exception as e:
    sys.print_exception(e)
    while True:
        blink(alvik, (1, 0, 0), (0, 0, 0), 500)
