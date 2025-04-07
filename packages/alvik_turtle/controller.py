from arduino_alvik import ArduinoAlvik
import time

robot = ArduinoAlvik()
robot.begin()

def forward(distance_mm):
    """Move the robot forward by a specified distance in millimeters."""
    robot.drive(distance_mm, unit='mm', speed=50) 
    time.sleep(1)

def backward(distance_mm):
    """Move the robot backward by a specified distance in millimeters."""
    robot.drive(-distance_mm, unit='mm', speed=50)
    time.sleep(1)

def left(angle_degrees):
    """Rotate the robot left by a specified angle in degrees."""
    robot.rotate(-angle_degrees, unit='deg', speed=50)
    time.sleep(1)

def right(angle_degrees):
    """Rotate the robot right by a specified angle in degrees."""
    robot.rotate(angle_degrees, unit='deg', speed=50)
    time.sleep(1)