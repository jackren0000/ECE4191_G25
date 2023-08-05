######### This is the motor control test using gpiozero.Robot library

from gpiozero import Robot, PiGPIOFactory
from time import sleep

# Define the pin factory
# pin_factory = PiGPIOFactory()

# Initialize the robot
robot = Robot(left=(17, 27), right=(22, 23))

# Move forward
print('Moving forward')
robot.forward()
sleep(2) # Move for 2s

# Move backward
print('Moving backward')
robot.backward()
sleep(2) # Move for 2s

# Turn right
print('Turning right')
robot.right()
sleep(2) # Turn for 2s

# Turn left
print('Turning left')
robot.left()
sleep(2)

# Stop
print('Stopping')
robot.stop()
