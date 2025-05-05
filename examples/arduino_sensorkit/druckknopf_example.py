from machine import Pin
import time

# Taster mit internem Pull-Up; Taster zwischen Pin und GND
button = Pin('A5', Pin.OUT)

# LED-Ausgang
button.value(0)

last_state = button.value()
last_debounce = time.ticks_ms()
debounce_delay = 50  # ms

while True:
    reading = button.value()
    # Bei Zustandswechsel Debounce-Timer starten
    if reading != last_state:
        last_debounce = time.ticks_ms()
    # Nach Verzögerung als gültig ansehen
    if time.ticks_diff(time.ticks_ms(), last_debounce) > debounce_delay:
        if reading == 0:  # gedrückt
            print("Button gedrückt")
        else:
            print("Button losgelassen")
    last_state = reading
    time.sleep_ms(10)
