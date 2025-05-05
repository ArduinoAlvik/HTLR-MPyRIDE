from arduino_alvik import ArduinoAlvik
import math
import time

robot = ArduinoAlvik()
robot.begin()

# Initialize position and heading
position = [0.0, 0.0]  # x, y in mm
heading = 0.0  # in degrees, 0 pointing along the positive X-axis

def forward(distance_mm):
    global position, heading
    robot.move(distance_mm, blocking=True)
    # Update position
    rad = math.radians(heading)
    position[0] += distance_mm * math.cos(rad)
    position[1] += distance_mm * math.sin(rad)

def backward(distance_mm):
    global position, heading
    robot.move(-distance_mm, blocking=True)
    # Update position
    rad = math.radians(heading)
    position[0] -= distance_mm * math.cos(rad)
    position[1] -= distance_mm * math.sin(rad)

def left(angle_degrees):
    global heading
    robot.rotate(angle_degrees, blocking=True)
    heading = (heading + angle_degrees) % 360

def right(angle_degrees):
    global heading
    robot.rotate(-angle_degrees, blocking=True)
    heading = (heading - angle_degrees) % 360

def goto(x, y):
    global position, heading
    # Save the current heading
    original_heading = heading
    
    dx = x - position[0]
    dy = y - position[1]
    distance = math.sqrt(dx * dx + dy * dy)
    
    # Calculate angle to the target
    target_angle = math.degrees(math.atan2(dy, dx))
    angle_to_turn = (target_angle - heading + 360) % 360
    if angle_to_turn > 180:
        angle_to_turn -= 360  # Shortest turn

    # Turn toward the target
    if angle_to_turn > 0:
        left(angle_to_turn)
    else:
        right(-angle_to_turn)
    
    # Move straight to the target
    forward(distance)
    
    # Now restore original heading
    heading_error = (original_heading - heading + 360) % 360
    if heading_error > 180:
        heading_error -= 360
    
    if heading_error > 0:
        left(heading_error)
    else:
        right(-heading_error)

def home():
    goto(0, 0)

def circle(radius_mm):
    pass