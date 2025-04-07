# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from arduino_alvik import ArduinoAlvik
from time import sleep_ms

ALVIK_NAME = "ALVIK24-3"
alvik = ArduinoAlvik()
alvik.left_led.set_color(1, 1, 0)  # GELB links
alvik.right_led.set_color(1, 1, 0) # GELB rechts
try:
    alvik.left_led.set_color(0, 1, 0)  # GRUEN links
    alvik.right_led.set_color(0, 1, 0)  # GRUEN rechts
    import ble_repl
    ble_repl.start(name=ALVIK_NAME)
except Exception as e:
    print("Fehler:", e)
    alvik.left_led.set_color(1, 0, 0) # ROT links
    alvik.right_led.set_color(1, 0, 0)  # ROT rechts
sleep_ms(50)  # Alvik braucht Zeit um die LEDs zu setzten


