from machine import Pin
import time
# Alvik 12C Schnittstelle mit Led I2C direkt verbinden und
#dann A5 (Pin 12) auswählen auf alvik der ist VCC und den high oder low schalten
# Pins definieren
pin_A5 = Pin(12, Pin.OUT)  # GPIO 12 = HIGH A4

# Pin A4 auf HIGH setzen

# Pin A5 auf LOW setzen
pin_A5.value(0)

# Blinkschleife
while True:
    pin_A5.value(0)  # A5 LOW
    time.sleep(1)

    pin_A5.value(1)  # A5 HIGH
    time.sleep(1)
