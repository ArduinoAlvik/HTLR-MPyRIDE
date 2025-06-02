from arduino_alvik import ArduinoAlvik  # Importiere dein Alvik-Modul
import time
from ble_repl import BLEUARTStream

def bewegung(cmd):
   try:
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

# Roboter starten
alvik = ArduinoAlvik()
alvik.begin()

# Bluetooth starten
BLEUARTStream.register_callback(bewegung)

# Endlosschleife (kann ersetzt werden, wenn du z.ÃÂÃÂÃÂÃÂ¢ÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ¯B. weitere Logik hast)
while True:
   time.sleep(1)