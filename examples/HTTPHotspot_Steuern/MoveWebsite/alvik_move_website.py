from alvik_http_server.alvik_http_server import AlvikHTTPServer
from alvik_utils.upy_streamwriter import UPYStreamWriter
from arduino_alvik import ArduinoAlvik
import os

try:
    import ure  # MicroPython Regex
except ImportError:
    import re as ure

ALVIK_NAME = "ALVIK24-03"
ALVIK_HOTSPOT_PW = "12345678"

class AlvikHTTPBootloader:
    def __init__(self):
        self.alvik = ArduinoAlvik()  # Dein Roboter-Objekt
        self.controller = AlvikHTTPServer("MoveWebsite/movesite_index.html")  # Dein HTML-Interface
        self.controller.add_endpoint("GET /command?dir=*", self._endpoint_command_move)

    def start_hotspot(self, ssid: str = ALVIK_NAME, password: str = ALVIK_HOTSPOT_PW):
        self.controller.start_hotspot(ssid, password)

    def start(self):
        self.controller.start_web_server()

    async def _endpoint_command_move(self, request: str, writer: UPYStreamWriter):
        """Verarbeitet Bewegungsbefehle."""
        try:
            direction = request.split("GET /command?dir=")[1].split(" ")[0]
            distance = 50  # Schrittweite in mm oder Grad
            unit = "mm"    # Einheit für Move

            if direction == 'up':
                print(f"Move up by {distance}")
                self.alvik.move(distance, blocking=False, unit=unit)
            elif direction == 'down':
                print(f"Move down by {distance}")
                self.alvik.move(-distance, blocking=False, unit=unit)
            elif direction == 'left':
                print(f"Rotate left by {distance}")
                self.alvik.rotate(distance, blocking=False)
            elif direction == 'right':
                print(f"Rotate right by {distance}")
                self.alvik.rotate(-distance, blocking=False)
            else:
                return 400, "Unknown direction"

            return 200, f"Command '{direction}' executed."

        except Exception as e:
            print(f"Error: {e}")
            return 500, "Internal Server Error"

if __name__ == "__main__":
    bootloader = AlvikHTTPBootloader()
    bootloader.start_hotspot()
    bootloader.start()