import bluetooth
from ble_repl import uart
from arduino_alvik import ArduinoAlvik  # Importiere dein Alvik-Modul
import time

# Roboter starten
alvik = ArduinoAlvik()

# Bluetooth starten
print("running")

# Callback bei empfangenen Daten
def on_rx():
    try:
        cmd = uart.read().decode().strip()
        print("Empfangen:", cmd)
        if cmd == "U":
            alvik.move(50, blocking=False)
        elif cmd == "D":
            alvik.move(-50, blocking=False)
        elif cmd == "L":
            alvik.rotate(50, blocking=False)
        elif cmd == "R":
            alvik.rotate(-50, blocking=False)
        else:
            print("Unbekannter Befehl:", cmd)
    except Exception as e:
        print("Fehler:", e)

# Handler zuweisen
uart.irq(on_rx)

# Endlosschleife (kann ersetzt werden, wenn du z. B. weitere Logik hast)
while True:
    time.sleep(1)
    print("ASD")
